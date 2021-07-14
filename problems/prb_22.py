"""
Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""
from typing import List
import requests
import string


def prepare_data(file_url: str) -> List[str]:
    content = requests.get(file_url).content.decode("utf-8")
    sorted_content_list = sorted([name.replace("\"", "") for name in content.split(",")])
    return sorted_content_list


if __name__ == "__main__":
    total = 0
    url = "https://projecteuler.net/project/resources/p022_names.txt"
    names = prepare_data(url)
    alphabet_orders = list(string.ascii_uppercase)
    for name in names:
        name_ind = names.index(name) + 1
        alphabetical_score = 0
        for letter in name:
            alphabetical_score += alphabet_orders.index(letter)+1
        total += alphabetical_score * name_ind
    print(f"The total of all the name scores in the file is {total}")
