import requests
import csv
import os


def get_random_joke():
    """gets joke from api"""
    link = "https://icanhazdadjoke.com/"
    serwer_answer = requests.get(link, headers={"Accept": "application/json"}).json()
    joke_id = serwer_answer["id"]
    joke_text = serwer_answer["joke"]

    return joke_id, joke_text


def handle_reading_database(file_handle):
    reader = csv.DictReader(file_handle)
    joke_data_base = []

    for row in reader:
        joke_data_base.append(
            {"joke_id": row["joke_id"], "joke_text": row["joke_text"]}
        )

    return joke_data_base


def read_jokes_from_data_base():
    path = "database.txt"
    database = []
    try:
        with open(path, "r") as file_handle:
            database = handle_reading_database(file_handle)
    except FileNotFoundError:
        print("could not find a file ")
    except PermissionError:
        print("yout do not have permision to db")
    except Exception as e:
        print("Error found during reading db")
        print(e)
    return database


def handle_appending_data_base(file_handle, joke_id, joke_text):
    file_handle.write("\n" + joke_id + "," + joke_text)
    # file_writer = csv.writer(
    #     file_handle,
    # )
    # file_writer.writerow(joke_id + joke_text)


def write_joke_to_data_base(joke_id, joke_text):
    path = "database.txt"
    try:
        with open(path, "a") as file_handle:
            handle_appending_data_base(file_handle, joke_id, joke_text)
    except FileNotFoundError:
        print("could not find this file")
    except PermissionError:
        print("Insufficient permision to access database")
    except Exception:
        print("Error during appending the database")


def user_interface():
    is_programm_running = True
    random_joke = None
    while is_programm_running:
        print(
            "Controls:"
            + "\n"
            + "quit: q"
            + "\n"
            + "read data base; r"
            + "\n"
            + "get random joke: g"
            + "\n"
            + "save current joke to database: s"
            + "\n"
        )

        user_input = input()
        user_input.rstrip()
        if user_input in ["q", "Q"]:
            is_programm_running = False
        elif user_input in ["r", "R"]:
            jokes = read_jokes_from_data_base()
            for joke in jokes:
                print(joke["joke_id"] + ", " + joke["joke_text"])
        elif user_input in ["g", "G"]:
            random_joke = get_random_joke()
            print(random_joke[0] + ", " + random_joke[1])
        elif user_input in ["s", "S"]:
            if random_joke:
                write_joke_to_data_base(random_joke[0], random_joke[1])
        else:
            print("invalid input")


def main():
    # joke_id, joke_text = get_random_joke()
    # write_joke_to_data_base(joke_id, joke_text)

    user_interface()


if __name__ == "__main__":
    main()
