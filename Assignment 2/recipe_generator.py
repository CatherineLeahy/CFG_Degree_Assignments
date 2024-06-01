# List of acceptable pet types. Pet finder has more pet types available, but the most common pets were selected for this assignment.
PET_TYPES = ["cat", "dog", "rabbit"]


def ingredients_is_valid(location):
    return True


def ask_ingredients():
    ingredients_input = input("Please enter your ingredients in a comma separated list: ").strip()
    if ingredients_is_valid(location_input):
        return ingredients_input
    else:
        return ask_ingredients()

def distance_is_valid(distance):
    try:
        int(distance)
    except ValueError:
        print("Entered radius '{}' is invalid. Enter a radius to the nearest mile".format(distance))
        return False
    return True


def ask_distance():
    distance_input = input("What is your search radius (miles)? ").strip()
    if distance_is_valid(distance_input):
        return distance_input
    else:
        return ask_distance()


def pet_type_is_valid(pet_type):
    for valid_type in PET_TYPES:
        if pet_type.lower() == valid_type:
            return True
    print("Entered pet '{}' is invalid. Enter a valid pet type {}".format(pet_type, PET_TYPES))
    return False


def ask_pet_type():
    pet_type_input = input("What type of pet are you looking to adopt? ").strip()
    if pet_type_is_valid(pet_type_input):
        return pet_type_input
    else:
        return ask_pet_type()


def main():
    print("Hello! Welcome to The USA Pet Finder's command line interface.")
    location = ask_location()
    distance = ask_distance()
    pet_type = ask_pet_type()


if __name__ == "__main__":
    main()