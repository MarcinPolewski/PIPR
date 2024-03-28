import os.path


class PathNotAFIle(Exception):
    def __inti__(self, path):
        super().__inti__("given path({path}) does not lead to a file")
        self._path = path


class FileInfo:
    def __init__(self, path):
        self._path = path
        if not os.path.isfile(path):
            raise PathNotAFIle(path)

    @property
    def parent_folder_path(self):
        """returns path to catalog"""
        return os.path.dirname(self._path)

    @property
    def parent_folder_name(self):
        return os.path.basename(os.path.dirname(self._path))

    @property
    def file_name(self):
        return os.path.splitext(os.path.basename(self._path))[0]

    @property
    def file_ext(self):
        return os.path.splitext(self._path)[1]

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


path = "/Users/marcinpolewski/Documents/Studia/PIPR/laby i filmiki/filmik9/zadanie_przed_labem/zad1.txt"
fi = FileInfo(path)
