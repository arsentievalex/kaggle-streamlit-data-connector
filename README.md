[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://kaggle-data-connector.streamlit.app/)

# Kaggle-Streamlit Data Connector
Basic Kaggle-Streamlit connector for CSV files. Built using ExperimentalBaseConnection.

Usage:
```python
from connection import KaggleDatasetConnection
import streamlit as st

conn = st.experimental_connection("kaggle_datasets", type=KaggleDatasetConnection, path='shivamb/netflix-shows')
df = conn.get(ttl=3600)
```
