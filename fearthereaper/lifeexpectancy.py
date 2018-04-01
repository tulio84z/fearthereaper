import requests
from datetime import datetime, timezone

API_STRING="http://api.population.io:80/1.0/life-expectancy/total"

def get_life_expectancy(gender, country, birthday):
    #url = "male/United%20Kingdom/1952-12-13/"

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "189b87be-dc21-4cc8-a1b8-f818613a3ab0"
    }
    country = _get_formated_country(country)
    birthday = _get_formated_date(birthday)

    url = "{}/{}/{}/{}/".format(API_STRING, gender, country, birthday)

    response = requests.request("GET", url, headers=headers)

    life_expectancy = response.json()['total_life_expectancy']
    return life_expectancy

def _get_formated_date(unformated_date):
    formated_date = unformated_date
    return formated_date

def _get_formated_country(country):
    formated_contry = country.strip()
    formated_contry = formated_contry.replace(" ","%20")
    return formated_contry

def calculate_current_week_num(birthday):
    now = datetime.now(timezone.utc)
    print(type(birthday))
    print(type(now))
    difference = now - birthday
    weeks, days = divmod(difference.days, 7)

    return weeks
