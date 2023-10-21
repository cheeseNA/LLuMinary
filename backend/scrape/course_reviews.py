import csv
import pprint
import re
import time
from typing import Dict, List, Optional, Set
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from requests import Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = "https://n.ethz.ch/~lteufelbe/coursereview/all.php"
PATH = "./course_reviews.csv"


class WebScrapper:
    """Class for a webscrapper
    self.url : the url of the website
    self.response : stores the response of the request sent
    self.soup : the bs4 object
    """

    def __init__(self, url) -> None:
        self.url = url
        self.response = None
        self.soup = None
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--incognito")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def get_response(self):
        """Sends an HTTP GET request to the given URL, Return the page_source"""
        self.driver.get(self.url)
        time.sleep(2)
        self.response = self.driver.page_source.encode("utf-8")
        return self.response

    def get_soup(self) -> Optional[BeautifulSoup]:
        """Returns a BeautifulSoup object of the website if page retrieved"""
        response = self.response if self.response else self.get_response()
        if not response:
            print("error loading webpage")
            return

        self.soup = BeautifulSoup(response, "html.parser")
        return self.soup

    def check_soup(self) -> Optional[BeautifulSoup]:
        soup = self.soup if self.soup else self.get_soup()
        return soup

    def get_page_title(self) -> str:
        """Sends an HTTP GET request to the given URL and returns the
        title of the webpage.
        """
        soup = self.check_soup()
        if not soup:
            return "Failed to retrieve webpage"

        # find and extract the title tag
        title_tag = soup.find("title")
        if title_tag:
            return title_tag.get_text()
        else:
            return "No title found on the webpage."

    def get_course_dict(self) -> Dict[str, str]:
        """Returns a list of all the course urls on the webpage"""
        soup = self.check_soup()
        if not soup:
            raise Exception("Failed to retrieve webpage")

        ul = soup.find("ul", id="all")
        # get all the li tags
        li_tags = ul.find_all("li")
        dicts = {
            li_tags[i].find("a").get_text(): li_tags[i].find("a")["href"]
            for i in range(len(li_tags))
        }
        return dicts

    def get_links(self) -> Optional[Set[str]]:
        """Return a set of all the links that could be branched into
        from the main link"""
        soup = self.check_soup()
        if not soup:
            return
        # extract all anchor tags (links) from the page
        anchor_tags = soup.find_all("a", href=True)

        base_url = self.response.url
        full_urls = {urljoin(base_url, tag["href"]) for tag in anchor_tags}

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
        return soup.find("div", id=div_id)

    def find_ul(self, ul_id: str):
        soup = self.check_soup()
        if not soup:
            return None
        return soup.find("ul", id=ul_id)

    def find_li(self):
        soup = self.check_soup()
        if not soup:
            return None
        return soup.find_all("li")


if __name__ == "__main__":
    webscraper = WebScrapper(URL)
    pprint.pprint(webscraper.get_course_dict())
