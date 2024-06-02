from datetime import datetime
import pprint
import requests

API_ID = 'ae7b3fe0'
API_KEY = '9df3c1657ee8917acb0978d30b1af0e6'


def get_recipe(ingredients, api_id, api_key):
    if not ingredients:
        url = 'https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&random=true&mealType=Dinner'.format(api_id, api_key)
    else:
        formatted_user_ingredients = ",".join(ingredients)
        url = 'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key=%20{}&random=true&mealType=Dinner'.format(formatted_user_ingredients, api_id, api_key)
    print(url)
    response = requests.get(url)
    data = response.json()
    single_recipe = data['hits'][0]['recipe']  # add handling for no recipes
    return single_recipe


def ingredients_is_valid(ingredients):
    return True


def ask_ingredients():
    user_ingredients = []
    first_ingredients_input = input("Please enter your first ingredient. Leave blank for a randomised recipe: ").strip()
    if first_ingredients_input == '':
        return user_ingredients
    else:
        user_ingredients.append(first_ingredients_input)
    next_ingredients_input = input("Please enter your next ingredient. Leave blank and enter once all ingredients"
                                   " inputted: ").strip()
    while next_ingredients_input != '':
        user_ingredients.append(next_ingredients_input)
        next_ingredients_input = input("Please enter your next ingredient. Leave blank and enter once all ingredients "
                                       "inputted: ").strip()
    return user_ingredients


def write_to_file(recipe, elapsed_time):
    recipe_title = recipe['label']
    recipe_ingredients = recipe['ingredientLines']
    url = recipe['url']
    recipe_instructions_url = ("See full cooking instructions on: {}".format(url))
    timer = ("It took us {}ms to find a recipe for your dinner tonight!".format(elapsed_time))
    with open('recipe_output.md', 'w') as file:
        file.writelines('# :plate_with_cutlery: {} :knife: \n\n{} \n\n{} \n\n{}'.format(recipe_title, recipe_ingredients, recipe_instructions_url, timer))



def main():
    print("Hello! Allow Edamam's API to decide what's for dinner! Tell us what's in your fridge, and we'll provide the"
          " recipe. Bon apetite!.")
    ingredients = ask_ingredients()
    print(ingredients)  # delete at end
    time_now = datetime.now()
    recipe = get_recipe(ingredients, API_ID, API_KEY)
    pprint.pprint(recipe)  # delete at end
    elapsed_time = (datetime.now() - time_now).microseconds/1000
    write_to_file(recipe, elapsed_time)





if __name__ == "__main__":
    main()