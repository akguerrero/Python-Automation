import urllib.request

url = 'https://www.example.com'

try:

    response = urllib.request.urlopen(url)

    data = response.read()

    html_content = data.decode('utf-8')

    print(html_content)
    
except Exception as e:
    print("Error fetching URL:", e)