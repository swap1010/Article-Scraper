import requests
from bs4 import BeautifulSoup
import os
import string
n = int(input())
types = input()
for i in range(1, n + 1):
    url = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={i}"
    req = requests.get(url).content
    soup = BeautifulSoup(req, "html.parser")
    os.mkdir(os.path.join(os.getcwd(), f"page_{i}"))
    for article in soup.find_all("article"):
        article_type = article.find_all("span", attrs={'data-test': "article.type"})[0].span.contents[0]
        if types == article_type:
            article_heading = article.find_all("a", attrs={"data-track-action": "view article"})[0].contents[0].replace(",", "")
            for ch in string.punctuation:
                article_heading = article_heading.replace(ch, "")
            file_name = "_".join(article_heading.split()) + ".txt"
            article_url = "https://www.nature.com" + \
                          article.find_all("a", attrs={"data-track-action": "view article"})[
                              0].get("href")
            cont = requests.get(article_url).content
            soup2 = BeautifulSoup(cont, "html.parser")
            content = soup2.find("div", class_="article-item__body").text
            with open(os.path.join(os.getcwd(), f"page_{i}", file_name), "w", encoding="UTF-8") as file:
                    file.write(content)
