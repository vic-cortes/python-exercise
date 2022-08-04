from dataclasses import dataclass

import requests
from lxml import etree
from bs4 import BeautifulSoup


@dataclass
class Webpage:
    webpage_url: str

    def __post_init__(self) -> None:
        self._soup = None
        self._dom  = None

    @property
    def content_available(self) -> bool:
        response = requests.get(self.webpage_url)

        if not response.ok:
            return False

        self._soup = BeautifulSoup(response.content)
        self._dom  = etree.HTML(response.content)

        return True

    @property
    def title(self):
        return self._soup.title

    @property
    def description(self):
        return self._soup.find("meta", {"name": "description"})
    
    @property
    def favicon(self):
        FAVICON_XPATH = "//link[contains(@href, 'favicon')]"

        if not (fav_element := self._dom.xpath(FAVICON_XPATH)): 
            return "Not Available"

        # Converts node to html string
        return etree.tostring(fav_element[0]).decode("ascii")

    def metadata(self):
        return {
            "title_tag": self.title,
            "favicon_tag": self.favicon,
            "description_tag": self.description,
        }

    @classmethod
    def get_metadata(cls, webpage_url: str) -> dict:
        webpage = cls(webpage_url=webpage_url)

        if not webpage.content_available:
            return

        return webpage.metadata()