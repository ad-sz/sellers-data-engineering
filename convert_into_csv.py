import pandas as pd
import csv
import json
import os
from global_variables import *


# create new csv files for all files with data
# os.makedirs(os.path.dirname(CUSTOMERS_CSV_FILEATH_NEW), exist_ok=True)
# os.makedirs(os.path.dirname(INVENTORY_STATUS_CSV_FILEATH_NEW), exist_ok=True)
# os.makedirs(os.path.dirname(PRODUCTS_CSV_FILEATH_NEW), exist_ok=True)
# os.makedirs(os.path.dirname(SALES_TRANSACTIONS_JSON_FILEATH_NEW), exist_ok=True)
# os.makedirs(os.path.dirname(SELLERS_CSV_FILEATH_NEW), exist_ok=True)



# data = pd.read_json(sales_transactions_json_fileath)

# # Zapisanie do pliku CSV, używając średnika jako separatora
# data.to_csv(sales_transactions_csv_fileath, sep=';', index=False)

"""function for ceate new customers csv file with standart layout"""
def customers_csv_processed(CUSTOMERS_CSV_FILEATH_OLD, CUSTOMERS_CSV_FILEATH_NEW, SELLERS_CSV_FILEATH_OLD):
    # create data frame from customer csv file
    data_frame_customers_csv = pd.read_csv(CUSTOMERS_CSV_FILEATH_OLD)
    # change columns names in customer data frame file
    data_frame_customers_csv.columns = ['id_customer', 'name_customer', 'date_added_customer', 'region']

    # create data frame with 2 collumns from sellers csv file
    data_frame_sellers_csv = pd.read_csv(SELLERS_CSV_FILEATH_OLD[['ID', 'Responsible for Region']])
    # change columns names in sellers data frame file
    data_frame_sellers_csv.columns = ['id_seller', 'region']

    # connection two data frames by region, adding responsible seller for the customer
    data_frame_customers_csv = pd.merge(data_frame_customers_csv, data_frame_sellers_csv, on='region', how='left')

    # change all letters for small
    data_frame_customers_csv = data_frame_customers_csv.applymap(lambda x: x.lower if type(x) == str else x)
