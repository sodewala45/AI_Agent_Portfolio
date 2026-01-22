import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# 1. PAGE SETUP
st.set_page_config(page_title="AI Agent Portfolio | Master Dashboard", layout="wide")

# Custom CSS for the Navy Blue Button and Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #f0f2f6;
    }
    /* Navy Blue LinkedIn Button */
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
        margin-top: 20px;
    }
    .linkedin-btn:hover {
        background-color: #000066;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. ANALYTICS SESSION STATE
if 'analytics' not in st.session_state:
    st.session_state.analytics = {
        "TikTok Agent": 12,
        "Logistics Agent": 8,
        "Job Hunter": 25
    }

# 3. HEADER SECTION
st.title("🌐 My AI Agent Ecosystem")
st.markdown("##### Exploring the intersection of Automation, NLP, and Efficiency.")

# 4. ANALYTICS DASHBOARD (Admin View)
with st.expander("📊 Portfolio Engagement Analytics"):
    st.write("Real-time tracking of project interest:")
    df_stats = pd.DataFrame({
        'Agent': list(st.session_state.analytics.keys()),
        'Clicks': list(st.session_state.analytics.values())
    })
    st.bar_chart(df_stats.set_index('Agent'))

st.divider()

# 5. AGENT GRID
col1, col2, col3 = st.columns(3)

def create_agent_card(column, title, desc, link, key):
    with column:
        st.subheader(title)
        st.write(desc)
        if st.button(f"Launch {title}", key=key):
            st.session_state.analytics[title] += 1
            # JavaScript to open the link in a new tab
            components.html(f"""
                <script>
                window.open('{link}', '_blank');
                </script>
            """, height=0)
            st.rerun()

create_agent_card(col1, "📈 TikTok Agent", "E-commerce Lead Gen & Content Automation.", "https://huggingface.co/spaces/sodewala45/TikTok_Agent", "btn1")
create_agent_card(col2, "🚛 Logistics Agent", "Supply Chain Route & Inventory Optimizer.", "https://huggingface.co/spaces/sodewala45/Logistics_Agent", "btn2")
create_agent_card(col3, "🎯 Job Hunter", "Autonomous Job Scouting & Match Filtering.", "https://huggingface.co/spaces/sodewala45/Job_Search_Agent", "btn3")

st.divider()

# 6. FOOTER / CONTACT SECTION
f_col1, f_col2, f_col3 = st.columns([1, 2, 1])

with f_col2:
    st.write("### Let's Build Something Together")
    st.write("I'm currently open to roles in AI Automation and Python Development.")
    
    # THE NAVY BLUE LINKEDIN BUTTON
    # Replace '#' with your actual LinkedIn profile URL
    st.markdown("""
        <a href="https://www.linkedin.com/in/YOUR_USERNAME" target="_blank" class="linkedin-btn">
            Connect with me on LinkedIn
        </a>
    """, unsafe_allow_html=True)
