import streamlit as st
import pandas as pd  # <--- This fixes the error!
import streamlit.components.v1 as components

# 1. PAGE SETUP
st.set_page_config(page_title="AI Agent Portfolio", layout="wide")

# 2. ANALYTICS SESSION STATE
# Note: On Hugging Face, this resets when the app sleeps. 
# For permanent storage, we would connect Google Sheets next.
if 'analytics' not in st.session_state:
    st.session_state.analytics = {
        "TikTok Agent": 0,
        "Logistics Agent": 0,
        "Job Hunter": 0
    }

# 3. ANALYTICS DASHBOARD (Admin View)
st.title("🌐 My AI Agent Ecosystem")

with st.expander("📊 Portfolio Analytics (Admin)"):
    st.write("Real-time engagement tracking:")
    # Create the DataFrame safely now that pd is imported
    df_stats = pd.DataFrame({
        'Agent': list(st.session_state.analytics.keys()),
        'Clicks': list(st.session_state.analytics.values())
    })
    st.bar_chart(df_stats.set_index('Agent'))

st.divider()

# 4. AGENT GRID
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

create_agent_card(col1, "TikTok Agent", "E-commerce Lead Gen & Content Automation.", "https://huggingface.co/spaces/sodewala45/TikTok_Agent", "btn1")
create_agent_card(col2, "Logistics Agent", "Supply Chain Route & Inventory Optimizer.", "https://huggingface.co/spaces/sodewala45/Logistics_Agent", "btn2")
create_agent_card(col3, "Job Hunter", "Autonomous Job Scouting & Match Filtering.", "https://huggingface.co/spaces/sodewala45/Job_Search_Agent", "btn3")
