import requests


class RozetkaAPI:
    def __init__(self):
        self.session = requests.Session()
        self.request_url = 'https://rozetka.com.ua/api/product-api/v4/goods/get-main'
        self._response = None

    def get_item_data(self, item_id):
        item_data = list()
        available_item = self._check_available_items(item_id)
        item_info = available_item['data']
        item_data.append(dict(
            item_id=item_info['id'],
            title=item_info['title'],
            href=item_info['href'],
            price=item_info['price'],
            old_price=item_info['old_price'],
            brand=item_info['brand'],
            category=item_info['last_category']['title']
        ))

        return item_data

    def _get_response(self, item_id):
        params = {'goodsId': item_id}
        if not self._response:
            self._response = self.session.get(self.request_url, params=params)
        return self._response

    def _check_available_items(self, item_id):
        items = self._get_response(item_id).json()
        if self._response.ok:
            return items
        return False

    def _get_available_items(self, item_id):
        available_items = []
        checked_item = self._check_available_items(item_id)
        if checked_item:
            available_items.append(checked_item)
        return available_items
