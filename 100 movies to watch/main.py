import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movie_titles = soup.find_all(name="h3", class_="title")

movie_names = [movie.getText() for movie in all_movie_titles]
#
# for n in range(len(movie_names) - 1, -1, -1):
#     print(movie_names[n])

# ATBBYg7Y9kx7TmAJwZraUvEXSnJzDBA2AE09

movies = movie_names[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")