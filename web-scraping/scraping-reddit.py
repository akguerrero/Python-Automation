import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

def getdata(url):
    r = requests.get(url)
    return r.text

url = 'https://www.example.com'
html_data = getdata(url)
soup = BeautifulSoup(html_data, 'html.parser')
print(soup)