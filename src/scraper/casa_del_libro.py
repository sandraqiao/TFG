from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import datetime as dt
from decimal import Decimal

def extract_data(url: str):

    service = Service("drivers/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(url)
    html = driver.page_source
    driver.quit()

    full_soup = BeautifulSoup(html, 'html.parser')
    libro_soup = full_soup.find_all("script", type="application/ld+json")
    libro_json = json.loads(libro_soup[0].string)

    datos = {
        "precio": get_precio(libro_json),
        "pct_descuento": get_pct_descuento(full_soup),
        "fecha_consulta": dt.date.today(),
        "disponible": get_disponible(libro_json)
    }

    return datos

def get_pct_descuento(soup):
    text = soup.find(string=lambda texto: texto and "de dto. exclusivo web" in texto)

    if text is not None:
        descuento = text[(text.find("-")+1):(text.find("%"))]

    return descuento

def get_precio(libro_json):
    precio = libro_json[1]["workExample"][0]["offers"][0]["Price"]

    if precio is None:
        raise ValueError("Precio no encontrado.")

    return Decimal(precio)

def get_disponible(libro_json):
    disponible = libro_json[1]["workExample"][0]["offers"][0]["availability"]

    if disponible and "InStock" in disponible:
        return True

    if disponible and "OutOfStock" in disponible:
        return False

    raise ValueError("Disponibilidad no encontrada.")

# def get_url(libro_json):
#     url = libro_json[1]["@id"]

#     if url is None:
#         raise ValueError("URL no encontrada.")

#     return url