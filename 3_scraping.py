from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL = "http://quotes.toscrape.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("div", {"class": "quote"})

# print(
#     results[0].find("span").text,
#     results[0].find_all("span")[1].find("small").text,
#     URL + results[0].find_all("span")[1].find("a")["href"],
# )

for result in results:
    print(
        result.find("span").text,
        result.find_all("span")[1].find("small").text,
        urljoin(URL, result.find_all("span")[1].find("a")["href"]),
    )
