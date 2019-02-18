import requests
from bs4 import BeautifulSoup
from ptt import PTTclrawler
from dotenv import load_dotenv
import os 

def main():
    print('| * Total page number:', page_number)
    crawl = PTTclrawler(board=board)
    for i in range(0, page_number):
        datas = crawl.get_hrefs_from_page()
        print('| * Artical Number:', len(datas))

if __name__ == "__main__":
    load_dotenv()
    board = os.getenv("BOARD")
    page_number =  os.getenv("PAGE_NUMBER")
    page_number = int(page_number)
    main()