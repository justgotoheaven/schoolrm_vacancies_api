from requests import Session
from bs4 import BeautifulSoup


class BaseParser:

    def __init__(self):
        self.session = Session()
        self.soup = BeautifulSoup()

    @staticmethod
    def get_soup(content):
        return BeautifulSoup(content, 'lxml')
