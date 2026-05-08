from langgraph.graph import StateGraph, START, END
from graph.state import AgentState
from agents.nodes import (
    instagram_agent,
    linkedin_post_agent,
    linkedin_article_agent,
    announcement_agent
)

def router(state: AgentState):
    if not state.get("instagram_caption"):
        return "instagram_agent"
    elif not state.get("linkedin_post"):
        return "linkedin_post_agent"
    elif not state.get("linkedin_article"):
        return "linkedin_article_agent"
    elif not state.get("announcement_message"):
        return "announcement_agent"
    return END

workflow = StateGraph(AgentState)

workflow.add_node("instagram_agent", instagram_agent)
workflow.add_node("linkedin_post_agent", linkedin_post_agent)
workflow.add_node("linkedin_article_agent", linkedin_article_agent)
workflow.add_node("announcement_agent", announcement_agent)

workflow.add_conditional_edges(START, router)
workflow.add_edge("instagram_agent", "linkedin_post_agent")
workflow.add_edge("linkedin_post_agent", "linkedin_article_agent")
workflow.add_edge("linkedin_article_agent", "announcement_agent")
workflow.add_edge("announcement_agent", END)

app = workflow.compile()

print("✅ LangGraph Workflow Compiled Successfully!")
