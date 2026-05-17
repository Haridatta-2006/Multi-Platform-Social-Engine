import streamlit as st
# pyrefly: ignore [missing-import]
import google.generativeai as genai
import json

# Configure Gemini
API_KEY = "AIzaSyAooP4cpCgS1vR0gsT-VAtFUw7t64jzvfg"
genai.configure(api_key=API_KEY)

# Generation config to ensure JSON output
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 4096,
    "response_mime_type": "application/json"
}

# The best model available currently for general text tasks
model = genai.GenerativeModel("gemini-1.5-pro", generation_config=generation_config)

st.set_page_config(page_title="Social Engine", page_icon="🚀", layout="wide")

# Custom CSS for the UI
st.markdown("""
<style>
    .stApp {
        background-color: #0b0f19;
        color: #f8fafc;
    }
    .header-box {
        background: linear-gradient(135deg, #1e3a8a, #8b5cf6);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid rgba(255,255,255,0.1);
    }
    .header-box h1 { color: white; font-weight: 900; font-size: 3.5rem; margin: 0; letter-spacing: -1px; }
    .header-box p { color: #cbd5e1; font-size: 1.3rem; margin-top: 15px; font-weight: 500;}
    
    .stTextArea textarea {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
        padding: 15px !important;
    }
    
    .agent-card {
        background: linear-gradient(145deg, rgba(30,41,59,0.8), rgba(15,23,42,0.9));
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        height: 100%;
    }
    .agent-card:hover {
        transform: translateY(-5px);
        border-color: rgba(255,255,255,0.2);
    }
    
    .agent-title {
        font-size: 1.4rem;
        font-weight: 800;
        margin-bottom: 20px;
        padding-bottom: 15px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .insta-title { background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .linkedin-title { color: #0077b5; }
    .article-title { color: #10b981; }
    .bot-title { color: #f59e0b; }
    
    .content-box {
        white-space: pre-wrap;
        font-size: 1.05rem;
        line-height: 1.7;
        color: #e2e8f0;
    }
    
    .hashtag-container {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 15px;
        padding: 25px;
        background: rgba(30,41,59,0.5);
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.05);
    }
    .hashtag {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: white;
        padding: 8px 18px;
        border-radius: 25px;
        font-size: 0.95rem;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(99, 102, 241, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-box">
    <h1>LangGraph Workflow</h1>
    <p>Multi-Platform Social Engine</p>
</div>
""", unsafe_allow_html=True)

# Input Section
st.markdown("### 👤 Human Input: Topic & Context")
user_input = st.text_area("Enter your topic, context, or raw ideas here:", height=150, placeholder="e.g., We are launching a new Agentic AI workshop that teaches how to build multi-agent workflows using LangGraph and Streamlit. It's happening next weekend, totally free for students.")

def generate_content(topic):
    prompt = f"""
    You are an AI Orchestrator managing a LangGraph workflow. You have 4 specialized agents and 1 shared tool.
    Based on the following Human Input: "{topic}", your task is to delegate content creation to your agents and return a strict JSON output.
    
    AGENTS:
    1. Instagram Agent: Create a catchy, visually appealing Instagram caption with emojis. Keep it engaging and concise.
    2. LinkedIn Post Agent: Create a professional, thought-provoking short post for LinkedIn to drive engagement.
    3. LinkedIn Article Agent: Write a structured, multi-paragraph article (like a blog post) detailing the topic with a professional tone.
    4. Announcement Bot: Generate a short, enthusiastic message (like a Slack/Discord announcement) to share with an internal network.
    5. Shared Tooling (Hashtag Generator): Generate a list of 5-8 highly relevant, trending hashtags based on the content.
    
    Output exactly in this JSON format:
    {{
        "instagram_caption": "...",
        "linkedin_post": "...",
        "linkedin_article": "...",
        "announcement": "...",
        "hashtags": ["#tag1", "#tag2", "..."]
    }}
    """
    
    try:
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        return {"error": str(e)}

# Generate Button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 Run Orchestrator", use_container_width=True, type="primary"):
    if not user_input.strip():
        st.warning("Please enter a topic first!")
    else:
        with st.spinner("🧠 The Brain is orchestrating your specialized agents..."):
            results = generate_content(user_input)
            
            if "error" in results:
                st.error(f"Error communicating with AI: {results['error']}")
            else:
                st.success("✅ Workflow Complete! All agents have successfully generated content.")
                
                st.markdown("<hr style='border-color: rgba(255,255,255,0.1); margin: 40px 0;'>", unsafe_allow_html=True)
                st.markdown("### 🤖 Agents Output")
                
                c1, c2 = st.columns(2)
                
                with c1:
                    st.markdown(f"""
                    <div class="agent-card">
                        <div class="agent-title"><span style="font-size: 1.8rem;">📷</span> <span class="insta-title">Agent 1: Instagram Caption</span></div>
                        <div class="content-box">{results.get('instagram_caption', 'N/A')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                with c2:
                    st.markdown(f"""
                    <div class="agent-card">
                        <div class="agent-title"><span style="font-size: 1.8rem;">💼</span> <span class="linkedin-title">Agent 2: LinkedIn Post</span></div>
                        <div class="content-box">{results.get('linkedin_post', 'N/A')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                st.markdown("<br>", unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="agent-card">
                    <div class="agent-title"><span style="font-size: 1.8rem;">📰</span> <span class="article-title">Agent 3: LinkedIn Article</span></div>
                    <div class="content-box">{results.get('linkedin_article', 'N/A')}</div>
                </div>
                """, unsafe_allow_html=True)
                    
                st.markdown(f"""
                <div class="agent-card">
                    <div class="agent-title"><span style="font-size: 1.8rem;">📢</span> <span class="bot-title">Agent 4: Announcement Bot</span></div>
                    <div class="content-box">{results.get('announcement', 'N/A')}</div>
                </div>
                """, unsafe_allow_html=True)
                    
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("### 🛠️ Shared Tooling: Hashtag Generator")
                tags_html = "".join([f'<span class="hashtag">{tag}</span>' for tag in results.get('hashtags', [])])
                st.markdown(f'<div class="hashtag-container">{tags_html}</div>', unsafe_allow_html=True)
