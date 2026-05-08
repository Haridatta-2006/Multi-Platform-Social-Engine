import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import everything safely
import importlib.util

def import_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Import main
main = import_module("main", "main.py")
run_social_engine = main.run_social_engine

import gradio as gr

def generate_content(topic, context, platforms):
    if not topic or not topic.strip():
        return ["❌ Please enter a topic!"] * 4
    
    result = run_social_engine(topic.strip(), context.strip() if context else "")
    
    ig = result.get("instagram_caption", "Not generated") if "Instagram" in platforms else "Not selected"
    li_post = result.get("linkedin_post", "Not generated") if "LinkedIn Post" in platforms else "Not selected"
    li_article = result.get("linkedin_article", "Not generated") if "LinkedIn Article" in platforms else "Not selected"
    ann = result.get("announcement_message", "Not generated") if "Announcement" in platforms else "Not selected"
    
    return ig, li_post, li_article, ann

with gr.Blocks(title="Multi-Platform Social Engine", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 Multi-Platform Social Engine\n**LangGraph Multi-Agent AI**")
    
    with gr.Row():
        with gr.Column(scale=1):
            topic = gr.Textbox(label="Main Topic", placeholder="Enter any topic...", lines=2)
            context = gr.Textbox(label="Context (Optional)", placeholder="Target audience or extra details", lines=3)
            platforms = gr.CheckboxGroup(
                choices=["Instagram", "LinkedIn Post", "LinkedIn Article", "Announcement"],
                value=["Instagram", "LinkedIn Post"],
                label="Select Platforms"
            )
            btn = gr.Button("Generate Content", variant="primary")
        
        with gr.Column(scale=2):
            with gr.Tab("📸 Instagram"): ig_out = gr.Textbox(lines=10)
            with gr.Tab("💼 LinkedIn Post"): post_out = gr.Textbox(lines=10)
            with gr.Tab("📝 LinkedIn Article"): article_out = gr.Textbox(lines=14)
            with gr.Tab("📢 Announcement"): ann_out = gr.Textbox(lines=6)
    
    btn.click(generate_content, [topic, context, platforms], [ig_out, post_out, article_out, ann_out])

demo.launch()
