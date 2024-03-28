import pandas as pd
import csv
import json
import os

sales_transactions_json_fileath = 'D:/python_data/projekt/products_management/sellers-data-engineering/data/sales_transactions.json'

sales_transactions_csv_fileath = 'D:/python_data/projekt/products_management/sellers-data-engineering/data/sales_transactions_csv.csv'

os.makedirs(os.path.dirname(sales_transactions_csv_fileath), exist_ok=True)

data = pd.read_json(sales_transactions_json_fileath)

# Zapisanie do pliku CSV, używając średnika jako separatora
data.to_csv(sales_transactions_csv_fileath, sep=';', index=False)