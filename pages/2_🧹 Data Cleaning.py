import streamlit as st
import pandas as pd

st.title("🧹 Data Cleaning")
st.subheader("Automatically clean your dataset before visualization and AI analysis.")
if "Dataset" in st.session_state:
    cleaned_df = st.session_state["Dataset"].copy()
    
    st.header("📌 Dataset Status")
    rows=cleaned_df.shape[0]
    columns=cleaned_df.shape[1]
    st.write(f"**Rows**:{rows}")
    st.write(f"**Columns**:{columns}")

    st.header("⚠️ Missing Values Before Cleaning")
    missing_df = pd.DataFrame({
    "Column Name": cleaned_df.columns,
    "Missing Values": cleaned_df.isnull().sum().values
     })
    st.dataframe(missing_df,width="stretch")

    st.header("🔁 Duplicate Rows")
    duplicate_rows=cleaned_df.duplicated().sum()
    st.write(f"**Total duplicate rows**:{duplicate_rows}")
    
    st.divider()

    apply_btn = st.button("🧹 Apply Cleaning")
    if apply_btn:
         before_rows = cleaned_df.shape[0]
         before_columns = cleaned_df.shape[1]
         before_missing = cleaned_df.isnull().sum().sum()
         before_duplicates = cleaned_df.duplicated().sum()
         
    
         cleaned_df.drop_duplicates(inplace=True)
         cleaned_df.dropna(how="all", inplace=True)
         cleaned_df.dropna(axis=1, how="all", inplace=True)
         
         for i in cleaned_df.columns:
              if pd.api.types.is_numeric_dtype(cleaned_df[i]):
                   cleaned_df[i].fillna(
                   cleaned_df[i].median(),
                   inplace=True
                   )
              else:
                   cleaned_df[i].fillna(
                   cleaned_df[i].mode()[0],  
                   inplace=True
                   )
         st.session_state["Cleaned_Dataset"] = cleaned_df
         
         after_rows = cleaned_df.shape[0]
         after_columns = cleaned_df.shape[1]
         after_missing = cleaned_df.isnull().sum().sum()
         after_duplicates = cleaned_df.duplicated().sum()
         st.success("✅ Dataset cleaned successfully!")
         st.header("🧹 Cleaning Summary")

         st.write(f"**Rows Before Cleaning:** {before_rows}")
         st.write(f"**Rows After Cleaning:** {after_rows}")

         st.write(f"**Columns Before Cleaning:** {before_columns}")
         st.write(f"**Columns After Cleaning:** {after_columns}")

         st.write(f"**Missing Values Before Cleaning:** {before_missing}")
         st.write(f"**Missing Values After Cleaning:** {after_missing}")

         st.write(f"**Duplicate Rows Before Cleaning:** {before_duplicates}")
         st.write(f"**Duplicate Rows After Cleaning:** {after_duplicates}")
         st.header("👀 Cleaned Dataset Preview")
         st.dataframe(cleaned_df.head(),width="stretch")

else:
    st.info("ℹ️ Please upload a dataset from the 'Upload CSV Dataset' page first.")
