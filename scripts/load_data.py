import csv
import os
import pandas as pd
import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def load_cards_data(conn):
    """ load data from a CSV file into the database """

    # Load data for each individual CSV for the Disney Lorcana datasource
    try:
        print("Loading data from Disney Lorcana CSV files")
        
        # Get a list of CSV files from the data/processed/disney_lorcana dir
        disney_lorcana_dir = "data/processed/disney_lorcana"
        datasource_name = "disney_lorcana"
        csv_files = [f"{disney_lorcana_dir}/{f}" for f in os.listdir(disney_lorcana_dir) if f.endswith('.csv')]
        num_files = len(csv_files)
        print(f"Found {num_files} CSV files in {disney_lorcana_dir}")

        # Load data from each CSV file
        for csv_file in csv_files:
            print(f"Loading data from {csv_file}")
            df = pd.read_csv(csv_file)
            # Add a column for the datasource name
            df['datasource_name'] = datasource_name
            df.rename(columns={'card_name': 'name'}, inplace=True)
            df[['name', 'datasource_name']].to_sql('cards', conn, if_exists='append', index=False)
            print("Data loaded successfully")
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
        # load card data
        load_cards_data(conn)
    else:
        print("Error! cannot create the database connection.")

    if conn:
        conn.close()

if __name__ == '__main__':
    main()