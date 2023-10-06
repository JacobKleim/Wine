import datetime
from collections import defaultdict

import pandas


def group_wines_by_category(file):
    wines = pandas.read_excel(file,
                              na_values='nan',
                              keep_default_na=False)

    wines_by_category = defaultdict(list)

    for _, row in wines.iterrows():
        category = row['Категория']
        wine = {
            'Название': row['Название'],
            'Категория': row['Категория'],
            'Сорт': row['Сорт'],
            'Цена': row['Цена'],
            'Картинка': row['Картинка'],
            'Акция': row['Акция'],
        }
        wines_by_category[category].append(wine)
    return wines_by_category


def get_past_years():
    foundation_year = 1920
    current_year = datetime.datetime.now().year
    past_years = current_year - foundation_year
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
