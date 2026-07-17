import streamlit as st

st.set_page_config(page_title="Home",page_icon="🏡",layout="wide")

st.title("📊 **DataInsight AI**")

st.markdown(
    "### AI-Powered Business Analytics Platform"
)
st.divider()
st.info(
    "👋 Welcome to DataInsight AI! Upload your dataset and transform raw data into meaningful insights using interactive visualizations and AI-powered analysis."
)


col1,col2,col3=st.columns(3)

col1.metric(
    label="📂 Supported Formats",
    value="CSV"
)

col2.metric(
    label="⚡ Data Cleaning",
    value="Automatic"
)

col3.metric(
    label="🤖 AI Engine",
    value="Gemini"
)

st.divider()

st.header("Analyze • Visualize • Discover • Decide")

st.caption("Clean your data, uncover insights, and make smarter business decisions.")

st.divider()

st.subheader("🌟 Why Choose DataInsight AI?")
feature_column1,feature_column2,feature_column3,feature_column4=st.columns(4)

with feature_column1:
    with st.container(border=True):
        st.subheader("🧹 Automatic Data Cleaning")
        st.write(
            "Automatically removes duplicate records, fills missing values, and prepares high-quality datasets for analysis."
    )
with feature_column2:
    with st.container(border=True):
        st.subheader("📊 Interactive Visualizations")
        st.write(
            "Generate interactive charts to identify trends, comparisons, and business insights within seconds."
    )
with feature_column3:
    with st.container(border=True):
        st.subheader("🤖 AI Assistant")
        st.write(
            "Ask questions in natural language and receive AI-powered business insights."
    )
with feature_column4:
    with st.container(border=True):
        st.subheader("📄 Report Generation")
        st.write(" Download cleaned datasets and AI-generated reports for sharing and documentation."
    )

st.divider() 

st.subheader("⚡ How It Works")
st.write("Transform your data into actionable insights in five simple steps.")
step1,step2,step3,step4,step5=st.columns(5)

with step1:
    with st.container(border=True):
        st.subheader("①")

        st.markdown("# 📂")

        st.markdown("### Select Data Source")

        st.caption(
            "Upload your business dataset to begin the analysis."
)
        
with step2:
    with st.container(border=True):
        st.subheader("②")

        st.markdown("# 🧹")

        st.markdown("### Automatic Cleaning")

        st.caption(
            "Remove duplicates, handle missing values, and prepare analysis-ready data automatically."
        )

with step3:
    with st.container(border=True):
        st.subheader("③")

        st.markdown("# 📊")

        st.markdown("### Generate Visualizations")

        st.caption(
            "Create interactive charts to discover trends, patterns, and business insights."
        )

with step4:
    with st.container(border=True):
        st.subheader("④")

        st.markdown("# 🤖")

        st.markdown("### AI Business Assistant")

        st.caption(
            "Ask questions in natural language and receive AI-powered business insights."
        )

with step5:
    with st.container(border=True):
        st.subheader("⑤")

        st.markdown("# 📄")

        st.markdown("### Download Reports")

        st.caption(
            "Export cleaned datasets and AI-generated reports for sharing and documentation."
        )

    

st.info("""
🚀 **Get Started** 
           
Click **Data Processing** in the left sidebar to upload, clean, visualize, and analyze your dataset.""")

st.divider()


st.markdown("""
### 📂 Supported Formats

✅ CSV
            
🟡 Excel (.xlsx) - Coming Soon
            
🟡 JSON - Coming Soon 

🟡 TXT  - Coming Soon
""")

st.markdown("---")
st.markdown("### 👨‍💻 Developed by **Shivendra Mahato**")


st.caption(
"Version 1.0 • Powered by Streamlit • Pandas • Plotly • Google Gemini AI"
)


