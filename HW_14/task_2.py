import datetime
from datetime import timedelta, datetime

import requests


class MoneyCourse:
    SITE_API_URL = 'https://api.privatbank.ua/p24api/exchange_rates?json'

    def money_course_single_date(self, user_date, user_curr):
        try:
            format_correct = bool(datetime.strptime(user_date, '%d.%m.%Y'))
        except ValueError:
            format_correct = False

        if format_correct:
            first_available_date = (datetime.now() - timedelta(days=4 * 365)).strftime('%d.%m.%Y')
            if user_date <= first_available_date:
                params = {'date': user_date}
                api_by_date = requests.get(self.SITE_API_URL, params=params).json()
                rates = api_by_date['exchangeRate']

                if user_curr in available_curr_list:
                    if user_curr != 'UAH':
                        print('Course for', user_curr, 'to UAH at', user_date, ':')
                        for rate_num in range(len(rates)):
                            if ('currency', user_curr) in rates[rate_num].items():
                                if 'purchaseRate' in rates[rate_num]:
                                    print('Buy:', rates[rate_num]['purchaseRate'])
                                else:
                                    print('Buy:', rates[rate_num]['purchaseRateNB'])

                                if 'saleRate' in rates[rate_num]:
                                    print('Sale:', rates[rate_num]['saleRate'])
                                else:
                                    print('Sale:', rates[rate_num]['saleRateNB'])
                    else:
                        print('Same currency as base.')
                else:
                    print('Wrong currency.')
            else:
                print('Bank hasn`t rates for this date.')
                rates = []
        else:
            print('Wrong date format.')
            rates = []

        return rates

    def money_course_date_interval(self, start_date, end_date, user_curr):
        try:
            start_correct = bool(datetime.strptime(start_date, '%d.%m.%Y'))
            end_correct = bool(datetime.strptime(end_date, '%d.%m.%Y'))
            if start_correct and end_correct:
                format_correct = True
        except ValueError:
            format_correct = False

        if format_correct:
            first_available_date = (datetime.now() - timedelta(days=4 * 365)).strftime('%d.%m.%Y')

            if start_date <= first_available_date and end_date <= first_available_date:
                if start_date < end_date:
                    new_start_date = datetime.strptime(start_date, "%d.%m.%Y").date()
                    new_end_date = datetime.strptime(end_date, "%d.%m.%Y").date()
                    today = datetime.now().date()

                    if new_end_date <= today:
                        delta = new_end_date - new_start_date
                        days_interval = []
                        for i in range(delta.days + 1):
                            day = (new_start_date + timedelta(days=i)).strftime('%d.%m.%Y')
                            days_interval.append(day)

                        for single_day in days_interval:
                            course.money_course_single_date(single_day, user_curr)
                    else:
                        print('Wrong end date.')
                else:
                    print('Wrong interval')
            else:
                print('Bank hasn`t rates for this date.')
        else:
            print('Wrong date format.')

        return


if __name__ == '__main__':
    course = MoneyCourse()

    print("""Money exchange course.
    Bank archive storage data for last 4 years.
    Available currencies: USD, EUR, CHF, GBR, PLZ, SEK, XAU, CAD 
        1. Course at one date
        2. Course at dates interval
    """)
    available_curr_list = ['USD', 'EUR', 'CHF', 'GBR', 'PLZ', 'SEK', 'XAU', 'CAD']
    operation_num = int(input('Operation number: '))
    if operation_num == 1:
        user_date = input('Enter date (dd.mm.yyyy): ')
        user_curr = input('Enter currency: ')
        course.money_course_single_date(user_date, user_curr)
    elif operation_num == 2:
        start_date = input('Enter start date (dd.mm.yyyy): ')
        end_date = input('Enter end date (dd.mm.yyyy): ')
        user_curr = input('Enter currency: ')
        course.money_course_date_interval(start_date, end_date, user_curr)
    else:
        print('Wrong operation number.')
