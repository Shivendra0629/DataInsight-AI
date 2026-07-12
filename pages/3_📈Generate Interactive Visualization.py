import streamlit as st
import pandas as pd 
import plotly.express as px
st.title("📈 Generate Interactive Visualization")
st.subheader("Select a column and chart type to explore your data visually.")

if "Cleaned_Dataset" in st.session_state:
    df= st.session_state["Cleaned_Dataset"]
    st.success("✅ Using the cleaned dataset for visualization.")

elif 'Dataset' in st.session_state:
    df = st.session_state["Dataset"]
    st.warning("⚠️ Dataset has not been cleaned yet. Visualizations are generated using the original uploaded dataset.")
    
else:
    st.info("ℹ️ Please upload a dataset from the 'Upload CSV Dataset' page first.")
    st.stop()
selected_x_column=st.selectbox("📌Select X-axis Column",df.columns.tolist())
selected_y_column=st.selectbox("📌Select Y-axis Column",df.columns.tolist())
chart_list=['Bar Plot','Box Plot','Histogram Plot','Pie Plot']
selected_chart=st.selectbox("Select a chart to visualize",chart_list)
btn=st.button("📊 Generate Visualization")
if btn:
    if selected_x_column == selected_y_column:
        st.error("❌ X-axis and Y-axis columns cannot be the same. Please select different columns.")
    elif selected_chart=="Bar Plot":
        fig=px.bar(
                    df,
                    x=selected_x_column,
                    y=selected_y_column
                    )
        st.plotly_chart(fig,width="stretch")
    elif selected_chart=='Box Plot':
        fig=px.box(
                   df,
                   x=selected_x_column,
                   y=selected_y_column
                   )
        st.plotly_chart(fig,width="stretch")
    elif selected_chart=='Histogram Plot':
        if pd.api.types.is_numeric_dtype(df[selected_x_column]):
                fig=px.histogram(
                   df,
                   x=selected_x_column
                   )
                st.plotly_chart(fig,width="stretch")
        else:
                st.warning("⚠️ Please select a numeric column (int or float) for the X-axis to generate a Histogram Chart.")
    elif selected_chart=='Pie Plot':
        if df[selected_x_column].nunique()>20: 
                   st.warning("⚠️ Pie charts work best with 20 or fewer unique categories.")
        elif pd.api.types.is_numeric_dtype(df[selected_y_column]):
            fig=px.pie(
                    df,
                    names=selected_x_column,
                    values=selected_y_column
                    )
            st.plotly_chart(fig,width="stretch")
        else:
            st.warning("⚠️ Please select a numeric column (int or float) for the Y-axis to generate a Pie Chart.")
