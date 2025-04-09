import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Analysis and Visualization App")
st.write(""" 
This app allows users to:
- Upload a dataset
- View basic statistics
- Visualize data features
""")

file_upload = st.file_uploader('Choose a CSV file', type='csv')

if file_upload is not None:
    data = pd.read_csv(file_upload)

    st.write('### Data Preview')
    st.write(data.head())

    st.write('### Data Statistics')
    st.write(data.describe())

    st.write('### Data Visualization')
    column = st.selectbox('Select a column to visualize', data.columns)

    if data[column].dtype != 'object':  # fixed typo 'onject'
        st.write(f'#### Histogram of column `{column}`')
        plt.figure(figsize=(10, 5))
        sns.histplot(data[column], kde=True)
        st.pyplot(plt)

        st.write('#### Scatter Plot')
        x_column = st.selectbox('Select x-axis for scatter plot', data.columns)
        y_column = st.selectbox('Select y-axis for scatter plot', data.columns)
        plt.figure(figsize=(10, 5))
        sns.scatterplot(data=data, x=x_column, y=y_column)
        st.pyplot(plt)
    else:
        st.warning(f"The selected column `{column}` is not numeric. Please choose a numeric column for histogram or scatter plot.")
