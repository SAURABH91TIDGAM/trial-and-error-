import requests
import bs4
import datetime

URL = "https://www.billboard.com/charts/hot-100/"

date = input("which year do you want to travel to? Type date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/"+date)
website_html = response.text

soup = bs4.BeautifulSoup(website_html, "html.parser")

track_names = soup.select("li ul li h3")
artist_names  = soup.select("li ul li span")

song_names = [song.getText().strip() for song in track_names]
artists = [artist.getText().strip() for artist in artist_names]
print(song_names)
print(artists)