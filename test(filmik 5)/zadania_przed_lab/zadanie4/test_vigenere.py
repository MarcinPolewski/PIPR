from vigenere import encrypt_vigenere, decrypt_vigenere
import pytest


def test_encrypt_vigenere_typical():
    assert (
        encrypt_vigenere("TAJNE", "TO JEST BARDZO TAJNY TEKST")
        == "MO SRWM BJEHSO CNNGY CROLT"
    )


def test_decrypt_vigenere_typical():
    assert (
        decrypt_vigenere("TAJNE", "MO SRWM BJEHSO CNNGY CROLT")
        == "TO JEST BARDZO TAJNY TEKST"
    )


def test_encrypt_vigenere_key_is_longer():
    assert (
        encrypt_vigenere(
            "TAJNETAJNETAJNETAJNETAJNETAJNETAJNETAJNE", "TO JEST BARDZO TAJNY TEKST"
        )
        == "MO SRWM BJEHSO CNNGY CROLT"
    )


def test_decrypt_vigenere_key_is_longer():
    assert (
        decrypt_vigenere(
            "TAJNETAJNETAJNETAJNETAJNETAJNETAJNETAJNE", "MO SRWM BJEHSO CNNGY CROLT"
        )
        == "TO JEST BARDZO TAJNY TEKST"
    )


def test_encrypt_vigenere_small_letters():
    assert (
        encrypt_vigenere("TaJnE", "tO jEsT BaRDZo TAjNY TeKsT")
        == "MO SRWM BJEHSO CNNGY CROLT"
    )


def test_decrypt_vigenere_small_letters():
    assert (
        encrypt_vigenere("TaJnE", "tO jEsT BaRDZo TAjNY TeKsT")
        == "MO SRWM BJEHSO CNNGY CROLT"
    )


def test_encrypt_vigenere_key_is_number():
    with pytest.raises(ValueError):
        encrypt_vigenere("1", "TO JEST BARDZO TAJNY TEKST")


def test_decrypt_vigenere_key_is_number():
    with pytest.raises(ValueError):
        decrypt_vigenere("1", "MO SRWM BJEHSO CNNGY CROLT")


def test_encrypt_vigenere_text_no_letters():
    with pytest.raises(ValueError):
        encrypt_vigenere("TAJNE", "TO JEST BARDZ12O TA%JNY TEK#ST")


def test_decrypt_vigenere_text_no_letters():
    with pytest.raises(ValueError):
        decrypt_vigenere("1", "MO SR1WM BJ5HSO% CNNGY C#ROLT")


def test_encrypt_vigenere_empty_key():
    assert (
        encrypt_vigenere("", "TO JEST BARDZO TAJNY TEKST")
        == "TO JEST BARDZO TAJNY TEKST"
    )


def test_decrypt_vigenere_empty_key():
    assert (
        decrypt_vigenere("", "TO JEST BARDZO TAJNY TEKST")
        == "TO JEST BARDZO TAJNY TEKST"
    )


def test_encrypt_vigenere_empty_text():
    assert encrypt_vigenere("TAJNE", "") == ""


def test_decrypt_vigenere_empty_text():
    assert decrypt_vigenere("TAJNE", "") == ""
