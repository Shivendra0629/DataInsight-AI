import streamlit as st
import pandas as pd
from google import genai
from datetime import datetime

st.title("🧠 Get AI-Powered Business Insights")
st.subheader("Ask questions about your dataset and receive AI-generated insights.")
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

if "Cleaned_Dataset" in st.session_state:
    df=st.session_state["Cleaned_Dataset"]
    st.info(
    f"📊 Dataset Loaded: **{df.shape[0]} rows × {df.shape[1]} columns**"
)
    st.success("✅ Using the cleaned dataset for AI-powered insights.")
elif "Dataset" in st.session_state:
    df=st.session_state["Dataset"]
    st.warning("⚠️ Dataset has not been cleaned yet. AI insights will be generated using the original uploaded dataset.")
    
else:
    st.info("ℹ️ Please upload a dataset from the 'Upload CSV Dataset' page first.")
    st.stop()


st.header("💬 Ask Your Question")
st.caption("💡 Example questions you can ask:")

st.markdown("""
- Which category has the highest sales?
- What trends do you observe in the dataset?
- Which products are underperforming?
- Are there any anomalies or outliers?
- What business recommendations would you make?
""")
user_question = st.text_area(
    "Enter your question",
    height=150,
    placeholder="Example: Which products generate the highest revenue and what should the company focus on?"
)

btn=st.button("🧠 Generate AI Insights",use_container_width=True,
    disabled=not user_question.strip())

if btn:
   if  user_question.strip() =="":
    st.warning("⚠️ Please enter a question before generating AI insights.")
   else:
      prompt = f"""
      You are an expert Business Data Analyst.
      Dataset Shape:
      Rows: {df.shape[0]}
      Columns: {df.shape[1]}

      Dataset Columns:
      {df.columns.tolist()}
      
      Dataset Statistics:
      {df.describe(include="all").to_string()}

      Dataset Sample:
      {df.head(5).to_string()}

      
      User Question:
      {user_question}

      Provide:
      1. A direct answer to the user's question.
      2. Important patterns or trends found.
      3. Business insights.
      4. Actionable recommendations.
      5. Mention any limitations if only the sample data is available.
      Keep the response well-structured using Markdown headings and bullet points.
      Do not make assumptions that are not supported by the dataset.
      If information is unavailable, clearly say so instead of guessing.
      """
      
     
      
      
      try:
        with st.spinner("🤖 AI is analyzing your dataset..."):
         response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
            )
        st.success("✅ AI Insights Generated Successfully")
        st.session_state["AI_Insights"] = response.text
        st.session_state["User_Question"] = user_question
        st.divider()
        st.header("📊 AI Business Insights")
        with st.container(border=True):
            st.markdown(response.text)

      except Exception as e:
        st.error(f"❌ Error: {e}")

st.divider()
st.header("⬇️ Download Report")


if "AI_Insights" in st.session_state:
    st.success("✅ AI report is ready for download.")
    ai_report = st.session_state["AI_Insights"]
    if "Cleaned_Dataset" in st.session_state:
        report_df = st.session_state["Cleaned_Dataset"]
    else:
        report_df = st.session_state["Dataset"]

    report = f"""
    =============================
    AI BUSINESS REPORT
    =============================

    Dataset Summary
    ---------------
    Rows    : {report_df.shape[0]}
    Columns : {report_df.shape[1]}
    
    User Question
    -------------
    {st.session_state["User_Question"]}
    
    AI Business Insights
    --------------------
    {ai_report}

    Generated On
    ------------
    {datetime.now().strftime("%d-%m-%Y %H:%M")}
    =============================
    Generated using DataInsight AI
    =============================
    """
    st.caption(
    f"Report Length: {len(ai_report.split())} words"
)
    report_bytes = report.encode("utf-8")
    st.download_button(
        label="⬇️ Download AI Insights Report",
        data=report_bytes,
        file_name="DataInsight_AI_Report.txt",
        mime="text/plain"
)

if "Cleaned_Dataset" not in st.session_state and "AI_Insights" not in st.session_state:
    st.info("ℹ️ Nothing is available to download yet.")
