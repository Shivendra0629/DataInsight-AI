import streamlit as st 

st.title("⬇️ Download Report")
st.subheader("Download your cleaned dataset and AI-generated insights.")

if "Cleaned_Dataset" in st.session_state:
    st.success("✅ Cleaned dataset is ready for download.")
    cleaned_df = st.session_state["Cleaned_Dataset"]

    csv = cleaned_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download Cleaned Dataset (CSV)",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv"
)

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
    AI Business Insights
    --------------------

    {ai_report}

    =============================
    Generated using DataInsight AI
    =============================
    """
    report_bytes = report.encode("utf-8")
    st.download_button(
        label="⬇️ Download AI Insights Report",
        data=report_bytes,
        file_name="AI_Business_Report.txt",
        mime="text/plain"
)

if "Cleaned_Dataset" not in st.session_state and "AI_Insights" not in st.session_state:
    st.info("ℹ️ Nothing is available to download yet.")
