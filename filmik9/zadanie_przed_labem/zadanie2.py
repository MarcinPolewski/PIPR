import os.path
import json


class PathNotAFIle(Exception):
    def __inti__(self, path):
        super().__inti__("given path({path}) does not lead to a file")
        self._path = path


class FileInfo:
    def __init__(self, path):
        if not os.path.isfile(path):
            raise PathNotAFIle(path)

        self._path = path
        self._parent_folder_path = os.path.dirname(path)
        self._parent_folder_name = os.path.basename(os.path.dirname(path))
        self._file_name = os.path.splitext(os.path.basename(self._path))[0]
        self._file_ext = os.path.splitext(path)[1]

    @property
    def path(self):
        return self._path

    @property
    def parent_folder_path(self):
        return self._parent_folder_path

    @property
    def parent_folder_name(self):
        return self._parent_folder_name

    @property
    def file_name(self):
        return self._file_name

    @property
    def file_ext(self):
        return self._file_ext

    def set_path(self, new_path):
        if not os.path.isfile(new_path):
            raise PathNotAFIle(new_path)
        self._path = new_path

    def count_lines(self):
        """counts lines, if couldn't open file returns None"""
        counter = 0
        try:
            with open(self._path, "r") as file_handle:
                for line in file_handle:
                    counter += 1
            return counter
        except Exception:
            return None


def write_to_json(file_handle, file_info_classes):
    data_to_dump = []
    for file_info_class in file_info_classes:
        # path = file_info_class.path
        # parent_folder_path = file_info_class.parent_folder_path
        # parent_folder_name = file_info_class.parent_folder_name
        # file_name = file_info_class.file_name
        # file_ext = file_info_class.file_ext
        file_info = {
            "path": file_info_class.path,
            "parent_folder_path": file_info_class.parent_folder_path,
            "parent_folder_name": file_info_class.parent_folder_name,
            "file_name": file_info_class.file_name,
            "file_ext": file_info_class.file_ext,
            "number_of_lines": file_info_class.count_lines(),
        }
        data_to_dump.append(file_info)

    json.dump(data_to_dump, file_handle, indent=4)


def read_from_json(file_handle):
    file_info_classes = []
    file_data = json.load(file_handle)
    for row in file_data:
        fi = FileInfo(row["path"])
        file_info_classes.append(fi)
    return file_info_classes


def main():
    fi1 = FileInfo(
        "/Users/marcinpolewski/Documents/Studia/PIPR/laby i filmiki/filmik9/zadanie_przed_labem/zad1.txt"
    )
    fi2 = FileInfo(
        "/Users/marcinpolewski/Documents/Studia/PIPR/laby i filmiki/filmik9/zadanie_przed_labem/zad2.txt"
    )
    fi3 = FileInfo(
        "/Users/marcinpolewski/Documents/Studia/PIPR/laby i filmiki/filmik9/zadanie_przed_labem/zad3.txt"
    )
    file_info_classes = [fi1, fi2, fi3]

    with open("classes.json", "w") as file_handle:
        write_to_json(file_handle, file_info_classes)

    read_classes = []
    with open("classes.json", "r") as file_handle:
        read_classes = read_from_json(file_handle)

    for element in read_classes:
        print(element.path)


if __name__ == "__main__":
    main()
