# additional module imported (used to capture the time it takes the API to return the recipe)
from datetime import datetime

import requests


# my API access ID and key, see README for instructions on acquiring your own ID and key.
API_ID = 'ae7b3fe0'
API_KEY = '9df3c1657ee8917acb0978d30b1af0e6'


# method for passing user inputs to API and returning a recipe
def get_recipe(ingredients, api_id, api_key):
    # if no ingredients are inputted by user, a random recipe is called from the API
    if not ingredients:
        url = ('https://api.edamam.com/api/recipes/v2?type=public&app_id={}&app_key={}&random=true&mealType=Dinner'
               .format(api_id, api_key))
    # if ingredients are inputted, these are passed to the API
    else:
        # inputted ingredients joined in a list
        formatted_user_ingredients = ",".join(ingredients)
        url = ('https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key=%20{}&random=true&mealType='
               'Dinner').format(formatted_user_ingredients, api_id, api_key)
    response = requests.get(url)
    data = response.json()
    hits = data['hits']
    # if no recipes are found for the inputted ingredient, None is returned
    if not hits:
        return None
    # if a recipe is found for the inputted ingredients, the first recipe is returned
    else:
        single_recipe = data['hits'][0]['recipe']
        return single_recipe


# method for asking user for ingredient inputs
def ask_ingredients():
    user_ingredients = []
    ingredients_input = input("Please enter your first ingredient. Leave blank for a randomised recipe: ").strip()
    # whilst an ingredient is inputted, the user will continue to be asked to input the next ingredient
    while ingredients_input != '':
        # user ingredient list appended to add each ingredient inputted by user
        user_ingredients.append(ingredients_input)
        ingredients_input = input("Please enter your next ingredient. Leave blank and enter once all ingredients "
                                       "inputted: ").strip()
    # when the user stops inputting ingredients, return the list of user ingredients
    return user_ingredients


# method for writing API recipe title, image, ingredient list, instructions link & API return time to markdown file
def write_to_file(recipe, elapsed_time):
    recipe_title = recipe['label']
    # first 10 letters of recipe title used as markdown file name
    file_name = recipe_title[0:10].replace(" ", "_")
    image = recipe['image']
    recipe_ingredients = recipe['ingredientLines']
    url = recipe['url']
    recipe_instructions_url = ("See full cooking instructions on: {}".format(url))
    timer = ("It took us {}ms to find a recipe for your dinner tonight!".format(elapsed_time))
    # ingredients in list formatted into bullet points in markdown
    formatted_ingredients = "\n".join(["- {}".format(item) for item in recipe_ingredients])
    with open('recipe_output/{}.md'.format(file_name), 'w') as file:
        markdown_content = ('# {} \n\n'
                            '![recipe_image]({}) \n\n'
                            '## Ingredients:\n{} \n\n'
                            '## Instructions:\n{} \n\n'
                            '### Powered by Edamam \n{}'
                            .format(recipe_title, image, formatted_ingredients, recipe_instructions_url, timer))
        # all formatted API recipe content written to markdown file
        file.writelines(markdown_content)


# main method, calling on all above supplementary methods
def main():
    print("Hello! Allow Edamam's API to decide what's for dinner! Tell us what's in your fridge, and we'll provide the"
          " recipe. Bon apetite!")
    ingredients = ask_ingredients()
    time_now = datetime.now()
    recipe = get_recipe(ingredients, API_ID, API_KEY)
    # time taken for API to return recipe
    elapsed_time = (datetime.now() - time_now).microseconds/1000
    # if no recipes are found for inputted ingredients (as per get_recipe method), user is asked to restart app
    if recipe is None:
        print("No recipes found for your entered ingredients. Please restart app and try again.")
    # if recipes are found for inputted ingredients, write them to file
    else:
        write_to_file(recipe, elapsed_time)


if __name__ == "__main__":
    main()