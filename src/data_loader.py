import pandas as pd
from pathlib import Path


def load_telco_dataset():
    data_path = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return pd.read_csv(data_path)
    



# import kagglehub
# from kagglehub import KaggleDatasetAdapter

    # file_path = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    # df = kagglehub.load_dataset(
    #     KaggleDatasetAdapter.PANDAS,
    #     "blastchar/telco-customer-churn",
    #     file_path
    # ) 
    # return df     # just for testing api