
from typing import Dict
from graph.state import AgentState
from agents.config import AGENT_CONFIG
from tools.hashtag_generator import hashtag_generator
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

def create_agent_node(agent_name: str):
    config = AGENT_CONFIG[agent_name]

    def agent_node(state: AgentState) -> Dict:
        # Generate hashtags using shared tool
        hashtags = hashtag_generator.invoke({
            "topic": state.get("topic", ""),
            "context": state.get("context", ""),
            "count": 12 if agent_name == "instagram_caption" else 8,
            "platform": "instagram" if agent_name == "instagram_caption" else "linkedin"
        })

        # Add hashtags to context
        enhanced_context = f"{state.get('context', '')}\n\nRelevant Hashtags: {', '.join(hashtags)}"

        prompt_text = config["prompt"].format(
            topic=state.get("topic", ""),
            context=enhanced_context
        )

        messages = state.get("messages", []) + [{"role": "user", "content": prompt_text}]

        response = client.chat.completions.create(
            model="mixtral-8x7b-32768"
            messages=messages,
            temperature=0.7,
            max_tokens=400                  # Reduced
        )

        content = response.choices[0].message.content.strip()

        output = {}
        if agent_name == "instagram_caption":
            output["instagram_caption"] = content
            output["hashtags"] = hashtags
        elif agent_name == "linkedin_post":
            output["linkedin_post"] = content
        elif agent_name == "linkedin_article":
            output["linkedin_article"] = content
        elif agent_name == "announcement":
            output["announcement_message"] = content

        return {
            "messages": messages + [{"role": "assistant", "content": content}],
            **output,
            "next_agent": None
        }

    return agent_node


# Re-initialize agents
instagram_agent = create_agent_node("instagram_caption")
linkedin_post_agent = create_agent_node("linkedin_post")
linkedin_article_agent = create_agent_node("linkedin_article")
announcement_agent = create_agent_node("announcement")

print("✅ Agents updated with Hashtag Tool Integration!")
