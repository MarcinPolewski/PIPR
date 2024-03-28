def is_date_correct(date):
    """ checks if given date is in right format(doesn't verify if particular month has 31 days etc)"""
    try:
        day, month, year = date.split(".")
        day = int(day)
        month = int(month)
        year = int(year)
        if (day < 0 or day > 31) or (month < 0 or month > 12) or (year < 0):
            return False
    except Exception:
        return False
    return True


class Artist:
    def __init__(self, alias, birthday=None):
        if not alias:
            raise ValueError("arist's alias cannot be empty")
        self._alias = alias

        if (birthday) and (not is_date_correct(birthday)):
            raise ValueError("Invalid date format")
        self._birthday = birthday

    def get_alias(self) -> str:
        """return artist's alias"""
        return self._alias

    def get_birthday(self) -> str:
        """returns artist's birthday or None if it's unknown"""
        return self._birthday

    def set_alias(self, new_alias):
        """ sets artist's alias to given one"""
        if not new_alias:
            raise ValueError("alias cannot be empty")
        self._alias = new_alias

    def set_birthday(self, new_birthday):
        """ sets artist's birthday to given date"""
        if (not new_birthday) or (not is_date_correct(new_birthday)):
            raise ValueError("invalid birthday date provided")
        self._birthday = new_birthday

    def __str__(self):
        return f"{self._alias}{f", born on {self._birthday}" if self._birthday else ""}"


class Song:
    def __init__(self, artist, title, duration):
        if not isinstance(artist, Artist):
            raise ValueError("gived artist is not an instance of Artist Class")
        if (not title):
            raise ValueError("provided values cannot be empty")
        if duration < 0:
            raise ValueError("Duration cannot be negative value")

        self._artist = artist
        self._title = title
        self._duration = duration

    def get_artist(self):
        """ returns artist's alias"""
        return self._artist

    def get_title(self):
        """ returns sonngs title"""
        return self._title

    def set_artist(self, new_artist):
        if not isinstance(new_artist, Artist):
            raise ValueError("given artist is not an instance of artist class")
        self._artist = new_artist

    def get_duration(self):
        """ returns song's duration"""
        return self._duration

    def set_title(self, new_title):
        """ sets song's title to given one"""
        if not new_title:
            raise ValueError("title cannot be empty")
        self._title = new_title

    def set_duration(self, new_duration):
        """ sets song's duration to given value"""
        if new_duration < 0:
            raise ValueError("duration cannnot be a negative value")
        self._duration = new_duration

    def __str__(self):
        """ returns basic information about song(title, artist, duration)"""
        return f"This is song called {self._title} by {self._artist}. It is {self._duration:.2f} {"minute" if self._duration == 1 else "minutes"} long"
