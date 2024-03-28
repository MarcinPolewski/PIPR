from zadanie3 import Artist, Song, is_date_correct
import pytest

"""
-birthday has to have format day.month.year
-alias of artist cannot be empty
-song title cannot be empty
-song duration cannot be negative(can be 0)
"""


def test_is_date_correct():
    assert is_date_correct("12.12.1999")
    assert is_date_correct("12.12.1999")
    assert not is_date_correct("32.12.1999")
    assert not is_date_correct("12.13.1999")
    assert not is_date_correct("12.12")
    assert not is_date_correct("12.12.1999.1234")
    assert not is_date_correct("12/12/1999")
    assert not is_date_correct("12121999")


def test_Artist_init_and_getters():
    artist = Artist("The Rolling Stones")
    assert artist.get_alias() == "The Rolling Stones"

    artist = Artist("Jórek Ogórek", "03.04.1999")
    assert artist.get_alias() == "Jórek Ogórek"
    assert artist.get_birthday() == "03.04.1999"


def test_Artist_init_and_getters_empty_alias():
    with pytest.raises(ValueError):
        artist = Artist("")


def test_Artist_init_and_getters_invalid_date_format():
    with pytest.raises(ValueError):
        artist = Artist("JJ", "34.12.1999")
    with pytest.raises(ValueError):
        artist = Artist("JJ", "04.13.1999")
    with pytest.raises(ValueError):
        artist = Artist("JJ", "04/12/1999")
    with pytest.raises(ValueError):
        artist = Artist("JJ", "34.12")
    with pytest.raises(ValueError):
        artist = Artist("JJ", "34.12.1999.1234")
    with pytest.raises(ValueError):
        artist = Artist("JJ", "test.test.test")
    with pytest.raises(ValueError):
        artist = Artist("JJ", "slkdfjlfsakjf")


def test_Artist_set_alias():
    artist = Artist("The Rolling Stones")
    assert artist.get_alias() == "The Rolling Stones"
    artist.set_alias("The Rolling Stones - Reborn")
    assert artist.get_alias() == "The Rolling Stones - Reborn"


def test_Artist_set_alias_empty():
    artist = Artist("The Rolling Stones")
    with pytest.raises(ValueError):
        artist.set_alias("")


def test_Artist_set_birthday():
    artist = Artist("The Rolling Stones")
    artist.set_birthday("02.04.2005")
    assert artist.get_birthday() == "02.04.2005"

    artist = Artist("ACDC", "02.04.2005")
    artist.set_birthday("02.7.1999")
    assert artist.get_birthday() == "02.7.1999"


def test_Artist_set_birthday_empty():
    artist = Artist("The Rolling Stones")
    with pytest.raises(ValueError):
        artist.set_birthday("")


def test_Artist_set_birthday_invalid_date():
    artist = Artist("The Rolling Stones")
    with pytest.raises(ValueError):
        artist.set_birthday("34.12.1999")
    with pytest.raises(ValueError):
        artist.set_birthday("04.13.1999")
    with pytest.raises(ValueError):
        artist.set_birthday("34.12")
    with pytest.raises(ValueError):
        artist.set_birthday("34.12.1999.1234")
    with pytest.raises(ValueError):
        artist.set_birthday("test.test.test")
    with pytest.raises(ValueError):
        artist.set_birthday("slkdfjlfsakjf")


def test_Artist__str__():
    artist = Artist("The Rolling Stones")
    assert str(artist) == "The Rolling Stones"

    artist = Artist("Jórek Ogórek", "03.04.1999")
    assert str(artist) == "Jórek Ogórek, born on 03.04.1999"


def test_Song_init_and_getters():
    artist = Artist("Jórek Ogórek", "03.04.1999")
    song = Song(artist, "Do Aliny Maliny", 5.20)

    assert song.get_artist() == artist
    assert song.get_title() == "Do Aliny Maliny"
    assert song.get_duration() == 5.20


def test_Song_init_and_getters_invalid_values():
    artist = Artist("Jórek Ogórek", "03.04.1999")
    with pytest.raises(ValueError):
        song = Song(artist, "", 5.20)
    with pytest.raises(ValueError):
        song = Song("artist", "Do Aliny Maliny", 5.20)
    with pytest.raises(ValueError):
        song = Song(artist, "Do Aliny Maliny", -5.20)


def test_Song_set_artist():
    artist = Artist("Jórek Ogórek", "03.04.1999")
    artist2 = Artist("Bolek Lolek", "03.04.1999")
    song = Song(artist, "Do Aliny Maliny", 5.20)

    song.set_artist(artist2)
    assert song.get_artist() == artist2


def test_Song_set_artist_class_not_provided():
    artist = Artist("Jórek Ogórek", "03.04.1999")
    artist2 = Artist("Bolek Lolek", "03.04.1999")
    song = Song(artist, "Do Aliny Maliny", 5.20)

    with pytest.raises(ValueError):
        song.set_artist("artist2")


def test_Song_set_title():
    artist = Artist("Jórek Ogórek", "03.04.1999")
    song = Song(artist, "Do Aliny Maliny", 5.20)
    song.set_title("Do Julki Kulki")

    assert song.get_title() == "Do Julki Kulki"


def test_Song_set_title_empty():
    artist = Artist("Jórek Ogórek", "03.04.1999")
    song = Song(artist, "Do Aliny Maliny", 5.20)

    with pytest.raises(ValueError):
        song.set_title("")


def test_Song_set_duration():
    artist = Artist("Jórek Ogórek", "03.04.1999")
    song = Song(artist, "Do Aliny Maliny", 5.20)

    song.set_duration(12.34)
    assert song.get_duration() == 12.34


def test_Song_set_duration_negative():
    artist = Artist("Jórek Ogórek", "03.04.1999")
    song = Song(artist, "Do Aliny Maliny", 5.20)

    with pytest.raises(ValueError):
        song.set_duration(-1.1)


def test_Song__str__():
    artist = Artist("Jórek Ogórek", "03.04.1999")

    song = Song(artist, "Do Aliny Maliny", 5.20)
    assert (
        str(song)
        == "This is song called Do Aliny Maliny by Jórek Ogórek, born on 03.04.1999. It is 5.20 minutes long"
    )

    song = Song(artist, "Do Aliny Maliny", 1.00)
    assert (
        str(song)
        == "This is song called Do Aliny Maliny by Jórek Ogórek, born on 03.04.1999. It is 1.00 minute long"
    )
