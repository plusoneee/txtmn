import pandas as pd
import jieba.analyse
jieba.set_dictionary("dict.txt.big")
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os 

class LyricsAnalyse():
    def __init__(self, stopwords_list, file_path="hebe_lyrics.csv"):
        self.stopwords = {}.fromkeys(stopwords_list)
        self.songs = pd.read_csv(file_path)
        # LyricsAnalyse_results/ 圖片存放目錄 
        if not os.path.isfile('./LyricsAnalyse_results/'):
            os.makedirs('./LyricsAnalyse_results/', exist_ok=True)
        self.img_save_folder = './LyricsAnalyse_results/'

    def read_lyrics_content_from_csv(self, file_path="hebe_lyrics.csv"):
        print(':::: Lyrics content processing')
        contents_list = self.songs['content']
        contents = ' '.join(contents_list) # list -> str
        return contents

    def analyse_and_extract_tags(self, sentence, topK=10):
        print(':::: Cut word and extracttags by jieba')
        datas = ''
        for word in sentence:
            tags = jieba.analyse.extract_tags(sentence, topK)
            datas += ','.join(tags)
        return datas

    def cut_word_from_jieba(self, contents, save_cutword_txt=False):
        segs = jieba.cut(contents, cut_all=False)
        seg_list = list(filter(lambda i: i != ' ', segs)) # delete ' ' from segs and save as list type.
        seg_contents = ' '.join(seg_list)
        if save_cutword_txt:
            with open('./after_cut_txt.text') as f:
                f.write(seg_contents)
        return seg_contents

    def wordcloud_setting(self, result_data):
        print(':::: Word cloud settings and generate')
        wc = WordCloud(font_path="NotoSerifCJKtc-hinted/NotoSerifCJKtc-Black.otf", # set font 
                background_color="white", # background color
                max_words = 1000, # word cloud max wordsnumbers
                width=1920, # picture width
                collocations = False,
                height=1080,
                stopwords=self.stopwords
                )
        return wc.generate(result_data)

    def save_photo(self, wc, save_filename):
        wc.to_file(self.img_save_folder + save_filename)
        print(':::: Save image finishe!')

    def read_file_get_every_song_topK(self, file_path="hebe_lyrics.csv", k=10):
        print(":::: Read file and get every song top K word")
        contents = self.songs['content']
        datas = ''
        for contant in contents:
            tags = jieba.analyse.extract_tags(contant, k)
            datas += " ".join(tags)
        return datas

    def not_cut_word_analyse(self):
        # 讀取原檔案未斷詞
        not_wordcut_sentence = self.read_lyrics_content_from_csv()
        wc = self.wordcloud_setting(result_data=not_wordcut_sentence)
        self.save_photo(wc, 'not_cut_word_analyse.jpg')

    def cut_song_analyse(self):
        # 讀取原檔案且歌詞進行jieba斷詞
        not_wordcut_sentence = self.read_lyrics_content_from_csv()
        seg_contents = self.cut_word_from_jieba(not_wordcut_sentence)
        wc = self.wordcloud_setting(result_data=seg_contents)
        self.save_photo(wc, 'cut_song_analyse.jpg')

    def every_song_topK_analyse(self):
        # 讀取每首歌的十大關鍵字
        get_topK_sentence = self.read_file_get_every_song_topK(k=10)
        wc = self.wordcloud_setting(result_data=get_topK_sentence)
        self.save_photo(wc, 'every_song_topK_analyse.jpg')

    def top100word_from_topK_analyse(self):
        # 從每一首歌的十大關鍵字中再取出100個
        get_topK_sentence = self.read_file_get_every_song_topK(k=10)
        to200_sentence = self.analyse_and_extract_tags(get_topK_sentence, topK=100)
        wc = self.wordcloud_setting(result_data=get_topK_sentence)
        self.save_photo(wc, 'top100word_from_topK_analyse.jpg')

key = ["一個", "一個", "這樣", "怎麼", "什麼", "Wu", "La", "la", "ah", "oh", "LaLa", "ahLa", "瑪麗"]
anlyse = LyricsAnalyse(stopwords_list=key, file_path='hebe_lyrics.csv')
anlyse.top100word_from_topK_analyse()
anlyse.every_song_topK_analyse()
anlyse.cut_song_analyse()
anlyse.not_cut_word_analyse()
