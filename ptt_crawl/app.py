import requests
from bs4 import BeautifulSoup
from ptt import PTTclrawler, SelectSaver
from dotenv import load_dotenv
import os 
import json

def main():
    print('| * Total page number:', page_number)
    crawl = PTTclrawler(board=board)
    saver = SelectSaver()
    for i in range(0, page_number):
        datas = crawl.get_hrefs_from_page()
        s = saver.to_csv(datas)
        


if __name__ == "__main__":
    load_dotenv()
    board = os.getenv("BOARD")
    page_number =  os.getenv("PAGE_NUMBER")
    page_number = int(page_number)
    main()