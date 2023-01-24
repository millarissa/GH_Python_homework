from scrapper.models import Product # noqa


def _get_data_to_insert(rosetka_item_values):
    inserted_items = []
    inserted_items.append(list(rosetka_item_values.values()))
    return inserted_items


def insert_items(rosetka_item_values):
    file_result_list = _get_data_to_insert(rosetka_item_values)
    item_details = file_result_list[0]
    Product.objects.update_or_create(
        item_id=item_details[0],
        title=item_details[1],
        href=item_details[2],
        current_price=item_details[3],
        old_price=item_details[4],
        brand=item_details[5],
        category=item_details[6]
    )
