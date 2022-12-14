import csv

import sqlite3
from sqlite3 import Error


class CsvOperations:
    def read_csv_file(self):
        with open('rosetka_items.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            items_id_list = []
            for row in reader:
                item_id = row['item_id']
                items_id_list.append(item_id)
            return items_id_list


class DataBaseOperations:

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect('rosetka.db')
            return conn
        except Error as e:
            print(e)

        return conn

    def _create_table(self, create_table_sql):
        try:
            conn = self.create_connection()
            c = conn.cursor()
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

    def _get_data_to_insert(self, rosetka_item_values):
        inserted_items = []
        inserted_items.append(list(rosetka_item_values.values()))
        return inserted_items

    def insert_items(self, rosetka_item_values):
        file_result_list = self._get_data_to_insert(rosetka_item_values)
        conn = self.create_connection()
        self._create_items_table()

        cur = conn.cursor()
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

        conn.commit()
        return cur.lastrowid
