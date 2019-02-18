import requests
from bs4 import BeautifulSoup
from ptt import PTTclrawler
from dotenv import load_dotenv
import os 
load_dotenv()
board = os.getenv("BOARD")
page_number =  os.getenv("PAGE_NUMBER")
crawl = PTTclrawler(board=board, page=page_number)
crawl.get_hrefs_from_page()