
def ingredients_is_valid(location):
    return True


def ask_ingredients():
    ingredients_input = input("Please enter your ingredients in a comma separated list: ").strip()
    if ingredients_is_valid(ingredients_input):
        return ingredients_input
    else:
        return ask_ingredients()

def main():
    print("Hello! Allow Edamam's API to decide what's for dinner! Tell us what's in your fridge, and we'll provide the recipe. Bon apetite!.")
    ingredients = ask_ingredients()


if __name__ == "__main__":
    main()