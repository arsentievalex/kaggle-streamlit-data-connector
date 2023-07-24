from streamlit.connections import ExperimentalBaseConnection
import os
import pandas as pd
import zipfile
import streamlit as st


class KaggleDatasetConnection(ExperimentalBaseConnection):

    def _connect(self):
        # Set Kaggle credentials
        os.environ['KAGGLE_USERNAME'] = self._secrets.KAGGLE_USERNAME
        os.environ['KAGGLE_KEY'] = self._secrets.KAGGLE_KEY

        # importing here because it requires the credentials to be set
        from kaggle.api.kaggle_api_extended import KaggleApi

        # Initialize Kaggle API connection
        self.conn = KaggleApi()

    def get(self, path, ttl):
        @st.cache_data(ttl=ttl)
        def _get(path=path):
            # Authenticate to Kaggle
            self.conn.authenticate()
            # Download zip file
            self.conn.dataset_download_files(path)
            # get filename from path
            file_name = path.split('/')[-1] + ".zip"
            # Dataset is downloaded as a zip, so we need to extract it
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall('.')

            # Assuming there's a single CSV file in the dataset, we can load it into a DataFrame
            csv_file = [file for file in os.listdir('.') if file.endswith('.csv')][0]
            df = pd.read_csv(csv_file)
            return df
        return _get(path)





