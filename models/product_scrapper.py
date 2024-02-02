# # Import necessary modules
# from odoo import models, fields, api
# import requests
# from bs4 import BeautifulSoup


# class BookScrapper(models.Model):
#     _name = 'book.scrapper'
#     _description = 'Book Scrapper'

#     name = fields.Char(string='Book Scrapper', required=True)
#     books = fields.One2many('book.scrapper.book',
#                             'scrapper_id', string='Books')

#     def scrape_books_and_create_records(self):
#         # URL of the website to scrape
#         url = 'https://books.toscrape.com/'

#         # Send an HTTP request to the URL
#         response = requests.get(url)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.content, 'html.parser')

#             # Extract information for each book
#             for book in soup.find_all('article', class_='product_pod'):
#                 title = book.h3.a['title']
#                 rating = book.p['class'][1]
#                 price = book.select_one(
#                     'div p.price_color').get_text(strip=True)
#                 availability = book.select_one(
#                     'div p.instock.availability').get_text(strip=True)

#                 # Create a record in the Odoo model
#                 self.books.create({
#                     'title': title,
#                     'rating': rating,
#                     'price': price,
#                     'availability': availability,
#                 })
#         else:
#             print(
#                 f"Failed to retrieve the page. Status code: {response.status_code}")


# class BookScrapperBook(models.Model):
#     _name = 'book.scrapper.book'
#     _description = 'Book Scrapper Book'

#     title = fields.Char(string='Title', required=True)
#     rating = fields.Char(string='Rating')
#     price = fields.Char(string='Price')
#     availability = fields.Char(string='Availability')
#     scrapper_id = fields.Many2one('book.scrapper', string='Book Scrapper')

# # Usage:
# # - Create a new record in the 'book.scrapper' model
# # - Call the 'scrape_books_and_create_records' method on the created record
# # - View the results in the 'book.scrapper.book' model
