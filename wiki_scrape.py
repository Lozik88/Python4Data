import requests as r
from bs4 import BeautifulSoup as b
import pandas as pd
import sql_connect as connection
cnxn = connection.cnxn()
cursor = cnxn.cursor()

df = pd.DataFrame()

url_str = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
website_url = r.get(url_str).text
soup = b(website_url,'lxml')
# print(soup.prettify())
my_table = soup.find("table",{"class":"wikitable sortable"}) #Why can't I use full class name?
links = my_table.find_all("a")
td = my_table.find_all("td")

countries = []
for link in links:
    countries.append(link.get("title"))



df["Countries"] = countries

for country in countries:
    print(country)