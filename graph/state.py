
from typing import TypedDict, Annotated, List, Dict, Optional
from langgraph.graph import add_messages

class AgentState(TypedDict):
    """Main state for the entire LangGraph workflow"""

    # Core input
    topic: str
    context: str                      # Additional details from user

    # Messages for conversation/memory
    messages: Annotated[List, add_messages]

    # Generated content from different agents
    instagram_caption: Optional[str]
    linkedin_post: Optional[str]
    linkedin_article: Optional[str]
    announcement_message: Optional[str]

    # Shared data
    hashtags: Optional[List[str]]

    # Routing and control
    next_agent: Optional[str]         # Which agent to call next
    final_output: Optional[Dict]      # Compiled final result
