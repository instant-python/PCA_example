import streamlit as st
import pandas as pd
import plotly.express as px
from pca import pca_run

st.set_page_config(page_title='PCA Example', layout='wide')

################## Header Section ##################
with st.container():
    st.title('PCA Example')
    st.write('Sample PCA analysis using your dataset')
################## Header Section ##################

################## Main Section ##################
with st.container():
    st.write('---')
    # 2 columns
    col1, empty_col, col2 = st.columns([0.4,0.1,1])

    # left column with a data uploader
    with col1:
        input_data = st.file_uploader('Choose your file')
    
    # run PCA
    if input_data is None:
        with col2:
            st.header('Please upload a file!')
    else:
        input_df = pd.read_csv(input_data)
        pca_data, cat_data_list, pca_cols = pca_run(input_df)
        
        with col1:
            # PCA selection box
            pca1 = st.selectbox('First Principle Component',options=pca_cols,index=0)
            pca_cols.remove(pca1)
            pca2 = st.selectbox('Second Principle Component',options=pca_cols,index=0)
            # Category name selection box
            color_category = st.selectbox('Select category legened',options=cat_data_list, index=0)
        
        with col2:
            scatter_chart = px.scatter(data_frame=pca_data, x=pca1, y=pca2, color=color_category, height=500)
            st.plotly_chart(scatter_chart, use_container_width=True)

################## Main Section ##################