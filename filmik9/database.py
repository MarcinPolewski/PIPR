from model_io import read_from_csv, write_to_csv, read_from_json, write_to_json
from os.path import splitext


class PeronPathNotFound(FileNotFoundError):
    pass


class PersonPermissionError(PermissionError):
    pass


class PersonPathIsDirectory(IsADirectoryError):
    pass


class Database:
    def __init__(self):
        self.people = []

    def load_from_file(self, path):
        ext = splitext(path)[:-1]
        try:
            with open(path, "r") as file_handle:
                if ext is "json":
                    self.people = read_from_json(file_handle)
                else:
                    self.people = read_from_csv(file_handle)
        except FileNotFoundError:
            raise PeronPathNotFound("could not open person databse")
        except PermissionError:
            raise PersonPermissionError(
                "You do not have permissions to open the database"
            )
        except IsADirectoryError:
            raise PersonPathIsDirectory("can only work on files")

    def save_to_file(self, path):
        ext = splitext(path)[:-1]
        try:
            with open(path, "w") as file_handle:
                if ext == "json":
                    write_to_json(file_handle, self.people)
                else:
                    write_to_csv(file_handle, self.people)
        except FileNotFoundError:
            raise PeronPathNotFound("could not open person databse")
        except PermissionError:
            raise PersonPermissionError(
                "You do not have permissions to open the database"
            )
        except IsADirectoryError:
            raise PersonPathIsDirectory("can only work on files")
