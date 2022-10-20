"""
Написати функцію <bank> , яка працює за наступною логікою:
користувач робить вклад у розмірі <a> одиниць
строком на <years> років під <percents> відсотків
(кожен рік сума вкладу збільшується на цей відсоток,
ці гроші додаються до суми вкладу і в наступному році
на них також нараховуються відсотки).
Параметр <percents> є необов'язковим і має значення
по замовчуванню <10> (10%). Функція повинна принтануть суму,
яка буде на рахунку, а також її повернути
(але округлену до копійок).
"""

def bank(dep, years, perc = 10):
    sum_dep = dep
   
    for year in range(1, years + 1):
        perc_dep = sum_dep * perc / 100
        sum_dep = round(sum_dep + perc_dep, 2)
        
    print('Final sum on deposit:',sum_dep)

    return sum_dep


try:  
    dep = int(input('Enter start sum of deposit: '))
    years = int(input('Enter number of years: '))
    perc = int(input('Enter percents: ') or '10')

    bank(dep, years)
    
except ValueError:
    print('Wrong value, please, try again')
