from matplotlib import pyplot as plt
import recipe


def sort_recipes(calories, labels):
    # @TODO write function to sort dishes according to their calories

    joined_lists = [(cal, lab) for cal, lab in zip(calories, labels)]
    joined_lists = sorted(joined_lists, key=lambda x: x[0], reverse=True)

    calories, labels = list(zip(*joined_lists))
    # zwracamy posortowane tablice
    return calories, labels


def plot_menu(menu):
    labels = []
    calories = []
    for _recipe in menu.recipes:
        labels.append(str(_recipe))
        calories.append(_recipe.get_kcal_per_portion())
    calories, labels = sort_recipes(calories, labels)
    # @TODO Prepare a Pie chart with calories from different dishes
    # plt.pie(calories, labels)
    # @FIXME syntax error
    plt.pie(labels, calories)
    title = f"Wigilijne kalorie: {sum(calories)}"
    plt.title(title, fontdict={"fontsize": "xx-large"})
    plt.show()


if __name__ == "__main__":
    test_recipes = [
        recipe.Recipe(
            {
                "label": "Kapusta",
                "ingredientLines": "Kapusta",
                "calories": 100,
                "yield": 5,
            }
        ),
        recipe.Recipe(
            {
                "label": "Pierogi",
                "ingredientLines": "maka, woda, farsz",
                "calories": 400,
                "yield": 2,
            }
        ),
        recipe.Recipe(
            {
                "label": "Barszcz",
                "ingredientLines": "buraki, woda, uszka",
                "calories": 500,
                "yield": 5,
            }
        ),
    ]
    test_menu = recipe.Menu(test_recipes)
    plot_menu(test_menu)
