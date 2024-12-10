import os
import sqlite3
import pandas as pd

def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def load_data_from_sources(conn, df, table_name):
    """ load data from dataframe and insert into the database """
    try:
        df.to_sql(table_name, conn, if_exists='append', index=False)
        print(f"Data loaded successfully into {table_name}")
    except Exception as e:
        print(e)

def create_table_from_dataframe(conn, df, table_name):
    """ create a table based on the dataframe schema """
    try:
        columns = ', '.join([f"{col} {dtype}" for col, dtype in zip(df.columns, df.dtypes.replace({'int64': 'INTEGER', 'float64': 'REAL', 'object': 'TEXT'}))])
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});"
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print(f"Table created successfully: {table_name}")
    except sqlite3.Error as e:
        print(e)

def load_sets_data(conn):
    # Load the sets data from lorecast_api datasource
    lorecast_api_df = pd.read_csv('data/raw/lorcast_api/sets.csv')

    # Add the datasource_name column
    lorecast_api_df['datasource_name'] = 'lorecast_api'

    # Create table based on dataframe schema
    create_table_from_dataframe(conn, lorecast_api_df, 'master_sets')

    # Load data into the table
    load_data_from_sources(conn, lorecast_api_df, 'master_sets')

def load_cards_data(conn):
    # Load data for each individual CSV for the Disney Lorcana datasource

    try:
        # Load data from Disney Lorcana CSV files
        print("Loading data from Disney Lorcana CSV files")
        disney_lorcana_dir = "data/processed/disney_lorcana"
        csv_files = [f"{disney_lorcana_dir}/{f}" for f in os.listdir(disney_lorcana_dir) if f.endswith('.csv')]
        num_of_files = len(csv_files)
        print(f"Found {num_of_files} CSV files in {disney_lorcana_dir}")

        # Load data from each CSV file
        for csv_file in csv_files:
            print(f"Loading data from {csv_file}")

            # Load data from CSV file
            disney_lorcana_df = pd.read_csv(csv_file)

            # Add a column for the datasource name
            disney_lorcana_df["datasource_name"] = "disney_lorcana"

            # Rename the card_name column to name
            disney_lorcana_df.rename(
                columns={
                    "card_id": "id",
                    "card_name": "name",
                }, 
                inplace=True
            )

        # Load data from Lorcast API CSV files
        lorcast_api_dir = "data/raw/lorcast_api"
        csv_files = [f"{lorcast_api_dir}/{f}" for f in os.listdir(lorcast_api_dir) if f.endswith('.csv')]
        num_of_files = len(csv_files)
        print(f"Found {num_of_files} CSV files in {lorcast_api_dir}")
        
        # Load data from each CSV file
        for csv_file in csv_files:
            print(f"Loading data from {csv_file}")

            # Load data from CSV file
            lorcast_api_df = pd.read_csv(csv_file)

            # Add a column for the datasource name
            lorcast_api_df["datasource_name"] = "lorcast_api"

        # Combine dataframes if needed
        combined_df = pd.concat([
            disney_lorcana_df, 
            lorcast_api_df
        ], ignore_index=True)

        # Create table based on dataframe schema
        create_table_from_dataframe(conn, combined_df, 'master_cards')

        # # Load data into the table
        # load_data_from_sources(conn, combined_df, 'master_cards')
        
    except sqlite3.Error as e:
        print(e)
    except FileNotFoundError as e:
        print(e)

def main():
    database = "data/processed/disney_lorcana.db"

    # create a database connection
    conn = create_connection(database)

    # create table
    if conn is not None:
        load_sets_data(conn)
        load_cards_data(conn)
    else:
        print("Error! cannot create the database connection.")

    if conn:
        conn.close()

if __name__ == '__main__':
    main()