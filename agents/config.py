
from prompts.instagram import INSTAGRAM_CAPTION_PROMPT
from prompts.linkedin_post import LINKEDIN_POST_PROMPT
from prompts.linkedin_article import LINKEDIN_ARTICLE_PROMPT
from prompts.announcement import ANNOUNCEMENT_PROMPT

AGENT_CONFIG = {
    "instagram_caption": {
        "name": "Instagram Caption Generator",
        "prompt": INSTAGRAM_CAPTION_PROMPT,
        "description": "Creates engaging Instagram captions"
    },
    "linkedin_post": {
        "name": "LinkedIn Post Generator",
        "prompt": LINKEDIN_POST_PROMPT,
        "description": "Creates professional LinkedIn posts"
    },
    "linkedin_article": {
        "name": "LinkedIn Article Writer",
        "prompt": LINKEDIN_ARTICLE_PROMPT,
        "description": "Writes long-form LinkedIn articles"
    },
    "announcement": {
        "name": "Announcement Bot",
        "prompt": ANNOUNCEMENT_PROMPT,
        "description": "Generates cross-platform sharing messages"
    }
}
