from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def print_all_quotes():
    """Prints all quotes that can be found at http://quotes.toscrape.com/"""
    page_number = 1
    while True:
        URL = f"http://quotes.toscrape.com/page/{page_number}/"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find_all("div", {"class": "quote"})
        for result in results:
            print(
                result.find("span").text,
                result.find_all("span")[1].find("small").text,
                urljoin(URL, result.find_all("span")[1].find("a")["href"]),
            )
        if page_number == 10:
            break

        page_number += 1


if __name__ == '__main__':
    print_all_quotes()
