import os
import pandas as pd
from sqlalchemy import create_engine
from global_variables import *

# # create engine sql data base
# engine = create_engine('mssql+pyodbc://DESKTOP-HTQ5LV8/data_base?driver=ODBC+Driver+18+for+SQL+Server&Trusted_Connection=yes&TrustServerCertificate=True')

# # listing csv files in the folder
# files_csv = [file for file in os.listdir(CSV_FILES_FILEPATH) if file.endswith('_converted.csv')]

# # adding every file to sql data base
# for file_csv in files_csv:
#     filepath_to_file = os.path.join(CSV_FILES_FILEPATH, file_csv)
#     df = pd.read_csv(filepath_to_file)

#     # create table name by remove '_converted.csv' from file name
#     table_name = file_csv.replace('_converted', '')

#     # save data frame to table in data base
#     df.to_sql(table_name, con=engine, if_exists='replace', index=False)

#     print(f'Tabela {table_name} została pomyślnie utworzona w bazie danych.')

try:
    # create engine sql data base
    engine = create_engine('mssql+pyodbc://DESKTOP-HTQ5LV8/data_base?driver=ODBC+Driver+18+for+SQL+Server&Trusted_Connection=yes&TrustServerCertificate=True')
    print("Połączenie z bazą danych zostało nawiązane.")

    # listing csv files in the folder
    files_csv = [file for file in os.listdir(CSV_FILES_FILEPATH) if file.endswith('_converted.csv')]
    print(f"Zawartość folderu: {os.listdir(CSV_FILES_FILEPATH)}")
    print(f"Znaleziono {len(files_csv)} plików do przetworzenia.")

    # adding every file to sql data base
    for file_csv in files_csv:
        print(f"Przetwarzanie pliku: {file_csv}")
        filepath_to_file = os.path.join(CSV_FILES_FILEPATH, file_csv)
        df = pd.read_csv(filepath_to_file)

        # create table name by removing '_converted.csv' from file name
        table_name = file_csv.replace('_converted.csv', '')
        print(f"Tworzenie tabeli: {table_name}")

        # save data frame to table in data base
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)

        print(f"Tabela {table_name} została pomyślnie utworzona w bazie danych.")

except Exception as e:
    print(f"Wystąpił błąd: {e}")