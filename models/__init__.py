from . import product


# create table in model
# any thing added in pgadmin


# create table for scrape books model

# from odoo import fields, models, api
# import requests
# from bs4 import BeautifulSoup


# class IntegrationProduct(models.Model):
#     _name = 'integration.product'
#     _description = 'High Services Integration'
#     _inherit = 'mail.thread'

#     name = fields.Char(string="Name", required=True, tracking=True)
#     title = fields.Char(string="Title", required=True, tracking=True)
#     availability_inventory = fields.Char(
#         string="Availability_inventory", tracking=True)
#     rate = fields.Char(string="rate", tracking=True)
#     price = fields.Integer(string="Price")
#     product_id = fields.Many2one(
#         'integration.product', string='Product', required=True)

#     # Add the field for the URL with a default value


# class BookScraper:
#     def __init__(self, url):
#         self.url = url

#     def fetch_data(self):
#         # Send an HTTP request to the URL
#         response = requests.get(self.url)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Parse the HTML content of the page
#             soup = BeautifulSoup(response.content, 'html.parser')
#             return soup.find_all("article")
#         else:
#             print(
#                 f"Failed to retrieve the page. Status code: {response.status_code}")
#             return []

#     def scrape_books(self):
#         books = self.fetch_data()
#         titles_of_interest = ['Olio', 'Set Me Free', "Shakespeare's Sonnets"]
#         for book in books:
#             title = book.h3.a["title"]
#             # Check if the title is in the list of titles you are interested in
#             if title in titles_of_interest:
#                 rate = book.p["class"][1]
#                 availability = book.select_one(
#                     'div p.instock.availability').get_text(strip=True)
#                 price_element = book.find("p", class_="price_color")
#                 price = price_element.text
#                 print(
#                     f"The title: {title}\nRate: {rate} stars\n, Price: {price}\n,availability={availability}")

#                 # Create a record in IntegrationProduct
#                 integration_product_vals = {
#                     'name': title,
#                     'title': title,
#                     'availability_inventory': availability,
#                     'rate': rate,
#                     'price': price,
#                 }


# # Usage
# url_to_scrape = 'https://books.toscrape.com/'
# book_scraper = BookScraper(url_to_scrape)
# book_scraper.scrape_books()


# book_data = []
# book_data.append(
#     {"title": title, "rate": rate, "availability": availability, "price": price})

# return book_data
