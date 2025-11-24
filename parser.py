import requests
from bs4 import BeautifulSoup
import pandas as pd




travel_books = []
url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
response = requests.get(url)


html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
books = soup.find_all("article", class_ = 'product_pod')


for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_ = 'price_color').text
    rating = book.p['class'][-1]
    #print(f'Name: {title}, price: {price}, rating: {rating}')
    travel_books.append({
        'Title': title,
        'Price': price,
        'Rating': rating
    })


df = pd.DataFrame(travel_books)

df.to_csv("travel_books.csv", index=False)

print('Sucsesful')