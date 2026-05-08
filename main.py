%%writefile app.py

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gradio as gr
from main import run_social_engine

def generate_movie_content(topic, context, platforms):
    if not topic or not topic.strip():
        return ["❌ Please enter a movie topic!"] * 4
    
    result = run_social_engine(topic.strip(), context.strip() if context else "")
    
    outputs = []
    for p in ["Instagram", "LinkedIn Post", "LinkedIn Article", "Announcement"]:
        if p in platforms:
            if p == "Instagram":
                outputs.append(result.get("instagram_caption", "Not generated"))
            elif p == "LinkedIn Post":
                outputs.append(result.get("linkedin_post", "Not generated"))
            elif p == "LinkedIn Article":
                outputs.append(result.get("linkedin_article", "Not generated"))
            else:
                outputs.append(result.get("announcement_message", "Not generated"))
        else:
            outputs.append("Not selected")
    
    return outputs

with gr.Blocks(title="🎥 Movie Social Engine", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🎬 Movie Content Generator
    **LangGraph Multi-Agent AI System** - Powered by Groq
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            topic = gr.Textbox(
                label="🎞️ Movie Topic",
                placeholder="e.g. Why Interstellar is Still the Best Sci-Fi Movie",
                lines=2
            )
            context = gr.Textbox(
                label="📝 Context / Target Audience",
                placeholder="e.g. For sci-fi lovers and movie enthusiasts",
                lines=3
            )
            platforms = gr.CheckboxGroup(
                choices=["Instagram", "LinkedIn Post", "LinkedIn Article", "Announcement"],
                value=["Instagram", "LinkedIn Post"],
                label="Select Platforms to Generate"
            )
            btn = gr.Button("🚀 Generate Content", variant="primary", size="large")
        
        with gr.Column(scale=2):
            with gr.Tab("📸 Instagram Caption"):
                ig = gr.Textbox(lines=10)
            with gr.Tab("💼 LinkedIn Post"):
                post = gr.Textbox(lines=10)
            with gr.Tab("📝 LinkedIn Article"):
                article = gr.Textbox(lines=14)
            with gr.Tab("📢 Announcement"):
                ann = gr.Textbox(lines=6)
    
    btn.click(
        generate_movie_content,
        inputs=[topic, context, platforms],
        outputs=[ig, post, article, ann]
    )

    gr.Markdown("---\nBuilt with ❤️ using **LangGraph + Groq**")

if __name__ == "__main__":
    demo.launch(share=True)
