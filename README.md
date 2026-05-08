# Multi-Platform Social Engine - LangGraph Agentic AI

**Production-Level Multi-Agent System** for generating optimized content across Instagram, LinkedIn, and more.

### ✨ Features
- **LangGraph Orchestrator** (Stateful Multi-Agent Workflow)
- 4 Specialized Agents (Instagram, LinkedIn Post, LinkedIn Article, Announcement Bot)
- Shared Tool: Intelligent Hashtag Generator
- Groq LLM Integration (Fast & Cost-effective)
- Clean Project Structure with proper package organization

### 🏗️ Architecture
- **Human Input** → **LangGraph Brain** → Routes to specialized agents
- Agents use shared tools and maintain conversation memory
- Sequential + Conditional Routing

### 🚀 How to Run

```python
from main import run_social_engine

result = run_social_engine(
    topic="Your Topic Here",
    context="Additional context or target audience"
)
