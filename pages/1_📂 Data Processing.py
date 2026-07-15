import streamlit as st 
import pandas as pd 

st.title("📂 Dataset Preprocessing")
st.subheader("Upload your CSV dataset,get the summary and download the clean file.")


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
    st.write(f"**Rows**:{df.shape[0]}")
    st.write(f"**Columns**:{df.shape[1]}")

    st.header("📋 Column Names")
    column_df = pd.DataFrame({
        "Column Name": df.columns
     })
    st.dataframe(column_df,use_container_width=True)
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
    st.divider()

else:
    st.info("ℹ️ Please upload a CSV file to begin analysis.")


if "Dataset" in st.session_state:
    cleaned_df = st.session_state["Dataset"].copy()
    st.header("🤖 Automatic Data Cleaning")
    with st.spinner("Cleaning your dataset..."):
        before_rows = cleaned_df.shape[0]
        before_columns = cleaned_df.shape[1]
        before_missing = cleaned_df.isnull().sum().sum()
        before_duplicates = cleaned_df.duplicated().sum()
        
        cleaned_df.drop_duplicates(inplace=True)
        cleaned_df.dropna(how="all", inplace=True)
        cleaned_df.dropna(axis=1, how="all", inplace=True)
        for i in cleaned_df.columns:
            if pd.api.types.is_numeric_dtype(cleaned_df[i]):
                cleaned_df=cleaned_df[i].fillna(cleaned_df[i].median())
            else:
                cleaned_df=cleaned_df[i].fillna(cleaned_df[i].mode()[0])
    
    st.session_state["Cleaned_Dataset"] = cleaned_df
    st.success("✅ Dataset cleaned successfully!")
    st.divider()

if "Cleaned_Dataset" in st.session_state:
    st.success("✅ Cleaned dataset is ready to download.")
    cleaned_df = st.session_state["Cleaned_Dataset"]
    
    csv = cleaned_df.to_csv(index=False).encode("utf-8")
    st.download_button(
            label="⬇️ Download Cleaned Dataset (CSV)",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
            )
         
    after_rows = cleaned_df.shape[0]
    after_columns = cleaned_df.shape[1]
    after_missing = cleaned_df.isnull().sum().sum()
    after_duplicates = cleaned_df.duplicated().sum()

    
    st.header("👀 Cleaned Dataset Preview")
    st.dataframe(cleaned_df.head(10),use_container_width=True)

    st.header("📋 Cleaning Summary")
    st.write(f"✔ Rows Before Cleaning: {before_rows}")
    st.write(f"✔ Rows After Cleaning: {after_rows}")

    st.write(f"✔ Columns Before Cleaning: {before_columns}")
    st.write(f"✔ Columns After Cleaning: {after_columns}")

    st.write(f"✔ Missing Values Filled : {before_missing-after_missing}")
    
    st.write(f"✔ Duplicate Rows Removed : {before_duplicates-after_duplicates}")

    
         




