## lyrics mining
包含兩個部分`蒐集資料`及`歌詞分析`:
1. 資料集 (dataset) 來源從 [Mojim.com 魔鏡歌詞網](http://mojim.com) 爬取歌詞。`Scrapy`會負責抓取歌詞，接著透過`pipelines`會判別歌名是否重複，並將重複的歌曲(`item`)過濾(`drop`)掉，最後輸出成`csv`檔。
2. 歌詞分析是使用`jieba`及`wordcloud`做歌詞的斷字及分析（程式碼於檔案`app.py`）。

### Requirement
```
pandas
jieba
matplotlib
wordcloud
```

### Results
分析完的圖片會儲存於`LyricsAnalyse_results`.

not_cut_word_analyse.jpg
![Imgur](https://i.imgur.com/5NE7uLy.jpg)

cut_song_analyse.jpg
![Imgur](https://i.imgur.com/OZptVSi.jpg)

every_song_topK_analyse.jpg
![Imgur](https://i.imgur.com/uL9pgWE.jpg)

top100word_from_topK_analyse.jpg
![Imgur](https://i.imgur.com/BKlIUrS.jpg)