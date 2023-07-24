from connection import KaggleDatasetConnection
import streamlit as st


st.set_page_config(page_title="Kaggle-Streamlit Connection Demo App")

st.image('https://i.postimg.cc/PfVwHZ2Z/kaggle-streamlit-header.png', width=500)

st.title("Kaggle-Streamlit Connector App")

st.info('This is a demo app that presents basic use of custom Kaggle-Streamlit connector built using ExperimentalBaseConnection')

"""
[Kaggle](https://www.kaggle.com/) is the world's largest data science community. It enables users to explore and analyze a wide variety of public datasets.
This app demonstrates a simple `KaggleDatasetConnection` which was built by extending the 
[built-in ExperimentalBaseConnection](https://docs.streamlit.io/library/api-reference/connections/st.connections.experimentalbaseconnection)
You can view the connection source code
[here](https://github.com/arsentievalex/kaggle-streamlit-data-connector/blob/main/connection.py).
"""

st.info('While Kaggle offers datasets in different formats, this connector ONLY supports datasets with a single CSV file.')

"""
A user can connect to a Kaggle dataset by providing the dataset path. 
The path is the part of the dataset URL after the domain name, the structure is following: username/dataset-name.
For example, for the dataset https://www.kaggle.com/shivamb/netflix-shows, the path is `shivamb/netflix-shows`.
"""

"""Using this example, the code to connect to the dataset would look like this:"""

code = """
from connection import KaggleDatasetConnection
import streamlit as st

conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection)
df = conn.get(path='shivamb/netflix-shows', ttl=3600)
"""

secrets = """
 [connections.kaggle_datasets]
 KAGGLE_USERNAME = "insert your Kaggle username"
 KAGGLE_KEY = "insert your Kaggle API key"
"""

st.code(code, language='python')

"""`KaggleDatasetConnection` class assumes that you have secrets set up in the following format:"""

st.code(secrets, language='toml')

st.subheader("Loading Netflix Movies and TV Shows dataset")
# load data
conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection)
df = conn.get(path='shivamb/netflix-shows', ttl=3600)

st.write('The dataset has {} rows and {} columns'.format(df.shape[0], df.shape[1]))

st.write('The columns are: {}'.format(', '.join(df.columns)))
st.write('Data Preview:')
st.dataframe(df.head(20))




