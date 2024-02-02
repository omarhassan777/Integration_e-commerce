from odoo import fields, models, api
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Import urljoin from urllib.parse
import base64


class IntegrationProduct(models.Model):
    _name = 'integration.product'
    _description = 'High Services Integration'
    _inherit = 'mail.thread'

   # _rec_name="name"

    name = fields.Char(string="Name", tracking=True)
    title = fields.Char(string="Title", tracking=True)
    availability_inventory = fields.Char(
        string="Availability_inventory", tracking=True)
    rate = fields.Char(string="Rate", tracking=True)
    price = fields.Char(string="Price")
    discount = fields.Char(string="discount")
    product_id = fields.Integer(string='product_id')
    image = fields.Binary(string="Image")
    cv = fields.Html()
    adress = fields.Text(string="Adress")

    list_books = fields.Selection(selection=[], string="List Book")

    #    max_length=max(my_list), string="List Book")

    # book_id = fields.Many2one(
    #     'integration.product', string='Book', required=True)

    @api.onchange('name')
    def _onchange_from_api(self):
        url = 'https://books.toscrape.com/'
        # Send an HTTP request to the URL
        response = requests.get('https://books.toscrape.com/')

        # Check if the request was successful (status code 200)
        if response.status_code == 200:

            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            # Example selector for articles
            books = soup.find_all("article")
            # titles_of_interest = [
            #     'Olio', 'Set Me Free', "Shakespeare's Sonnets","It's Only the Himalayas"]

            # to work list menu
            # Update the choices for the list_books field

            for book in books:
                title = book.h3.a.get("title")

                # Check if the title is in the list of titles you are interested in

                if self.name == title:
                    self.title = book.h3.a.get("title")

                    base_url = 'https://books.toscrape.com/'
                    image_url = urljoin(base_url, book.a.img.get("src"))
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        self.image = base64.b64encode(
                            image_response.content)

                    else:
                        print(
                            f"Failed to retrieve image. Status code: {image_response.status_code}")

                    rate = book.p["class"][1]
                    availability_element = book.select_one(
                        'div p.instock.availability')
                    availability_inventory = availability_element.get_text(
                        strip=True) if availability_element else ''

                    price_element = book.find("p", class_="price_color")
                    price = price_element.text
                    # discount = price

                    print(
                        f"The title: {self.name}\nRate: {rate} stars\nPrice: {price}\nAvailability: {availability_inventory}")

                    # Update fields in the Odoo record
                    self.title = self.title
                    self.rate = rate
                    self.availability_inventory = availability_inventory
                    self.price = str(price)
                    # self.discount = str(discount)
                    # Return updated field values
                    # return {'value':
                    #
                    # self.price = int(price.replace('£', '').replace('.', ''))

        else:
            print(
                f"Failed to retrieve the page. Status code: {response.status_code}")

    def open_web_page(self):
        # Define the URL you want to open
        web_page_url = 'https://books.toscrape.com/'

        # Open the URL in a new browser window
        return {
            'type': 'ir.actions.act_url',
            'url': web_page_url,
            'target': 'new',
        }

    def action_open_inventory(self):
        # Define the URL of the inventory module
        inventory_url = 'http://localhost:8868/web?db=odoo_tur#action=379&model=product.template&view_type=kanban&cids=1&menu_id=213'

        # Return the action to open the URL in a new window
        return {
            'type': 'ir.actions.act_url',
            'url': inventory_url,
            'target': 'new',
        }


# class Books(models.Model):
#     _name = 'library.book'
#     _description = 'Library Book'
#     _inherit = 'integration.product'
#     name_book = fields.Char(string='Book Name')
#     # Add other fields related to a book
# # Usage
# book_info_list = []
# # Fetch book information
# print("abdo =", book_info_list)
# list_globel = []
# book_info_list.append(IntegrationProduct.scrape_books())
