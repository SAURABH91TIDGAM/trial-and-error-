import codecs

from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.name)
print(soup.title.string)
print(soup.prettify())
print(soup.a)
print(soup.li.string)

all_anchor_tags = soup.find_all(name="a")
print()

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

h3_heading = soup.find_all("h3", class_="heading")
print(h3_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

headings = soup.select(".heading")
print(headings)