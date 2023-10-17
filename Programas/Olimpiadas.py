import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://realpython.github.io/fake-jobs/")
print(response.status_code)
# print(response.content)

soup = BeautifulSoup(response.content, "html.parser")

# 200 todo bien
if response.status_code == 200:
    print(soup.head.title)
    soup = BeautifulSoup(response.content, "html.parser")
    lista_divs = soup.find_all("div", attrs={"class": "card-content"})
    # TYPE,tipo de dato     print(type(lista_div[0]))

    data = {"Role": [], "Company": [], "City": [], "Date": []}

    for div in lista_divs:

        role = div.find("h2", attrs={"class": "title is-5"})
        company = div.find("h3", attrs={"class": "subtitle is-6 company"})
        city = div.find("p", attrs={"class": "location"})
        date = div.find("time")
        data["Role"].append(role.text)
        data["Company"].append(company.text)
        data["City"].append(city.text.strip())
        data["Date"].append(date.text)

    data_fr = pd.DataFrame(data)
    data_fr.to_csv("data_olimpiadas.csv")


else:
    print(f"Error {response.status_code} al momento de cargar la pagina")