import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="AI Agent Portfolio", page_icon="🚀", layout="wide")

# Custom CSS for a premium "Software House" look
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .agent-card {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border: 1px solid #e1e4e8;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. HEADER
st.title("🤖 My Autonomous AI Agent Suite")
st.markdown("#### High-impact automation tools for E-commerce, Logistics, and Career Growth.")
st.divider()

# 3. THE AGENT GRID
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""<div class="agent-card">
    <h3>📈 TikTok Shop Agent</h3>
    <p>Automated lead generation and niche analysis for viral e-commerce growth.</p>
    </div>""", unsafe_allow_html=True)
    st.link_button("Launch Agent", "https://huggingface.co/spaces/sodewala45/TikTok_Agent")

with col2:
    st.markdown("""<div class="agent-card">
    <h3>🚛 Logistics Agent</h3>
    <p>AI-driven route optimization and supply chain intelligence dashboard.</p>
    </div>""", unsafe_allow_html=True)
    st.link_button("Launch Agent", "https://huggingface.co/spaces/sodewala45/Logistics_Agent")

with col3:
    st.markdown("""<div class="agent-card">
    <h3>🎯 AI Elite linkedin Auto Job Hunter & Poster</h3>
    <p>Autonomous job discovery with >50% match filtering and one-click outreach.</p>
    </div>""", unsafe_allow_html=True)
    # Ensure this link matches your NEW Job Search Space URL
    st.link_button("Launch Agent", "https://huggingface.co/spaces/sodewala45/Job_Search_Agent")

st.divider()

# 4. CONTACT / FOOTER
st.subheader("📬 Let's Connect")
c1, c2, c3 = st.columns(3)
with c1:
    st.info("**Available for Remote AI Roles**")
with c2:
    st.success("**Expertise: Python, CI/CD, Streamlit**")
with c3:
    st.link_button("View My LinkedIn", "https://www.linkedin.com/in/sodewala")
