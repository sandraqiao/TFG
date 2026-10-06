from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import datetime as dt
from decimal import Decimal
from selenium.webdriver.common.by import By
from utils import constants

def get_soup(isbn: str | None = None, url: str | None = None):
    # service = Service("drivers/chromedriver-win64/chromedriver.exe")
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Chrome()

    try:
        if not url and isbn:
            driver.get(f"https://www.casadellibro.com/?query={isbn}")

            root = driver.find_element(By.CSS_SELECTOR, ".x-root-container")
            html = driver.execute_script("return arguments[0].shadowRoot.innerHTML", root)
            soup = BeautifulSoup(html, 'html.parser')

            url = extract_url(soup)

        if url is None:
            return None, None

        driver.get(url)

        html = driver.page_source
        return BeautifulSoup(html, 'html.parser'), url
    
    finally:
        driver.quit()

def extract_data_precios(soup: str) -> dict:
    libro_soup = soup.find_all("script", type="application/ld+json")
    libro_json = json.loads(libro_soup[0].string)

    datos = {
        "precio": get_precio(soup),
        "pct_descuento": get_pct_descuento(soup),
        "fecha_consulta": dt.date.today(),
        "disponible": get_disponible(libro_json),
        "tienda": constants.TIENDA_SCRAPER[0]
    }
    return datos

def extract_ficha_tecnica(soup: str) -> dict[str, str]:
    ficha = soup.select_one(".ficha-tecnica")
    data = {}

    if ficha:
        for campo in ficha.select(".campo[data-campo]"):
            nombre = campo.get("data-campo")
            texto = campo.get_text(" ",strip=True)

            if nombre:
                data[nombre] = texto

    return data

# ===============================================================================================================

def extract_url(soup):
    resultado = soup.find("a", attrs={"data-test": "result-link"})
    return resultado.get("href") if resultado else None

def get_titulo(soup):
    titulo = soup.find("h1", id="t-p-f")
    return titulo.get_text(strip=True) if titulo else None

def get_autores(soup):
    autores = []

    escritores = soup.find_all("h3", class_="text-l f-w-7 mb-2 brand-text")
    for escritor in escritores:
        texto = escritor.get_text(strip=True)
        if texto.startswith("Escrito por "):
            autores.append(texto.replace("Escrito por", "", 1).strip())

    return autores

def get_precio(soup):
    precio = soup.find("span", id="p-pf-f")

    if precio is None:
        raise ValueError("Precio no encontrado.")

    precio = precio.get_text(strip=True)
    precio = precio.replace("€", "").replace(",", ".")

    return Decimal(precio)

def get_pct_descuento(soup):
    text = soup.find(string=lambda texto: texto and "de dto. exclusivo web" in texto)

    if text is None:
        return None

    descuento = text[(text.find("-")+1):(text.find("%"))]
    return Decimal(descuento)

def get_disponible(json):
    disponible = json[1]["workExample"][0]["offers"][0]["availability"]

    if not disponible:
        raise ValueError("Disponibilidad no encontrada.")

    if "InStock" in disponible:
        return True
    if "OutOfStock" in disponible:
        return False

    raise ValueError("Disponibilidad con datos inesperados.")




# ===============================================================================================================
# ===============================================================================================================

# def get_soup(isbn: str):
#     # service = Service("drivers/chromedriver-win64/chromedriver.exe")
#     # driver = webdriver.Chrome(service=service)
#     driver = webdriver.Chrome()

#     try:
#         driver.get(f"https://www.casadellibro.com/?query={isbn}")
    
#         root = driver.find_element(By.CSS_SELECTOR, ".x-root-container")
#         html = driver.execute_script("return arguments[0].shadowRoot.innerHTML", root)
#         return BeautifulSoup(html, 'html.parser')
#     finally:
#         driver.quit()

# def extract_precio_data(url: str):

#     # service = Service("drivers/chromedriver-win64/chromedriver.exe")
#     # driver = webdriver.Chrome(service=service)
#     driver = webdriver.Chrome()

#     driver.get(url)
#     html = driver.page_source
#     driver.quit()

#     full_soup = BeautifulSoup(html, 'html.parser')
#     libro_soup = full_soup.find_all("script", type="application/ld+json")
#     libro_json = json.loads(libro_soup[0].string)

#     datos = {
#         # "precio": get_precio(libro_json),
#         "precio": get_precio(full_soup),
#         "pct_descuento": get_pct_descuento(full_soup),
#         "fecha_consulta": dt.date.today(),
#         "disponible": get_disponible(libro_json),
#         "tienda": constants.TIENDA_SCRAPER[0]
#     }

#     return datos

# def extract_ficha_tecnica(soup: str) -> dict[str, str]:
#     ficha = soup.select_one(".ficha-tecnica")

#     if not ficha:
#         return {}
#     data = {}
#     for campo in ficha.select(".campo[data-campo]"):
#         nombre = campo.get("data-campo")
#         texto = campo.get_text(" ", strip=True)
#         if nombre:
#             data[nombre] = texto

#     return data

# # ===============================================================================================================

# def extract_url(soup: str):
#     resultado = soup.find("a", attrs={"data-test": "result-link"})
#     if resultado is None:
#         return None
#     return resultado.get("href")

# def get_pct_descuento(soup):
#     text = soup.find(string=lambda texto: texto and "de dto. exclusivo web" in texto)

#     if text is not None:
#         descuento = text[(text.find("-")+1):(text.find("%"))]
#         return Decimal(descuento)

#     return None

# def get_precio(soup):
#     precio = soup.find("span", id="p-pf-f")

#     if precio is None:
#         raise ValueError("Precio no encontrado.")

#     precio = precio.get_text(strip=True)
#     precio = precio.replace("€", "").replace(",", ".")

#     return Decimal(precio)

# def get_disponible(libro_json):
#     disponible = libro_json[1]["workExample"][0]["offers"][0]["availability"]

#     if disponible and "InStock" in disponible:
#         return True

#     if disponible and "OutOfStock" in disponible:
#         return False

#     raise ValueError("Disponibilidad no encontrada.")