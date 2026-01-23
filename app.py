import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# 1. PAGE SETUP
st.set_page_config(page_title="AI Agent Portfolio", layout="wide", page_icon="🤖")

# Custom CSS for UI & Navy Blue LinkedIn Button
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .linkedin-btn {
        display: inline-block;
        padding: 0.75em 1.5em;
        background-color: #000080; /* Navy Blue */
        color: white !important;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        width: 100%;
        transition: 0.3s;
    }
    .linkedin-btn:hover {
        background-color: #000066;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }
    .agent-card {
        padding: 25px;
        border-radius: 15px;
        background-color: #ffffff;
        border: 1px solid #e1e4e8;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ANALYTICS (Session-based)
if 'analytics' not in st.session_state:
    st.session_state.analytics = {"TikTok Agent": 12, "Logistics Agent": 8, "Job Hunter": 25}

# 3. HEADER
st.title("🌐 My AI Agent Ecosystem")
st.info("A showcase of autonomous solutions for content, logistics, and career growth.")

# 4. VISITOR ANALYTICS (Admin View)
with st.expander("📊 Project Engagement Metrics (Admin)"):
    df_stats = pd.DataFrame({
        'Agent': list(st.session_state.analytics.keys()),
        'Clicks': list(st.session_state.analytics.values())
    })
    st.bar_chart(df_stats.set_index('Agent'))

st.divider()

# 5. THE AGENT GRID
col1, col2, col3 = st.columns(3)

# --- Ensure these URLs are exactly correct ---
links = {
    "TikTok": "https://huggingface.co/spaces/sodewala45/TikTok_Agent",
    "Logistics": "https://huggingface.co/spaces/sodewala45/Logistics_Agent",
    "Job": "https://huggingface.co/spaces/sodewala45/Job_Search_Agent"
}

with col1:
    st.markdown('<div class="agent-card"><h3>📈 TikTok Agent</h3><p>E-commerce Lead Generation & Content Automation</p></div>', unsafe_allow_html=True)
    if st.button("🚀 Launch TikTok Agent", key="tk"):
        st.session_state.analytics["TikTok Agent"] += 1
        components.html(f'<script>window.open("{links["TikTok"]}", "_blank");</script>', height=0)

with col2:
    st.markdown('<div class="agent-card"><h3>🚛 Logistics Agent</h3><p>Supply Chain Route & Inventory Optimizer</p></div>', unsafe_allow_html=True)
    if st.button("🚀 Launch Logistics Agent", key="lg"):
        st.session_state.analytics["Logistics Agent"] += 1
        components.html(f'<script>window.open("{links["Logistics"]}", "_blank");</script>', height=0)

with col3:
    st.markdown('<div class="agent-card"><h3>🎯 Job Hunter</h3><p>Autonomous Job Scouting & Match Filtering</p></div>', unsafe_allow_html=True)
    if st.button("🚀 Launch Job Hunter", key="jh"):
        st.session_state.analytics["Job Hunter"] += 1
        components.html(f'<script>window.open("{links["Job"]}", "_blank");</script>', height=0)

st.divider()

# 6. FOOTER: LinkedIn & Visitor Map
footer_col1, footer_col2 = st.columns([2, 1])

with footer_col1:
    st.write("### 🤝 Let's Connect")
    st.write("I build AI agents that solve real-world problems. Currently open to remote Python/AI Automation opportunities.")
    # UPDATE: Replace with your actual LinkedIn URL
    st.markdown('<a href="https://www.linkedin.com/in/YOUR_LINKEDIN_HERE" target="_blank" class="linkedin-btn">Connect on LinkedIn</a>', unsafe_allow_html=True)

with footer_col2:
    st.write("### 🌍 Global Visitors")
    # Your specific ClustrMaps Script
    components.html("""
    <div style="text-align: center;">
        <script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=-RMm3VS_E9b9mkmGW_O58Wee3vYnV3UGDJs2xuT2fMU&cl=ffffff&w=a"></script>
    </div>
    """, height=250)
