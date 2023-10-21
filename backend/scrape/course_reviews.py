import requests
import csv
import re

from bs4 import BeautifulSoup
from requests import Response
from typing import Optional, Set, Dict, List
from urllib.parse import urljoin

URL = 'https://n.ethz.ch/~lteufelbe/coursereview/all.php'
PATH = './course_reviews.csv'


class WebScrapper:
    """ Class for a webscrapper
        self.url : the url of the website
        self.response : stores the response of the request sent
        self.soup : the bs4 object
    """

    def __init__(self, url) -> None:
        self.url = url
        self.response = None
        self.soup = None

    def get_response(self) -> Response:
        """ Sends an HTTP GET request to the given URL, Return the Response
        """
        self.response = requests.get(self.url)
        return self.response if self.response.status_code == 200 else None

    def get_soup(self) -> Optional[BeautifulSoup]:
        """ Returns a BeautifulSoup object of the website if page retrieved"""
        response = self.response if self.response else self.get_response()
        if not response:
            print("error loading webpage")
            return

        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
            return self.soup
        return None

    def check_soup(self) -> Optional[BeautifulSoup]:
        soup = self.soup if self.soup else self.get_soup()
        return soup

    def get_page_title(self) -> str:
        """ Sends an HTTP GET request to the given URL and returns the
        title of the webpage.
        """
        soup = self.check_soup()
        if not soup:
            return "Failed to retrieve webpage"

        # find and extract the title tag
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.get_text()
        else:
            return "No title found on the webpage."

    def get_links(self) -> Optional[Set[str]]:
        """ Return a set of all the links that could be branched into
        from the main link"""
        soup = self.check_soup()
        if not soup:
            return
        # extract all anchor tags (links) from the page
        anchor_tags = soup.find_all('a', href=True)

        base_url = self.response.url
        full_urls = {urljoin(base_url, tag['href']) for tag in anchor_tags}

        return full_urls

    def find_class(self, class_name: str) -> bool:
        soup = self.check_soup()
        if not soup:
            return False

        if soup.find(class_=class_name):
            return True
        return False

    def find_div(self, div_id: str):
        soup = self.check_soup()
        if not soup:
            return None
        return soup.find('div', id=div_id)

    def find_ul(self, ul_id: str):
        soup = self.check_soup()
        if not soup:
            return None
        return soup.find('ul', id=ul_id)

    def find_li(self):
        soup = self.check_soup()
        if not soup:
            return None
        return soup.find_all('li')

