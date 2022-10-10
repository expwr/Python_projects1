import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="columns is-multiline")


job_elements = results.find_all("div", class_="card-content")



for job_element in job_elements:
    title_element = job_element.find(class_="title")
    company_element = job_element.find(class_="company")
    location_element = job_element.find(class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

