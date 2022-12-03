import sqlite3

from data_operations import CsvOperations
from data_operations import DataBaseOperations

if __name__ == '__main__':
    path_to_csv = 'rosetka_items.csv'

    operation = CsvOperations(path_to_csv)
    operation.read_csv_file()

    conn = sqlite3.connect('rosetka.db')
    database = DataBaseOperations(conn)
    database.insert_items(operation.read_csv_file())



