import re
from urllib.parse import urlparse
from loguru import logger 

class CrawlerDispatcher:
    def __init__(self) -> None:
        """Tracks crawlers"""
        self.crawlers = {}

    @classmethod
    def build(cls) -> "CrawlerDispatcher":
        """Build method for Builder pattern"""
        dispatcher = cls
        return dispatcher
    
    