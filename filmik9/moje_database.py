from model_io import read_from_csv, write_to_csv
from model_io import InvalidLineError, InvalidPersonData
from model import InvalidSexError
import os.path


class PersonPathNotFound(FileNotFoundError):
    pass


class PersonPermissionError(PermissionError):
    pass


class PersonPathIsADirectory(IsADirectoryError):
    pass


class Database:
    def __init__(self):
        self.people = []

    def load_from_file(self, path):
        with open(path, "r") as file_handle:
            try:
                self.people = read_from_csv(file_handle)
            except FileNotFoundError:
                raise PersonPathNotFound("Could not open person database")
            except PermissionError:
                raise PersonPermissionError(
                    "user doesn't have permission to poen the database"
                )
            except IsADirectoryError:
                raise PersonPathIsADirectory("Can only work on files")
            except InvalidSexError as e:
                print(f"loading data inpossible, wrong sex: {str(e)}")
            except InvalidLineError as e:
                print(f"could not load data, {str(e)}")
            except InvalidPersonData as e:
                print(str(e))

    def save_to_file(self, path):
        with open(path, "w") as file_handle:
            try:
                write_to_csv(file_handle, self.people)
            except FileNotFoundError:
                raise PersonPathNotFound("Could not open person database")
            except PermissionError:
                raise PersonPermissionError(
                    "user doesn't have permission to poen the database"
                )
            except IsADirectoryError:
                raise PersonPathIsADirectory("Can only work on files")
