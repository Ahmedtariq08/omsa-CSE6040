import numpy as np
import scipy as sp
import pandas as pd
from collections import Counter
import re

import dill
from pprint import pprint


### Solution - Exercise 0 (2 points) [Passed]
prefix_dict = {
    '#*': 'title',
    '#@': 'authors',
    '#t': 'year',
    '#c': 'venue',
    '#index': 'id',
    '#%': 'refs',
    '#!': 'abstract'
}

def get_record(lines: list) -> dict:
    output = {}
    for s in lines:
        for key in list(prefix_dict.keys()):
            if s.startswith(key):
                title = prefix_dict[key]
                replacedStr = s.replace(key, "").replace('\n', '')
                if (title in output.keys()):
                    output[title].append(replacedStr)
                    output[title].sort()
                else:
                    output[title] = [replacedStr]
        
    return output


### Solution - Exercise 1 (1 point) [Passed]
def clean_record(record: dict) -> dict:
    cleaned = record.copy()
    for mk in ['id', 'title', 'year', 'venue', 'abstract']:
        if (mk not in record.keys()):
            return None

    for key in cleaned.keys():
        if key == 'id' or key == 'year':
            cleaned[key] = int(record[key][0])
        elif key == 'refs':
            cleaned[key] = [int(x) for x in record[key]]
        else:
            cleaned[key] = record[key][0]
   
    return cleaned


### Solution - Exercise 2 (2 point) [Passed]
def records_to_metadf(records: list) -> pd.DataFrame:
    df = pd.DataFrame(records, columns=['id', 'title', 'year', 'venue', 'abstract'])
    return df

### Solution - Exercise 3 (2 point) [Passed]
def gen_corpus(metadf: pd.DataFrame, stopwords):
    output = metadf[['id', 'title']].copy()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    
    def process_row(row):
        raw_words = str(row['title'] + ' ' + row['abstract'] + ' ' + row['venue']).lower().split()
        processed_words = []
        
        for word in raw_words:
            token = "".join([c if c in alphabets else " " for c in word])
            for tk in token.split():
                if tk not in stopwords and tk not in processed_words:
                    processed_words.append(tk.strip())
                
        processed_words.sort()
        out = " ".join(processed_words).strip()    
        return out
        
    output['pseudodoc'] = metadf.apply(process_row, axis=1)
    return output
   

### Exercise 4 or 5 (2 points) [NOT Passed]
def count_words(cid, labels, corpusdf, k=10):
    indexes = [index for index, label in enumerate(labels) if label == cid]
    allTokens = corpusdf.loc[indexes]['pseudodoc'].values
    
    obj = {}    
    for line in allTokens:
        for word in line.split():
            if (word not in obj):
                obj[word] = len([x for x in allTokens if word in x])
    
    # Code edited to pass the cases, check and validate
    sorted_dict = dict(sorted(obj.items(), key=lambda item: (-item[1], item[0])))
    return set(list(sorted_dict.keys())[:k])
    

