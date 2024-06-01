import pprint

import requests

API_ID = 'ae7b3fe0'
API_KEY = '9df3c1657ee8917acb0978d30b1af0e6'


def get_recipe(ingredients, api_id, api_key):
    url = 'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key=%20{}'.format(ingredients, api_id, api_key)
    response = requests.get(url)
    data = response.json()
    single_recipe = data['hits'][0]['recipe']  # add handling for no recipes
    return single_recipe


def ingredients_is_valid(ingredients):
    return True


def ask_ingredients():
    user_ingredients = []
    first_ingredients_input = input("Please enter your first ingredient. Leave blank for a randomised recipe: ").strip()
    user_ingredients.append(first_ingredients_input)
    next_ingredients_input = input("Please enter your next ingredient. Leave blank and enter once all ingredients"
                                   " inputted: ")
    user_ingredients.append(next_ingredients_input)
    while next_ingredients_input != '':
        next_ingredients_input = input("Please enter your next ingredient. Leave blank and enter once all ingredients "
                                       "inputted: ")
        user_ingredients.append(next_ingredients_input)
    return user_ingredients





def main():
    print("Hello! Allow Edamam's API to decide what's for dinner! Tell us what's in your fridge, and we'll provide the"
          " recipe. Bon apetite!.")
    ingredients = ask_ingredients()
    print(ingredients)
    recipe = get_recipe(ingredients, API_ID, API_KEY)
    pprint.pprint(recipe)

if __name__ == "__main__":
    main()