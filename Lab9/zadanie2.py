"""
1. Wczytaj strukturę z pliku posts.json
2. Za pomocą dataclasses utwórz klasę odpowiadającą tej strukturze i przetwórz dane z pliku na listę instancji Twojej nowej klasy.
3. Dodaj metodę, która zwróci całkowitą ilość znaków w poście (tytuł + treść). Posortuj listę postów po tej całkowitej długości.
"""

import json
from dataclasses import dataclass


@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str

    def total_length(self):
        return len(self.title) + len(self.body)


def read_from_json(file_handle):
    data = json.load(file_handle)
    posts = []
    for row in data:
        userId = row["userId"]
        id = row["id"]
        title = row["title"]
        body = row["body"]
        post = Post(userId, id, title, body)
        posts.append(post)
    return posts


try:
    with open("posts.json") as file_handle:
        posts = read_from_json(file_handle)
except FileNotFoundError:
    print("could not find this file")
except PermissionError:
    print("insufficient permission")

posts = sorted(posts, key=lambda post: post.total_length())
for post in posts:
    print(post.total_length())
