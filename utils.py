import datetime
from collections import defaultdict

import pandas


def convert_to_dictionary():
    wines = pandas.read_excel('wine.xlsx',
                              na_values='nan',
                              keep_default_na=False)

    wines_by_category = defaultdict(list)

    for _, row in wines.iterrows():
        category = row['Категория']
        wine_data = {
            'Название': row['Название'],
            'Категория': row['Категория'],
            'Сорт': row['Сорт'],
            'Цена': row['Цена'],
            'Картинка': row['Картинка'],
            'Акция': row['Акция'],
        }
        wines_by_category[category].append(wine_data)
    return wines_by_category


def get_past_years():
    now = datetime.datetime.now()
    foundation_date = datetime.datetime(year=1920, month=1, day=1)
    days = (now - foundation_date).days
    year_days = 365
    past_years = int(days / year_days)
    return past_years


def get_year_form(number):
    if number % 100 in [11, 12, 13, 14]:
        return 'лет'
    elif number % 10 == 1:
        return 'год'
    elif number % 10 in [2, 3, 4]:
        return 'года'
    else:
        return 'лет'
