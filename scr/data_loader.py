import kagglehub
from kagglehub import KaggleDatasetAdapter

# File name inside dataset
file_path = "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Load dataset
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "blastchar/telco-customer-churn",
    file_path
)

print("Shape:", df.shape)

print("First 5 records:", df.head())

# def load_telco_dataset():
#     file_path = "WA_Fn-UseC_-Telco-Customer-Churn.csv"

#     df = kagglehub.load_dataset(
#         KaggleDatasetAdapter.PANDAS,
#         "blastchar/telco-customer-churn",
#         file_path
#     )

#     return df