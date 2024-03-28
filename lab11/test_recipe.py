import json
from recipe import Recipe, Menu, get_recipes

test_recipes_list = [
    {"label": "Kapusta", "ingredientLines": "Kapusta", "calories": 100, "yield": 5},
    {
        "label": "Pierogi",
        "ingredientLines": "maka, woda, farsz",
        "calories": 400,
        "yield": 2,
    },
    {
        "label": "Barszcz",
        "ingredientLines": "buraki, woda, uszka",
        "calories": 500,
        "yield": 5,
    },
]


def test_recipe():
    recipe = Recipe(test_recipes_list[0])
    assert recipe._name == "Kapusta"


def test_get_kcal_per_portion():
    recipe = Recipe(test_recipes_list[0])
    assert recipe.get_kcal_per_portion() == 20


def test_add_recipe():
    menu = Menu()
    recipe = Recipe(test_recipes_list[0])
    menu.add_recipe(recipe)
    assert menu.recipes[0]._name == "Kapusta"


def test_get_num_dishes():
    recipes = [Recipe(test_recipe) for test_recipe in test_recipes_list]
    menu = Menu(recipes)
    assert menu.get_num_dishes() == 3


def test_get_recipes():
    with open("secrets.json", "r") as file:
        secrets = json.load(file)
    assert "url" in secrets
    assert "app_id" in secrets
    assert "app_key" in secrets

    recipes = get_recipes(
        "kapusta",
        url=secrets["url"],
        app_id=secrets["app_id"],
        app_key=secrets["app_key"],
    )
    print(recipes)
    assert len(recipes) == 10
    assert recipes[1]._name == "Polish Kapusta"
