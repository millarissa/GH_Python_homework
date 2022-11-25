"""
Реалізуйте класс Transaction. Параметри:
- amount - суму на яку було здійснено транзакцію
- date - дату переказу
- currency - валюту в якій було зроблено переказ (за замовчуванням USD)
- usd_conversion_rate - курс цієї валюти до долара (за замовчуванням 1.0)
- description - опис транзакції (за дефолтом None)
Усі параметри повинні бути записані в захищені (_attr) однойменні атрибути.
Доступ до них лише на читання та за допомогою механізму property.
Якщо description дорівнює None, то відповідне property має повертати рядок
"No description provided".
Додатково реалізуйте властивість usd,
що має повертати суму переказу у доларах (сума * курс)
"""


class Transaction:
    def __init__(
                    self,
                    amount,
                    date,
                    currency='USD',
                    usd_conversion_rate=1.0,
                    description=None
                ):
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversion_rate = usd_conversion_rate
        self._description = description


    @property
    def amount(self):
        print('Amount:', self._amount)
        return self._amount

    @property
    def date(self):
        print('Date:', self._date)
        return self._date

    @property
    def currency(self):
        print('Currency:', self._currency)
        return self._currency

    @property
    def usd_conversion_rate(self):
        print('USD conversion rate:', self._usd_conversion_rate)
        return self._usd_conversion_rate

    @property
    def description(self):
        if self._description:
            print('Description:', self._description)
        else:
            print('No description provided')
        return self._description

    def usd(self):
        course = round(1 / self._usd_conversion_rate, 3)
        result = self._amount * course
        print('Amount in USD:', result)
        return result


transaction1 = Transaction(213, '2022.10.05', 'UAH', 37, 'Some money')
transaction1.amount
transaction1.currency
transaction1.date
transaction1.usd_conversion_rate
transaction1.description
transaction1.usd()
