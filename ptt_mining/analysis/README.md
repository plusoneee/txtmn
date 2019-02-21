
### Dependencies
* Python 3
### Python Requirements
```
re
demjson
jieba
ast
pandas
```

### Run
* (option 1) If you don't want to spend time on crawler, just run:
```
python app.py
```
* (option 2) If want to analyze datasets after using `crawler`, have to uncomment the [line](https://github.com/plusoneee/txtmn/blob/master/ptt_mining/analysis/app.py#L87) at `/analysis/app.py`. like:
```python
comments_classification_by_pushtag(pushs_to_dict(read_data()))
```

