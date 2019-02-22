import pandas as pd
import json
import demjson
import jieba
import ast
import re

def read_data(path='../datasets/ptt.csv'):
    print('| * read file: ../datasets/ptt.csv')
    headers_name = ["author", "board", "title", "time", "url", "content", "pushs", "push_number"]
    return pd.read_csv(path, names = ["author", "board", "title", "time", "url", "content", "pushs", "push_number"] )    

def pushs_to_dict(d):
    pushs = []
    print('| * only get pushs content and turn to dictionary format')
    for every_artical_pushs in d['pushs'][:]:
        pushs.append(demjson.decode(every_artical_pushs))
    print(pushs)
    return pushs

def comments_classification_by_pushtag(pushs):
    print('|* Starting classifiy data by push-tag')
    humming_comments = []
    promote_comments = []
    for article in pushs:
        for item in article:
            if item['push-tag'].find('噓')!=-1:
                #print('sh')
                humming_comments.append(item['push-content'].replace(' ','')[1:]) # 0index=':'
            elif item['push-tag'].find('推')!=-1:
                #print('push')
                 promote_comments.append(item['push-content'].replace(' ','')[1:]) # 0index=':'
   # print(humming_comments, promote_comments)
    with open('./checkpoint_txt_results/humming_comments.txt', 'w+') as f:
        humming_comments = str(humming_comments)
        f.write(humming_comments)
    with open('./checkpoint_txt_results/promote_comments.txt', 'w+') as f:
        promote_comments = str(promote_comments)
        f.write(promote_comments)

# 分別讀取推(p)與噓(h)評論的list 
def read_coments_file():
    print('| * Read comment list file')
    with open('./checkpoint_txt_results/promote_comments.txt') as f:
        # Convert string representation of list to list
        p = ast.literal_eval(f.read()) 
    with open('./checkpoint_txt_results/humming_comments.txt') as f:
    # Convert string representation of list to list
        h = ast.literal_eval(f.read()) 
    return p, h

# 分別建立兩個斷詞後的list(p_segs, h_segs)
def split_comments_to_seg(p, h):
    print('| * Split humming_comments and promote_comments 2segs list')
    p_segs = []
    h_segs = []
    r1 = '[a-zA-Z0-9’!#$%&()*.+？！[\\]^_`{|}~]+'
    # jieba.load_userdict("./userdict.txt")
    for sentence in p:
        sentence = re.sub(r1, '', sentence)
        p_segs += list(jieba.cut(sentence, cut_all=False))
    for sentence in h:
        sentence = re.sub(r1, '', sentence)
        h_segs += list(jieba.cut(sentence, cut_all=False))
    # merge p_segs and h_segs for build dictionary
    all_segs = list(set(p_segs + h_segs))
    return p_segs, h_segs, all_segs
    
def build_dict_from_all_segs(all_seg_list):
    print('| * Build dictionary from all_segs (Set)')
    segs_dict = {}
    for seg in all_seg_list:
        segs_dict[seg] = 0
    return segs_dict

def calculate_2type_comments(segs_dict, p_segs, h_segs):
    print('| * Calculate 2type comments')
    for seg in h_segs:
        segs_dict[seg] -=1
    for seg in p_segs:
        segs_dict[seg] += 1
    all_segs_sort_by_value = sorted(segs_dict.items(), key=lambda kv: kv[1])
    return all_segs_sort_by_value

def filter_short_segs(sorted_by_value):
    print('| * Filter too short segs')
    results = []
    for item in sorted_by_value:
        if len(item[0])>=2:
            results.append(item)
    print('推:',results[-10:])
    print('噓:',results[:10])


#comments_classification_by_pushtag(pushs_to_dict(read_data()))
# 直接使用checkpoint的資料開始執行
p, h = read_coments_file()
p_segs, h_segs, all_segs = split_comments_to_seg(p, h)
segs_dict = build_dict_from_all_segs(all_segs)
all_segs_sort_by_value = calculate_2type_comments(segs_dict, p_segs, h_segs)
filter_short_segs(all_segs_sort_by_value)
