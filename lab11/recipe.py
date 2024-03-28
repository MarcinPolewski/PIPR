import requests
import json
import plotter


def get_recipes(query, url, app_id, app_key):
    # @TODO request for the recipe with a given query. Try curl to figure out what is the structure
    list_of_recipes = requests.get(
        url.format(recipe_query=query, app_id=app_id, app_key=app_key)
    ).json()
    list_of_recipes = list_of_recipes["hits"]
    list_of_recipes_objects = []
    for recipe in list_of_recipes:
        list_of_recipes_objects.append(Recipe(recipe["recipe"]))
    pass
    return list_of_recipes_objects


class Recipe:
    def __init__(self, data):
        pass
        self._name = data["label"]
        self._ingredients = data["ingredientLines"]
        self._kcal = data["calories"]
        self._portions = data["yield"]

    def get_kcal_per_portion(self):
        # @TODO compute the portion kcal per portion
        return self._kcal // self._portions

    def __str__(self):
        return self._name


class Menu:
    def __init__(self, recipes=None):
        self.recipes = recipes if recipes is not None else []

    # @property
    # def recipes(self):
    #     return self._recipes

    def add_recipe(self, recipe):
        # @TODO add new recipe to the menu
        self.recipes.append(recipe)

    def get_menu_list(self):
        output_string = ""
        for idx, recipe in enumerate(self.recipes):
            output_string += f"{idx}. {recipe}\n"
        return output_string

    def get_num_dishes(self):
        return len(self.recipes)

    def __str__(self):
        return str(self.get_menu_list())


def main():
    # @TODO read url, id, key from json file
    url = None
    app_id = None
    app_key = None
    with open("secrets.json", "r") as file_handle:
        file_data = json.read(file_handle)
        url = file_data["url"]
        app_id = file_data["app_id"]
        app_key = file_data["app_key"]

    menu = Menu()
    n_dishes = 3
    while n_dishes > 0:
        print("What would You like to eat?")
        query = input()
        tmp_menu = Menu(get_recipes(query, url, app_id, app_key))
        if tmp_menu.get_num_dishes() == 0:
            print("No recipe with given name")
            continue
        print(tmp_menu)
        # @TODO write dish selection from the given list of recipes
        user_input = input("Which would you like to add (type c to continue)")
        if user_input[0] != "c":
            for element in user_input:
                recipe = tmp_menu.recipes[int(element)]
                menu.add_recipe(recipe)

    print("Final menu:")
    print(menu)
    plotter.plot_menu(menu)


if __name__ == "__main__":
    main()
