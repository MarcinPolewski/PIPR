# Zadanie 1
# Napisz funkcję, która jako parametr przyjmuje wyraz i tworzy słownik, gdzie kluczami są litery, zaś wartościami liczba ich wystąpień w danym słowie. Przykład: dla słowa "kukułka" funkcja powinna zwrócić: {'k': 3, 'u': 2, 'ł': 1, 'a': 1}.
def count_chars(word):
    char_counter = {}
    for char in word:
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] += 1
        # lub char_counter = counts.get(char,0) + 1 <- zamiast tych ifów
    return char_counter


# print(count_chars("kukułka"))
# Zadanie 2
# Napisz funkcję, która jako parametry przyjmuje napis, oraz krotkę z literą i jej częstością. Funkcja powinna odfiltrować z napisu słowa (przyjmujemy, że słowa oddzielone są od siebie spacją), które zawierają więcej lub tyle samo wystąpień podanej litery w stosunku do zadanej częstości. Przykładowe argumenty:


def count_letter(word, letter):
    counter = 0
    for character in word:
        if character == letter:
            counter += 1
    return counter


def filter_words(input_text, frequency):
    frequency_char, how_frequent = frequency
    output_text = ""
    words = input_text.split(" ")

    for word in words:
        if count_letter(word, frequency_char) < how_frequent:
            output_text += word + " "
    return output_text[:-1]  # unikamy spacji na końcu


# print(filter_words("Alice in wonderland went into a deep coma.", ("e", 2)))

# "Alice in wonderland went into a deep coma.", ("e", 2)
# Przykładowy rezultat działania:

# "Alice in wonderland went into a coma."
# Podpowiedź: Przeczytaj dokumentację funkcji str.split

# Zadanie 3
# Zanim zaczniesz pracę nad tym zadaniem upewnij się, że dotychczasowy kod znajduje się w repozytorium (tj. że wszystkie zmiany są zapisane - commit) Przerób funkcję z zadania 2 tak, aby jako drugi argument pobierała listę krotek litera, liczba i filtrowała wszystkie słowa, które zawierają więcej wystąpień którejkolwiek z zadanych liter zgodnie z jej zadaną częstością Przykładowe argumenty:

# "I literally can't deal with this drama right now.", [("a", 2), ("l", 3)]
# Przykładowy rezultat działania:

# "I can't deal with this right now."


def do_frequencies_comply(
    word, required_frequencies
):  # returns false if word has more letters than accepted
    word_frequencies = count_chars(word)  # słownik!

    for letter, frequency in required_frequencies:
        a = word_frequencies.get(letter, -1)

        if a != -1 and a >= frequency:  # letter exists in word and has higher feqcuency
            return False

    return True


def filter_words_multipe_frequencies(input_text, required_frequencies):
    words = input_text.split(" ")
    filtered_text = ""

    for word in words:
        if do_frequencies_comply(word, required_frequencies):
            filtered_text += word + " "

    return filtered_text[:-1]  # zeby nie zwrocic spacji na koncu


print(
    filter_words_multipe_frequencies(
        "I literally can't deal with this drama right now.", [("a", 2), ("l", 3)]
    )
)
