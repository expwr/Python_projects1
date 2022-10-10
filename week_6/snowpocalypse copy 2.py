import requests
from bs4 import BeautifulSoup

temp = []
new_temps = []

url = "https://weather.com/weather/tenday/l/08bd50a1176f54984872ff805fdff0dff19c2d1543f8aa72dc2f88ccd6c538d9"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

temps = soup.find_all("div", {"class": "DetailsSummary--temperature--1Syw3"})


for item in temps:
    temp.append(item.text)

for i in range(len(temp)):
    new_temps.append(temp[i].split("/"))

for i in range(len(new_temps)):
    new_temps[i][0] = new_temps[i][0].split("°")
    new_temps[i][1] = new_temps[i][1].split("°")

print(new_temps)




print(new_temps[0][1][0])