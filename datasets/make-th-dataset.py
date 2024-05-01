import random
random.seed(42)
from datasets import load_dataset
import os
import glob
import ujson
from tqdm.auto import tqdm
import pandas as pd
from transformers import AutoTokenizer
from pythainlp.tokenize import word_tokenize


tokenizer = AutoTokenizer.from_pretrained("scb10x/typhoon-7b",use_fast=True)

thai_list=list(load_dataset("pythainlp/thai_food_v1.0",split="train")["text"])
thai_list.extend(load_dataset("pythainlp/thailaw-v1.0",split="train")["text"])
_temp=load_dataset("pythainlp/thai-tnhc2-books",split="train")
thai_list.extend([i+"\n"+j for i,j in zip(_temp["book"],_temp["text"])])
del _temp
thai_list.extend(load_dataset("pythainlp/thai-constitution-corpus",split="train")["txt"])
thai_list.extend(load_dataset("pythainlp/thai-it-books",split="train")["text"])
thai_list.extend(load_dataset("pythainlp/prd_news_30112023",split="train")["Detail"])
thai_list.extend(load_dataset("pythainlp/thailand-policy-statements",split="train")["text"])
thai_list.extend(load_dataset("pythainlp/thai-cc-license",split="train")["text"])
_temp=load_dataset("pythainlp/thaisum",split="train")
thai_list.extend([i+"\n"+j for i,j in zip(_temp["title"],_temp["body"])])
del _temp
_temp=load_dataset("pythainlp/thaisum",split="validation")
thai_list.extend([i+"\n"+j for i,j in zip(_temp["title"],_temp["body"])])
del _temp
_temp=load_dataset("pythainlp/thaisum",split="test")
thai_list.extend([i+"\n"+j for i,j in zip(_temp["title"],_temp["body"])])
del _temp
thai_list.extend(load_dataset("pythainlp/blognone_news",split="train")["txt"])
thai_list.extend(load_dataset("pythainlp/goethe-website",split="train")["text"])
thai_list.extend([i for i in load_dataset("pythainlp/thai-wiki-dataset-v3",split="train")["text"] if len(i)>20])
thai_list.extend(load_dataset("pythainlp/thai-open-data-go-th",split="train")["text"])
# thai_list.extend(load_dataset("pythainlp/thai-financial-dataset",split="train")["text"])
thai_list.extend(load_dataset("pythainlp/thai_usembassy",split="train")["th"])
thai_list.extend(load_dataset("pythainlp/inquiringmind-website",split="train")["text"])
# thai_list.extend(list(pd.read_csv("./lab-data/ratchagitja-clean2.csv")["text"]))
thai_list.extend(load_dataset("pythainlp/thai-open-data-text-v1",split="train")["text"])
_temp=pd.read_csv("-news-30032024.csv")
thai_list.extend([i+"\n"+j for i,j in zip(_temp["title"],_temp["article"])])
del _temp
thai_list.extend(load_dataset("pythainlp/thaigov-corpus",split="train")["raw"])
thai_list.extend(load_dataset("pythainlp/thaigov-v2-corpus-31032024",split="train")["raw"])
_temp=pd.read_csv("-news-01042024.csv")
thai_list.extend([i+"\n"+j for i,j in zip(_temp["title"],_temp["article"])])
del _temp
thai_list=[i for i in thai_list if isinstance(i,str)]

import signal
thai_list=[i for i in tqdm(thai_list) if isinstance(i,str)]
random.shuffle(thai_list)
n=1
import signal

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)


with open("/disk/thai_data.jsonl","w",encoding="utf-8") as out:
    for t in tqdm(thai_list):
        try:
            with timeout(seconds=15):
                word_tokenize(t)
                ss = ujson.dumps({"meta": {"src":"th_data2_"+str(n)}, "text": t}, ensure_ascii=False)
                out.write(ss + "\n")
                n+=1
        except:
            # print(t)
            print("skip")
            continue