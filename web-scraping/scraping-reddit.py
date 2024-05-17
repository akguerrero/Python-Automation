import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

def getdata(url):
    r = requests.get(url)
    return r.text

url = 'https://www.reddit.com/r/learnpython/comments/78qnze/web_scraping_in_20_lines_of_code_with/'
html_data = getdata(url)
soup = BeautifulSoup(html_data, 'html.parser')
print(soup)