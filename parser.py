import requests


url = 'https://books.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    print('ok')
else:
    print(f'no ok {response.status_code}')