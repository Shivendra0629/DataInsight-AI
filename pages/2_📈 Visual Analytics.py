import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff

color_map = {
    "Default": px.colors.qualitative.Plotly,
    "Plotly": px.colors.qualitative.Plotly,
    "Dark": px.colors.qualitative.Dark24,
    "Light": px.colors.qualitative.Pastel                       # Colour Pallete --> px.colors.qualitative
}

st.title("📈 Generate Interactive Visualization")
st.subheader("Select a column and chart type to explore your data visually.")

if "Cleaned_Dataset" in st.session_state:
    df= st.session_state["Cleaned_Dataset"]
    st.success("✅ Using the cleaned dataset for visualization.")
    st.divider()
    st.subheader("📊 Dataset Overview")
    missing=df.isnull().sum().sum()
    duplicate=df.duplicated().sum()
    
    rows_1,col_1,missing_1,duplicates_1=st.columns(4)

    
    rows_1.metric( 
         label="Rows",
         value=df.shape[0]
    )
    col_1.metric(
         label="Columns",
         value=df.shape[1]
    )
    missing_1.metric(
         label="Missing",
         value=missing
    )
    duplicates_1.metric(
         label="Duplicates",
         value=duplicate
    )
    
else:
    st.info("ℹ️ Please upload a dataset from the 'Upload CSV Dataset' page first.")
    st.stop()
st.divider()
st.subheader("⚙️ Chart Configuration")

select_feature,chart_feature=st.columns([2,1])

with select_feature:
     with st.container(border=True):

        st.subheader("📌 Axis Selection")
        selected_x_column=st.selectbox("📌Select X-axis Column",df.columns.tolist())
        selected_y_column=st.selectbox("📌Select Y-axis Column",df.columns.tolist())

with chart_feature:
        with st.container(border=True):
             st.subheader("📊 Chart Type")
             chart_list =[ "📊 Bar Plot", 
                          "📦 Box Plot",
                          "📈 Histogram",
                          "🥧 Pie Chart",
                          "🔵 Scatter Plot",
                          "🔥 Correlation Heatmap"
                          ]
             selected_chart=st.selectbox("Choose Visualization",chart_list)
           

st.divider()
st.subheader("🎨 Chart Customization")
st.caption("Personalize your visualization before generating it.")
    
customization_1, customization_2, customization_3 = st.columns(3)
with customization_1:
    with st.container(border=True):
        st.subheader("📝 Chart Title")
        chart_title = st.text_input(
                   "Enter Chart Title",
                   placeholder="e.g. Sales by Region")
              
with customization_2:
    with st.container(border=True):
        st.subheader("🎨 Color Theme")
        color_theme = st.selectbox( "Choose Theme",
            ["Default", "Plotly", "Dark", "Light"] )
              
with customization_3:
    with st.container(border=True):
        st.subheader("📐 Chart Height")
        chart_height = st.slider("Chart Height",min_value=400,max_value=900,value=600,step=50 )
        

with st.container(border=True):
    st.subheader("🚀 Ready to Generate")
    st.caption("Click below to create the chart.")
    btn=st.button("📊 Generate Visualization",use_container_width=True)

st.divider()

if btn:
    
    final_title = chart_title if chart_title else selected_chart
    st.subheader(f"📈 {final_title}")
    if selected_x_column == selected_y_column:
        st.error("❌ X-axis and Y-axis columns cannot be the same. Please select different columns.")
    
    elif selected_chart=="📊 Bar Plot":
        fig=px.bar(
                    df,
                    x=selected_x_column,
                    y=selected_y_column,
                    color_discrete_sequence=color_map[color_theme]
                    )
        fig.update_layout(
            title=final_title,
            height=chart_height
        )
        st.success("✅ Visualization generated successfully.")
        st.plotly_chart(fig,width="stretch")
        
    elif selected_chart=='📦 Box Plot':
        
        fig=px.box(
                   df,
                   x=selected_x_column,
                   y=selected_y_column,
                   color_discrete_sequence=color_map[color_theme]
                   )
        fig.update_layout(
            title=final_title,
            height=chart_height
        )
        st.success("✅ Visualization generated successfully.")
        st.plotly_chart(fig,width="stretch")

    elif selected_chart=='📈 Histogram':
        
        if pd.api.types.is_numeric_dtype(df[selected_x_column]):
                fig=px.histogram(
                   df,
                   x=selected_x_column,
                   color_discrete_sequence=color_map[color_theme]
                   )
                fig.update_layout(
                     title=final_title,
                     height=chart_height
                 )
                st.success("✅ Visualization generated successfully.")
                st.plotly_chart(fig,width="stretch")
        else:
                st.warning("⚠️ Please select a numeric column (int or float) for the X-axis to generate a Histogram Chart.")
    
    elif selected_chart=='🥧 Pie Chart':
        
        if df[selected_x_column].nunique()>20: 
                   st.warning("⚠️ Pie charts work best with 20 or fewer unique categories.")
        elif pd.api.types.is_numeric_dtype(df[selected_y_column]):
            fig=px.pie(
                    df,
                    names=selected_x_column,
                    values=selected_y_column,
                    color_discrete_sequence=color_map[color_theme]
                    )
            fig.update_layout(
                 title=final_title,
                 height=chart_height
                 )
            st.success("✅ Visualization generated successfully.")
            st.plotly_chart(fig,width="stretch")
        else:
            st.warning("⚠️ Please select a numeric column (int or float) for the Y-axis to generate a Pie Chart.")

    elif selected_chart == "🔵 Scatter Plot":
        
        if (
        pd.api.types.is_numeric_dtype(df[selected_x_column]) and
        pd.api.types.is_numeric_dtype(df[selected_y_column]) ):
            fig = px.scatter(
                  df,
                  x=selected_x_column,
                  y=selected_y_column,
                  color_discrete_sequence=color_map[color_theme]
                  )
             
            fig.update_layout(
            title=final_title,
            height=chart_height
            )
            st.success("✅ Visualization generated successfully.")
            st.plotly_chart(fig, width="stretch")

        else:
             st.warning("⚠️ Scatter Plot requires numeric columns for both X-axis and Y-axis.")

    elif selected_chart == "🔥 Correlation Heatmap":
        
        numeric_df = df.select_dtypes(include="number")
        if numeric_df.shape[1] < 2:
             st.warning(
            "⚠️ Correlation Heatmap requires at least two numeric columns."
        )
        else:
            correlation = numeric_df.corr()
            fig = ff.create_annotated_heatmap(
                 z=correlation.values,
                 x=list(correlation.columns),
                 y=list(correlation.index),
                 annotation_text=correlation.round(2).values,
                 colorscale="Viridis",
                 showscale=True
                 )
            fig.update_layout(
                title=final_title,
                height=chart_height
            )
            st.success("✅ Visualization generated successfully.")
            st.plotly_chart(fig, width="stretch")


