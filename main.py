
from graph.graph import app
from utils.output import print_results
from graph.state import AgentState

def run_social_engine(topic: str, context: str = ""):
    """Main function to run the Multi-Platform Social Engine"""

    print("🚀 Starting Multi-Platform Social Engine...\n")

    input_state = AgentState(
        topic=topic,
        context=context,
        messages=[]
    )

    final_state = app.invoke(input_state)
    print_results(final_state)

    return final_state

# Example usage
if __name__ == "__main__":
    result = run_social_engine(
        topic="AI Agents Revolution in 2026",
        context="How autonomous AI agents will transform software development and content creation"
    )
