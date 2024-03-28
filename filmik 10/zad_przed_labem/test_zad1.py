from zad1 import (
    get_random_joke,
    write_joke_to_data_base,
    read_jokes_from_data_base,
    handle_reading_database,
    handle_appending_data_base,
)
from io import StringIO


def test_handle_appending_data_base():
    fake_data_base = "joke_id,joke_text" + "\n" + "12341234,hahahajoke"
    fake_file_handle = StringIO(
        fake_data_base,
    )

    new_joke_id = "4567"
    new_joke_text = "this isjoke2"

    handle_appending_data_base(fake_file_handle, new_joke_id, new_joke_text)

    assert "12341234,hahahajoke" == fake_file_handle.read()
    assert "\n4567,this isjoke2" == fake_file_handle.read()


def test_handle_reading_database():
    fake_data_base = "joke_id,joke_text" + "\n" + "12341234,hahahajoke"
    fake_file_handle = StringIO(fake_data_base)

    data_base = handle_reading_database(fake_file_handle)

    assert data_base[0] == {"joke_id": "12341234", "joke_text": "hahahajoke"}
