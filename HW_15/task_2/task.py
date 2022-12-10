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
        if rosetka_item_data:
            rosetka_item_values = rosetka_item_data[0]
            print(rosetka_item_values)
            database.insert_items(rosetka_item_values)
        else:
            print('For', item_id, 'no data available')


