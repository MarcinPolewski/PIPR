"""Napisz funkcję która dopisuje "top secret" jako dodatkową ostatnią linijkę w pliku, którego ścieżka jest podana w argumencie"""


def append_top_secret(path):
    with open(path, "a") as file_handle:
        file_handle.write("\ntop secret")


append_top_secret("wejsciowka.txt")
