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

def create_cards_table(conn):
    """ create a cards table in the database """
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS cards (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                datasource_name TEXT NOT NULL
                            );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print(f"Table created successfully: cards")
    except sqlite3.Error as e:
        print(e)

def main():
    database = "data/processed/disney_lorcana.db"

    # create a database connection
    conn = create_connection(database)

    # create table
    if conn is not None:
        create_cards_table(conn)
    else:
        print("Error! cannot create the database connection.")

    if conn:
        conn.close()

if __name__ == '__main__':
    main()