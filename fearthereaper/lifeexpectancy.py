import requests

API_STRING="http://api.population.io:80/1.0/life-expectancy/total/"

def get_life_expectancy(gender, country, birthday):
    url = "male/United%20Kingdom/1952-12-13/"

    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "189b87be-dc21-4cc8-a1b8-f818613a3ab0"
    }
    url = "{}/{}/{}/{}".format(API_STRING, gender, country, birthday)

    country = _get_formated_country(country)

    response = requests.request("GET", url, headers=headers)

    life_expectancy = response.json()['total_life_expectancy']
    return life_expectancy

def _get_formated_country(country):
    formated_contry = country.strip()
    formated_contry = formated_contry.replace(" ","%20")
    return formated_contry
