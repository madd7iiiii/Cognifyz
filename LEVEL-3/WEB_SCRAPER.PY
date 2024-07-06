import requests
from bs4 import BeautifulSoup

def scrape_quotes():
   
    url = 'http://quotes.toscrape.com'
    response = requests.get(url)

    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = []
        authors = []

        for quote in soup.find_all('span', class_='text'):
            quotes.append(quote.get_text())

        for author in soup.find_all('small', class_='author'):
            authors.append(author.get_text())

        
        for i in range(len(quotes)):
            print(f"Quote: {quotes[i]}")
            print(f"Author: {authors[i]}")
            print()

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_quotes()
