import requests
from bs4 import BeautifulSoup

rp4b4GB = requests.get("https://rpishop.cz/startovaci-sady/5071-1067-sada-s-raspberry-pi-4b-cooler-master-v2-32gb"
                       "-microsd-prislusenstvi-0784862387621.html#/212-velikost_ram-4_gb")

rp4b8GB = requests.get("https://rpishop.cz/startovaci-sady/5071-1068-sada-s-raspberry-pi-4b-cooler-master-v2-32gb"
                       "-microsd-prislusenstvi-0784862387621.html#/213-velikost_ram-8_gb")


if rp4b4GB.status_code == 200:
    soup_of_4b4GB = BeautifulSoup(rp4b4GB.content, "html.parser")

    find_4gb_price = soup_of_4b4GB.find("div", class_="current-price")
    content_of_price_div4b4GB = find_4gb_price.find("span")
    price_4b4GB = content_of_price_div4b4GB.get_text()
    print(f"Raspberry Pi 4B 4GB: {price_4b4GB}")
    find_4gb_availability = soup_of_4b4GB.find("div", id="product-availability")
    content_of_availability_div4b4GB = find_4gb_availability.find("p")
    unwanted = content_of_availability_div4b4GB.find("i")
    unwanted.extract()
    availability = content_of_availability_div4b4GB.get_text().strip()
    print(availability + "\n")
else:
    print(f"Error: {rp4b4GB.status_code}")


if rp4b8GB.status_code == 200:
    soup_of_4b8GB = BeautifulSoup(rp4b8GB.content, "html.parser")

    find_8gb_price = soup_of_4b8GB.find("div", class_="current-price")
    content_of_price_div4b8GB = find_8gb_price.find("span")
    price_4b8GB = content_of_price_div4b8GB.get_text()
    print(f"Raspberry Pi 4B 8GB: {price_4b8GB}")
    find_8gb_availability = soup_of_4b8GB.find("div", id="product-availability")
    content_of_availability_div4b8GB = find_8gb_availability.find("p")
    unwanted = content_of_availability_div4b8GB.find("i")
    unwanted.extract()
    availability = content_of_availability_div4b8GB.get_text().strip()
    print(availability + "\n")
else:
    print(f"Error: {rp4b8GB.status_code}")