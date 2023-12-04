[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://kaggle-data-connector.streamlit.app/)

# Kaggle-Streamlit Data Connector
Basic Kaggle-Streamlit connector for CSV files. Built using ExperimentalBaseConnection.

Usage:
```python
from st_kaggle_connector import KaggleDatasetConnection
import streamlit as st

conn = st.connection("kaggle_datasets", type=KaggleDatasetConnection)
df = conn.get(path='shivamb/netflix-shows', filename='netflix_titles.csv', ttl=3600)
```
