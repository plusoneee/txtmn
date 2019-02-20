
### Dependencies
* Python 3
### Python Requirements
```
python-dotenv
BeautifulSoup
requests
```

### Configure Settings
* Edit the file `.env.example`, and save as `.env`.
```
cp .env.example .env
vim .env
```
You can choose any `PTT board` whatever you want to crawl. `PAGE_NUMBER` is max page you need.
* For example:
```
BOARD = 'Gossiping'
PAGE_NUMBER = 10
```

### How to Run
```
python app.py
```

