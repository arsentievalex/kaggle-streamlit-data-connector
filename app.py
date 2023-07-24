from connection import KaggleDatasetConnection
import streamlit as st

st.set_page_config(page_title="Kaggle-Streamlit Connection Demo App")

st.title("Kaggle-Streamlit Connection Demo App")

# load data
conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection, path='shivamb/netflix-shows')
df = conn.get(zip_file_name='netflix-shows.zip')

st.write('The dataset has {} rows and {} columns'.format(df.shape[0], df.shape[1]))

st.write('The columns are: {}'.format(', '.join(df.columns)))

st.dataframe(df.head())

