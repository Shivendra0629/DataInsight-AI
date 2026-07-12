import streamlit as st 
import pandas as pd 

st.title("📂 Dataset Upload & Explorer")
st.subheader("Upload your CSV dataset and explore its structure before cleaning and analysis.")



uploaded_file =st.file_uploader("Choose your CSV file",type=["csv"])

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.session_state["Dataset"]=df
    st.success("✅ File uploaded successfully")
    st.divider()

    st.header("👀 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)
    st.divider()

    st.header("📌 Dataset Shape")
    rows=df.shape[0]
    columns=df.shape[1]
    st.write(f"**Rows**:{rows}")
    st.write(f"**Columns**:{columns}")

    st.header("📋 Column Names")
    column_df = pd.DataFrame({
        "Column Name": df.columns
     })
    st.dataframe(column_df, use_container_width=True)
    st.divider()

    st.header("🏷️ Data Types")
    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })
    st.dataframe(dtype_df,use_container_width=True)
    st.divider()

    st.header("⚠️ Missing Values")
    missing_df = pd.DataFrame({
        "Column Name": df.columns,
        "Missing Values": df.isnull().sum().values
    })
    st.dataframe(missing_df, use_container_width=True)
    st.divider()

    st.header("🔁 Duplicate Rows")
    duplicate_rows=df.duplicated().sum()
    st.write(f"**Total duplicate rows**:{duplicate_rows}")

else:
    st.info("ℹ️ Please upload a CSV file to begin analysis.")





