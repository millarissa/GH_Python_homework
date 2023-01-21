import sys
from pathlib import Path
import os
import django

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrapper_app.settings")

if __name__ == '__main__':
    django.setup()

from rozetka_api import RozetkaAPI
from db_operations import insert_items


def save_rozetka_items(item_id):
    rozetka = RozetkaAPI()

    rosetka_item_values = rozetka.get_item_data(item_id)
    if rosetka_item_values:
        insert_items(rosetka_item_values)


save_rozetka_items(sys.argv[1])
