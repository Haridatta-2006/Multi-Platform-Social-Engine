import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gradio as gr

# === Self-contained import to avoid errors ===
try:
    from main import run_social_engine
except:
    # Fallback: Load main.py directly
    import importlib.util
    spec = importlib.util.spec_from_file_location("main", "main.py")
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)
    run_social_engine = main_module.run_social_engine

def generate_content(topic, context, platforms):
    if not topic or not topic.strip():
        return ["❌ Please enter a topic!"] * 4
    
    try:
        result = run_social_engine(topic.strip(), context.strip() if context else "")
        
        ig = result.get("instagram_caption", "Not generated") if "Instagram" in platforms else "Not selected"
        li_post = result.get("linkedin_post", "Not generated") if "LinkedIn Post" in platforms else "Not selected"
        li_article = result.get("linkedin_article", "Not generated") if "LinkedIn Article" in platforms else "Not selected"
        ann = result.get("announcement_message", "Not generated") if "Announcement" in platforms else "Not selected"
        
        return ig, li_post, li_article, ann
    except Exception as e:
        error = f"❌ Error: {str(e)}"
        return error, error, error, error


with gr.Blocks(title="Multi-Platform Social Engine", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🚀 Multi-Platform Social Engine
    **LangGraph Multi-Agent AI System**
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            topic = gr.Textbox(label="📌 Main Topic", placeholder="Enter any topic...", lines=2)
            context = gr.Textbox(label="📝 Context (Optional)", placeholder="Target audience or extra info", lines=3)
            
            platforms = gr.CheckboxGroup(
                choices=["Instagram", "LinkedIn Post", "LinkedIn Article", "Announcement"],
                value=["Instagram", "LinkedIn Post"],
                label="Select Platforms"
            )
            btn = gr.Button("✨ Generate Content", variant="primary", size="large")
        
        with gr.Column(scale=2):
            with gr.Tab("📸 Instagram"): 
                ig_out = gr.Textbox(lines=10)
            with gr.Tab("💼 LinkedIn Post"): 
                post_out = gr.Textbox(lines=10)
            with gr.Tab("📝 LinkedIn Article"): 
                article_out = gr.Textbox(lines=14)
            with gr.Tab("📢 Announcement"): 
                ann_out = gr.Textbox(lines=6)
    
    btn.click(
        generate_content, 
        inputs=[topic, context, platforms], 
        outputs=[ig_out, post_out, article_out, ann_out]
    )

demo.launch()
