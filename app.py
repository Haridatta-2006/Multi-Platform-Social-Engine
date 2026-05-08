import streamlit as st
from main import run_social_engine

st.set_page_config(
    page_title="Multi-Platform Social Engine",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Multi-Platform Social Engine")
st.markdown("**LangGraph Powered Multi-Agent AI System**")

# Sidebar
with st.sidebar:
    st.header("🎛️ Controls")
    
    platforms = st.multiselect(
        "Select Platforms",
        options=["Instagram", "LinkedIn Post", "LinkedIn Article", "Announcement"],
        default=["Instagram", "LinkedIn Post"]
    )
    
    generate_btn = st.button("✨ Generate Content", type="primary", use_container_width=True)

# Main Area
col1, col2 = st.columns([1, 2])

with col1:
    topic = st.text_input("📌 Main Topic", 
                         placeholder="e.g. The Psychology Behind Great Movie Villains")
    
    context = st.text_area("📝 Context / Target Audience", 
                          placeholder="e.g. For movie lovers and film students", 
                          height=120)

with col2:
    if generate_btn and topic.strip():
        with st.spinner("🤖 Multi-Agents are working..."):
            result = run_social_engine(topic, context or "")
            
            st.success("✅ Content Generated Successfully!")
            
            if "Instagram" in platforms:
                st.subheader("📸 Instagram Caption")
                st.write(result.get("instagram_caption", ""))
                st.divider()
            
            if "LinkedIn Post" in platforms:
                st.subheader("💼 LinkedIn Post")
                st.write(result.get("linkedin_post", ""))
                st.divider()
            
            if "LinkedIn Article" in platforms:
                st.subheader("📝 LinkedIn Article")
                article = result.get("linkedin_article", "")
                st.write(article[:2500] + "..." if len(article) > 2500 else article)
                st.divider()
            
            if "Announcement" in platforms:
                st.subheader("📢 Announcement")
                st.write(result.get("announcement_message", ""))
    
    elif generate_btn:
        st.warning("Please enter a topic!")

st.markdown("---")
st.caption("Built with LangGraph • Groq • Streamlit")