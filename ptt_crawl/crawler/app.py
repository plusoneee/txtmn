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

    def search_all():
        for i in range(0, page_number):
            datas = crawl.get_hrefs_from_page()
            s = saver.to_csv(datas, save_file_path)

    def select_from_key():
        for i in range(0, page_number):
            datas = crawl.search_from_keyword(keyword)
            s = saver.to_csv(datas, save_file_path)
    print(if_search)
    if if_search == 'true': select_from_key()
    elif if_search == 'false': search_all()
    else: print('please check `IF_SEARCH` of .env file')
        
if __name__ == "__main__":
    load_dotenv()
    board = os.getenv("BOARD")
    keyword = os.getenv("KEYWORD")
    save_file_path = os.getenv("FILE_PATH_NAME")
    page_number =  os.getenv("PAGE_NUMBER")
    if_search =  os.getenv("IF_SEARCH")
    page_number = int(page_number)
    main()