"""
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?
NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""
from typing import Dict

BASIC_WORDS = {1: "one",
               2: "two",
               3: "three",
               4: "four",
               5: "five",
               6: "six",
               7: "seven",
               8: "eight",
               9: "nine",
               10: "ten",
               11: "eleven",
               12: "twelve",
               13: "thirteen",
               15: "fifteen",
               18: "eighteen",
               20: "twenty",
               30: "thirty",
               40: "forty",
               50: "fifty",
               80: "eighty",
               }


def construct_words_for(number: int, from_dict: Dict[int, str], sep) -> str:
    integers = str(number)
    if len(integers) == 2:
        return get_two_digits(number, from_dict, sep)
    elif len(integers) == 3:
        return get_three_digits(number, from_dict, sep)
    return sep.join(["one", "thousand"])


def get_two_digits(number, words, sep=""):
    if number in words:
        return words[number]
    elif number < 20:
        first_int = number - 10
        return "".join([words[first_int], "teen"])
    first_int = int(number / 10)
    first_value = first_int * 10
    first_as_str = words.get(first_value, "".join([words[first_int], "ty"]))
    remains = number - first_value
    return sep.join([first_as_str, words[remains]]) if remains > 0 else first_as_str


def get_three_digits(number: int, words: Dict[int, str], sep: str = "") -> str:
    first_int = int(number / 100)
    remains = number - (first_int * 100)
    first_str = sep.join([words[first_int], "hundred"])
    if remains > 0:
        return sep.join([first_str, "and", get_two_digits(remains, words, sep)])
    return first_str


if __name__ == "__main__":
    long_word = ""
    for num in range(1, 1001):
        number_as_str = BASIC_WORDS.get(num, construct_words_for(num, BASIC_WORDS, sep=""))
        long_word = "".join([long_word, number_as_str])
    n_letters = len([w for w in long_word if w != ""])
    print(f"{n_letters} letters would be used if "
          "all the numbers from 1 to 1000 (one thousand) "
          "inclusive were written out in words")
