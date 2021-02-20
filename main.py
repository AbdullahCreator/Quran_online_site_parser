from bs4 import BeautifulSoup
import requests

url = 'https://quran-online.ru/'
ayat_number = url + input('Введите номер суры и аята - ')
response = requests.get(ayat_number)
soup = BeautifulSoup(response.text, "lxml")

title = soup.title
get_ayat = soup.find_all('dd', class_='ayat')
print(title.text)
print(get_ayat[6].text.strip())

