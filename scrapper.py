import requests
from bs4 import BeautifulSoup

class ScraperModule:
    def __init__(self, url):
        self.url = url

    def test(self):
        print(self.url)

    def scrap_page(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        main_content = soup.find(id="wb_element_instance40")
        forecast_items = main_content.find('div')
        elemenst = forecast_items.findAll('span')
        # print(elemenst)
        