import streamlit as st
import os

# 1. ANALYTICS LOGIC: Tracking Clicks
# In a real production environment, you'd use a database. 
# Here, we'll simulate the dashboard view for you.

if 'analytics' not in st.session_state:
    st.session_state.analytics = {
        "TikTok Agent": 12,    # Mock data to start
        "Logistics Agent": 8,
        "Job Hunter": 25
    }

def track_click(agent_name):
    st.session_state.analytics[agent_name] += 1
    # Optimization: You can send this data to a Google Sheet via API later!
    st.toast(f"Metric Updated: {agent_name} click tracked!")

# 2. THE DASHBOARD VIEW (Only visible to you)
with st.expander("📊 Recruiter Insights (Admin View)"):
    st.write("See which projects are attracting the most attention:")
    
    # Create a nice bar chart of your traffic
    chart_data = pd.DataFrame({
        'Agent': list(st.session_state.analytics.keys()),
        'Clicks': list(st.session_state.analytics.values())
    })
    st.bar_chart(chart_data.set_index('Agent'))

# 3. UPDATED BUTTONS
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Launch TikTok Agent"):
        track_click("TikTok Agent")
        st.js_code("window.open('https://huggingface.co/spaces/your-username/TikTok_Agent')")

with col2:
    if st.button("Launch Logistics Agent"):
        track_click("Logistics Agent")
        st.js_code("window.open('https://huggingface.co/spaces/your-username/Logistics_Agent')")

with col3:
    if st.button("Launch Job Hunter"):
        track_click("Job Hunter")
        st.js_code("window.open('https://huggingface.co/spaces/your-username/Job_Search_Agent')")
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
