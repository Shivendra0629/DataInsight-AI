import streamlit as st

st.set_page_config(page_title="Home",page_icon="🏡",layout="wide")

st.title("📊 **DataInsight-AI**")
st.markdown(
    "### Transform your CSV data into meaningful business insights with AI-powered analytics."
)

st.info(
    "👋 Welcome to DataInsight AI! Upload your business dataset and uncover valuable insights using interactive visualizations and AI-powered analysis."
)
st.header("Analyze • Visualize • Discover • Decide")
st.subheader("🌟 Why DataInsight AI?")

st.success("""
✔ No coding required

✔ Interactive visualizations

✔ AI-powered business insights

✔ Automated data cleaning

✔ Professional downloadable reports
""")

st.divider() 
st.success("🚀 Get started by selecting **Dataset Explorer** from the left sidebar.")

st.subheader("🚀 Key Features")

st.markdown("""
1. 📂 Upload your CSV dataset
2. 🧹 Clean and prepare your data
3. 📈 Create interactive visualizations
4. 🧠 Ask AI questions about your data
5. ⬇️ Download your cleaned dataset and AI report
""")
st.divider()
st.markdown("👨‍💻 Developed by Shivendra Mahato")

st.caption("• Powered by Streamlit • Google Gemini AI • Plotly • Pandas")