#! NEED TO INSTALL LIBRARIES USING PIP - Beautiful Soup 4
#pip install bs4
from bs4 import BeautifulSoup
from requests import get
from urllib import response 

url = "https://mahoningctc.com/mcctc-high-school-staff"
response =  get(url)
# print(response.text[:500])


soup = BeautifulSoup(response.text, 'html.parser')
# print(type(soup))
# print(soup)
temps = soup.find_all('tr')
# print(teachers)
for item in temps:
    print(item.text)