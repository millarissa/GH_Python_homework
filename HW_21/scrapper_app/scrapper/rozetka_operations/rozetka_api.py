import requests


class RozetkaAPI:
    def __init__(self):
        self.request_url = 'https://rozetka.com.ua/api/product-api/v4/goods/get-main'

    def get_item_data(self, item_id):
        item_data = dict()
        available_item = self._get_available_items(item_id)

        if available_item:
            item_info = available_item['data']
            item_data = dict(
                item_id=item_info['id'],
                title=item_info['title'],
                href=item_info['href'],
                price=item_info['price'],
                old_price=item_info['old_price'],
                brand=item_info['brand'],
                category_id=item_info['last_category']['id'],
                category_title=item_info['last_category']['title'],
                sell_status=item_info['sell_status']
            )

        return item_data

    def _get_response(self, item_id):
        params = {'goodsId': item_id}
        response = requests.get(self.request_url, params=params)
        return response

    def _get_available_items(self, item_id):
        response = self._get_response(item_id)
        items = response.json()
        if response.ok:
            return items
        return False
