import csv
from bs4 import BeautifulSoup
import requests

url_base = 'https://www.gutenberg.org/ebooks/bookshelf/'
output_file = 'books_data.csv'

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Author', 'Category'])

    for i in range(425, 487):
        url = url_base + str(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        books = soup.find_all('li', class_="booklink")
        category = soup.find('h1').text.split(":")[1].split("(")[0].strip()

        for book in books:
            try:
                title = book.find('span', class_='title').text.strip()
                author = book.find('span', class_='subtitle').text.strip()
            except AttributeError:
                author = 'Unregistered'

            writer.writerow([title, author, category])

print(f"Data successfully saved to {output_file}")
