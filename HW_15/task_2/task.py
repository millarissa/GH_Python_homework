import rozetka_api
from data_operations import DataBaseOperations
from data_operations import CsvOperations


if __name__ == '__main__':
    csv_file = CsvOperations()
    database = DataBaseOperations()
    rozetka = rozetka_api.RozetkaAPI()

    list_of_ids = csv_file.read_csv_file()

    rosetka_item_list = []
    for item_id in list_of_ids:
        rosetka_item_data = rozetka.get_item_data(item_id)
        database.insert_items(item_id, rosetka_item_data)
