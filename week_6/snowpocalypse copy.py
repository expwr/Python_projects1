import requests
from bs4 import BeautifulSoup

temp = []
high = []
low = []

url = "https://www.wunderground.com/forecast/us/oh/canfield/44406"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

high_temps = soup.find("span", {"class": "temp-hi"})

low_temps = soup.find("span", {"class": "temp-lo"})


print(soup.find("span", {"class": "temp-lo"}))


