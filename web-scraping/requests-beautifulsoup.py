import requests # type: ignore
# from requests import get # type: ignore
from bs4 import BeautifulSoup # type: ignore

# get request
# r = get('https://www.geeksforgeeks.org/python-programming-language/')
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# print response status code
print(r)

# print raw content
# print(r.content)

# print prettified html
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify)