from scrapper.models import Product, Category # noqa


def insert_items(rosetka_item_values):
    category, created = Category.objects.get_or_create(
        id=rosetka_item_values['category_id'],
        category_title=rosetka_item_values['category_title']
    )

    Product.objects.update_or_create(
        item_id=rosetka_item_values['item_id'],
        title=rosetka_item_values['title'],
        href=rosetka_item_values['href'],
        current_price=rosetka_item_values['price'],
        old_price=rosetka_item_values['old_price'],
        brand=rosetka_item_values['brand'],
        category=category,
        sell_status=rosetka_item_values['sell_status']
    )