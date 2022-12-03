import requests


class RozetkaAPI:
    def __init__(self, item_id):
        self.item_id = item_id
        self.session = requests.Session()
        self.request_url = 'https://rozetka.com.ua/api/product-api/v4/goods/get-main'
        self._response = None

    def get_item_data(self):
        item_data = list()
        if self._get_available_items():
            for item in self._get_available_items():
                item_info = item['data']
                item_data.append(dict(
                    item_id=item_info['id'],
                    title=item_info['title'],
                    href=item_info['href'],
                    price=item_info['price'],
                    old_price=item_info['old_price'],
                    brand=item_info['brand'],
                    category=item_info['last_category']['title']
                ))
        else:
            item_data.append('No data available')
        return item_data


    @property
    def response(self):
        params = {'goodsId': self.item_id}
        if not self._response:
            self._response = self.session.get(self.request_url, params=params)
        return self._response

    def _check_available_items(self):
        items = self.response.json()
        if self.response.ok:
            return items
        return False

    def _get_available_items(self):
        available_items = []
        if self._check_available_items():
            available_items.append(self._check_available_items())
        return available_items













