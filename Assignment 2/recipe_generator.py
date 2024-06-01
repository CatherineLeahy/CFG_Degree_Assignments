import pprint

import requests

API_ID = ''
API_KEY = ''


def get_recipe(ingredients, api_id, api_key):
    url = 'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key=%20{}'.format(ingredients, api_id, api_key)
    response = requests.get(url)
    data = response.json()
    single_recipe = data['hits'][0]['recipe']
    return single_recipe


def ingredients_is_valid(ingredients):
    return True


def ask_ingredients():
    ingredients_input = input("Please enter your ingredients in a comma separated list: ").strip()
    if ingredients_is_valid(ingredients_input):
        return ingredients_input
    else:
        return ask_ingredients()


def main():
    print("Hello! Allow Edamam's API to decide what's for dinner! Tell us what's in your fridge, and we'll provide the"
          " recipe. Bon apetite!.")
    ingredients = ask_ingredients()
    recipe = get_recipe(ingredients, API_ID, API_KEY)
    pprint.pprint(recipe)

if __name__ == "__main__":
    main()