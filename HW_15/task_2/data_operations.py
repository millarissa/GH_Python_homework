import csv

import sqlite3
from sqlite3 import Error

from rozetka_api import RozetkaAPI


class CsvOperations:

    def __init__(self, path_to_csv):
        self.path_to_csv = path_to_csv

    def read_csv_file(self):
        with open(self.path_to_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            all_rosetka_items = []
            for row in reader:
                item_id = row['item_id']
                rosetka = RozetkaAPI(item_id)
                for rosetka_item in rosetka.get_item_data():
                    print(rosetka_item)
                    if type(rosetka_item) == dict:
                        all_rosetka_items.append(list(rosetka_item.values()))
            return all_rosetka_items


class DataBaseOperations:
    def __init__(self, conn):
        self.conn = conn

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def _create_table(self, create_table_sql):
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

        return

    def _create_items_table(self):
        sql = """ CREATE TABLE IF NOT EXISTS rosetka_items (
                                            item_id int,
                                            title text,
                                            href text,
                                            current_price text,
                                            old_price text, 
                                            brand text,
                                            category text,
                                            UNIQUE(item_id)
                                        ); """

        self._create_table(sql)
        return

    def insert_items(self, file_result_list):
        self._create_items_table()

        cur = self.conn.cursor()
        sql = ''' INSERT OR IGNORE INTO rosetka_items(
                                            item_id,
                                            title,
                                            href,
                                            current_price,
                                            old_price, 
                                            brand,
                                            category)
                          VALUES(?,?,?,?,?,?,?)'''

        for item in file_result_list:
            cur.execute(sql, item)

        self.conn.commit()
        return cur.lastrowid

