
from langchain_core.tools import tool
from typing import List
import re

@tool
def hashtag_generator(topic: str, context: str = "", count: int = 10, platform: str = "general") -> List[str]:
    """
    Generates optimized hashtags based on topic, context and target platform.

    Args:
        topic: Main topic
        context: Additional context
        count: Number of hashtags to generate (max 15)
        platform: Target platform (instagram, linkedin, general)
    """
    # Combine topic and context
    text = f"{topic} {context}".strip()

    # Basic keyword extraction (in production you could use LLM or NLP)
    words = re.findall(r'\b\w+\b', text.lower())
    keywords = list(set(words))[:8]

    base_hashtags = [word.capitalize() for word in keywords if len(word) > 3]

    # Platform-specific hashtags
    platform_tags = {
        "instagram": ["InstaDaily", "ExplorePage", "Viral", "Trending", "Aesthetic"],
        "linkedin": ["Leadership", "ProfessionalDevelopment", "Innovation", "ThoughtLeadership", "CareerGrowth"],
        "general": ["Motivation", "Success", "Growth", "Future", "Ideas"]
    }

    extra = platform_tags.get(platform.lower(), platform_tags["general"])

    all_tags = base_hashtags + extra
    hashtags = [f"#{tag}" for tag in all_tags[:count]]

    return hashtags
