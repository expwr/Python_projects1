import requests
from bs4 import BeautifulSoup
from urllib import response
from requests import get


URL = "https://www.weatherbug.com/weather-forecast/10-day-weather/"
response = get(URL)
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# weathers = soup.findAll("div", attrs={"class":"cardSectionText__CardSectionDescription-sc-oi8qub-3 cGDAnA"})
weathers = soup.find_all("div")
weathers = soup.find_all(class_="styles__ForecastDataContainer-sc-zhi62y-4 iYzyIL")

for weather in weathers:
    print(weather.text)

    
