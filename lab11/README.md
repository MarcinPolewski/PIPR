# Treść zadań lab 11

## Na początek potrzebujemy 4 pliki: 
- recipe.py
- test_recipe.py
- plotter.py
- test_plotter.py

## Zadanie:
Jak co roku Pani Matylda Fit przygotowuje fit wieczerzę wigilijną w oparciu o bazę przepisów udostępnioną za pomocą [api](https://developer.edamam.com/edamam-docs-recipe-api). Niestety w tym roku program z którego korzystała został zasabotowany przez Grinch'a który usunął najważniejsze elementy w dwóch plikach programu: `recipe.py` oraz `plotter.py`.

Pierwszy plik dotychczas umożliwiał komunikację z serwisem, natomiast drugi wyświetlał całkowitą liczbę kalorii spożytą w trakcie fit wieczerzy z podziałem na procentowy udział poszczególnych dań. 

Twoim zadaniem jest uratowanie Fit wigilii Pani Matyldy Fit i naprawa programu w linijkach zaczynających się od sformułowania `@TODO`. Najlepiej będzie zacząć od pliku `recipe` i funkcji `get_recipes`. Na szczęście Pani Matyldzie udało się odzyskać za pomocą gita testy które działały w poprzedniej wersji programu. Szkoda że nie zacommitowała wcześniej całego programu!

## Propozycja rozwiązania:
1. Umieścić swoje dane w pliku `secrets.json` i zaimplementować ich odczyt w odpowiednim miejscu.
2. Zaimplementować `get_recipes()`, zwrócić uwagę na test w którym sprawdzana jest ta funkcja. Jeżeli API nie działa (zwraca błąd 500), to możemy mieć do czynienia z awarią i w `get_recipes()` użyjemy danych z pliku.
3. Zaimplementować resztę `@TODO` w pliku `recipe.py` oprócz ostatniego
4. Zaimplementować `@TODO` w pliku plotter.py w oparciu o https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html
5. Zaimplementować ostatnie `@TODO` w pliku `recipe.py`
