
from langgraph.graph import StateGraph, START, END
from typing import Literal
from graph.state import AgentState
from agents.nodes import (
    instagram_agent,
    linkedin_post_agent,
    linkedin_article_agent,
    announcement_agent
)

def smart_router(state: AgentState) -> Literal["instagram_agent", "linkedin_post_agent", "linkedin_article_agent", "announcement_agent", END]:
    """Decides next agent based on what has been generated"""
    if not state.get("instagram_caption"):
        return "instagram_agent"
    elif not state.get("linkedin_post"):
        return "linkedin_post_agent"
    elif not state.get("linkedin_article"):
        return "linkedin_article_agent"
    elif not state.get("announcement_message"):
        return "announcement_agent"
    else:
        return END

# Build Graph
workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("instagram_agent", instagram_agent)
workflow.add_node("linkedin_post_agent", linkedin_post_agent)
workflow.add_node("linkedin_article_agent", linkedin_article_agent)
workflow.add_node("announcement_agent", announcement_agent)

# Conditional Routing
workflow.add_conditional_edges(
    START,
    smart_router,
    {
        "instagram_agent": "instagram_agent",
        "linkedin_post_agent": "linkedin_post_agent",
        "linkedin_article_agent": "linkedin_article_agent",
        "announcement_agent": "announcement_agent",
        END: END
    }
)

# Sequential fallback
workflow.add_edge("instagram_agent", "linkedin_post_agent")
workflow.add_edge("linkedin_post_agent", "linkedin_article_agent")
workflow.add_edge("linkedin_article_agent", "announcement_agent")
workflow.add_edge("announcement_agent", END)

app = workflow.compile()

print("✅ Improved LangGraph Orchestrator Ready!")
