
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
You can choose any `PTT board` whatever you want to crawl. `PAGE_NUMBER` is max page you need. Set the `IF_SEARCH = true`, if you want to search specific topic (or keyword). 
* For example:
```
BOARD = 'Gossiping'
PAGE_NUMBER = 100
# choose 'true' or 'false'
IF_SEARCH = 'true'
# if 'true':
KEYWORD = 'specific_word_from_BOARD'
```

### How to Run
```
python app.py
```

