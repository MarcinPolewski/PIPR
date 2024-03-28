"""
1. Wykorzystaj moduł `zipfile` do rozpakowania archiwum z plikami. Skorzystaj z: https://docs.python.org/3/library/zipfile.html
2. Wykorzystaj moduł `pathlib`, aby znaleźć w rozpakowanej strukturze katalogów wszystkie pliki z rozszerzeniem .txt. Posortuj listę tych plików według ich nazw, a następnie odczytaj każdy z nich i połącz ich treść w jeden napis. Skorzystaj z: https://docs.python.org/3/library/pathlib.html


Sortowanie: https://docs.python.org/3/howto/sorting.html
"""
import pathlib
from zipfile import ZipFile


with ZipFile("documents.zip", "w") as myzip:
?
