from celery import shared_task

from scrapper.rozetka_operations.db_operations import insert_items # noqa
from scrapper.rozetka_operations.rozetka_api import RozetkaAPI # noqa


@shared_task(name='get_and_save_items', queue='celery')
def get_and_save_items(product_ids):
    rozetka = RozetkaAPI()

    for item_id in product_ids.split('\n'):
        rosetka_item_values = rozetka.get_item_data(item_id)
        if rosetka_item_values:
            insert_items(rosetka_item_values)
            print('Added:', item_id)
        else:
            print('Not found:', item_id)
