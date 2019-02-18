import requests
from bs4 import BeautifulSoup

class PTTclrawler():
    def __init__(self, board='Gossiping'):
        print('| * 爬取看板:', board)
        self.now_page = 1
        self.r = requests.session()
        self.board = board
        if self.board == 'Gossiping': 
            payload = {'form':'/bbs/Gossiping/index.html', 'yes':'yes'}
            res = self.r.post('https://www.ptt.cc/ask/over18', data = payload)
        self.url = 'https://www.ptt.cc/bbs/'+ board + '/index.html'
        
    def get_hrefs_from_page(self):
        while True:
            self.datas = []
            print('| * Page Number ', self.now_page)
            res = self.r.get(self.url)
            soup = BeautifulSoup(res.text, "lxml")
            results = soup.select("div.title")
            up_page_href = soup.select("div.btn-group a")[3].get('href')
            self.url = 'https://www.ptt.cc' + up_page_href
            for item in results:
                a_item = item.select_one("a")
                title = item.text
                if a_item:
                    url = 'https://www.ptt.cc'+ a_item.get('href')
                    row = self.crawl_data_from_article(url)
                    self.datas.append(row)
            self.now_page= self.now_page + 1
    
            return self.datas

    def crawl_data_from_article(self, url):
        res = self.r.get(url)
        push_list = []
        soup = BeautifulSoup(res.text, "lxml")
        results = soup.select('span.article-meta-value')
        pushs = soup.select('div.push')
        for push in pushs:
            try:
                push_list.append({
                     'push-tag':push.select_one('span.push-tag').text,
                     'push-userid':push.select_one('span.push-userid').text,
                     'push-content':push.select_one('span.push-content').text,
                     'push-ipdatetime':push.select_one('span.push-ipdatetime').text
                })
            except: pass

        if results and len(results)>3:
            item = {
                'author': results[0].text,
                'board': results[1].text,
                'title': results[2].text,
                'time': results[3].text,
                'pushs': push_list,
            }
            return item

