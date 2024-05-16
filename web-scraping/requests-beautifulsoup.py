import requests # type: ignore
# from requests import get # type: ignore
from bs4 import BeautifulSoup # type: ignore

# documentation: https://beautiful-soup-4.readthedocs.io/en/latest/

# get request
# r = get('https://www.geeksforgeeks.org/python-programming-language/')
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# print response status code
print(r)

# print raw content
# print(r.content)

# print prettified html
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

# ----------------- #

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)