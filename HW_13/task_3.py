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
        return self._amount

    @property
    def date(self):
        return self._date

    @property
    def currency(self):
        return self._currency

    @property
    def usd_conversion_rate(self):
        return self._usd_conversion_rate

    @property
    def description(self):
        if not self._description:
            return 'No description provided'
        return self._description

    def usd(self):
        if self.currency != 'USD':
            course = round(1 / self.usd_conversion_rate, 3)
            result = self.amount * course
        else:
            result = self.amount
        return result


transaction1 = Transaction(213, '2022.10.05', 'UAH', 37)
print(transaction1.amount)
print(transaction1.currency)
print(transaction1.date)
print(transaction1.usd_conversion_rate)
print(transaction1.description)
print('Amount in USD:', transaction1.usd())
