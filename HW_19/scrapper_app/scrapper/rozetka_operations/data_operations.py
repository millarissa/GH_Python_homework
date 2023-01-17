import sqlite3
from sqlite3 import Error


class DataBaseOperations:

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect('db.sqlite3')
            return conn
        except Error as e:
            print(e)

        return conn

    def _get_data_to_insert(self, rosetka_item_values):
        inserted_items = []
        inserted_items.append(list(rosetka_item_values.values()))
        return inserted_items

    def insert_items(self, rosetka_item_values):
        file_result_list = self._get_data_to_insert(rosetka_item_values)
        conn = self.create_connection()

        cur = conn.cursor()
        sql = ''' INSERT OR IGNORE INTO scrapper_rozetkaitems(
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
