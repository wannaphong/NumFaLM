import random
random.seed(42)
from datasets import load_dataset
import os
import glob
import ujson
from tqdm.auto import tqdm
import pandas as pd


list_text=[]

template="{l1}\t{l2}"

scb_dataset = load_dataset("scb_mt_enth_2020","enth",split="train")["translation"]
n=0
for i in scb_dataset:
    if not isinstance(i,dict):
        i=eval(i)
    d=i
    if n%2==0:
        l1=d['en']
        l2=d['th']
    else:
        l1=d['th']
        l2=d['en']
    if l1==None or l2==None:
        continue
    if len(l1)<3 or len(l2)<3:
        continue
    list_text.append(template.format(l1=l1,l2=l2))
    n+=1
del scb_dataset

# dataset = load_dataset("pythainlp/scb-mt-en-th-2020_mt-opus",split="train")
# n=0
# for en,th in zip(dataset["en"],dataset["th"]):
#     if n%2==0:
#         l1=en
#         l2=th
#     else:
#         l1=th
#         l2=en
#     if l1==None or l2==None:
#         continue
#     if len(l1)<3 or len(l2)<3:
#         continue
#     if "TRANS".lower() in th.lower() or "สหชาติ อนุกูลกิจ" in th:
#         continue
#     list_text.append(template.format(l1=l1,l2=l2))
#     n+=1
# del dataset
dataset = load_dataset("bible_para", lang1="en", lang2="th",split="train")["translation"]
n=0
for i in dataset:
    if not isinstance(i,dict):
        i=eval(i)
    d=i
    if n%2==0:
        l1=d['en']
        l2=d['th']
    else:
        l1=d['th']
        l2=d['en']
    if l1==None or l2==None:
        continue
    if len(l1)<3 or len(l2)<3:
        continue
    list_text.append(template.format(l1=l1,l2=l2))
    n+=1
del dataset

dataset = load_dataset("tatoeba", lang1="en", lang2="th",split="train")["translation"]
n=0
for i in dataset:
    if not isinstance(i,dict):
        i=eval(i)
    d=i
    if n%2==0:
        l1=d['en']
        l2=d['th']
    else:
        l1=d['th']
        l2=d['en']
    if l1==None or l2==None:
        continue
    if len(l1)<3 or len(l2)<3:
        continue
    list_text.append(template.format(l1=l1,l2=l2))
    n+=1
del dataset

# dataset = load_dataset("pythainlp/thai_usembassy",split="train")
# n=0
# for en,th in zip(dataset["en"],dataset["th"]):
#     if n%2==0:
#         l1=en
#         l2=th
#     else:
#         l1=th
#         l2=en
#     if l1==None or l2==None:
#         continue
#     if len(l1)<3 or len(l2)<3:
#         continue
#     list_text.append(template.format(l1=l1,l2=l2))
#     n+=1
# del dataset

dataset = load_dataset("ayymen/Pontoon-Translations","en-th",split="train")
n=0
for en,th in zip(dataset["source_string"],dataset["target_string"]):
    if n%2==0:
        l1=en
        l2=th
    else:
        l1=th
        l2=en
    if l1==None or l2==None:
        continue
    if len(l1)<3 or len(l2)<3:
        continue
    list_text.append(template.format(l1=l1,l2=l2))
    n+=1
del dataset

dataset = pd.read_csv("lab-data/talpco-en-th.csv")["translation"]
n=0
for i in dataset:
    if not isinstance(i,dict):
        i=eval(i)
    d=i
    if n%2==0:
        l1=d['en']
        l2=d['th']
    else:
        l1=d['th']
        l2=d['en']
    if l1==None or l2==None:
        continue
    if len(l1)<3 or len(l2)<3:
        continue
    list_text.append(template.format(l1=l1,l2=l2))
    n+=1
del dataset
dataset = load_dataset("alt", "alt-parallel",split="train")["translation"]
n=0
for i in dataset:
    if not isinstance(i,dict):
        i=eval(i)
    d=i
    if n%2==0:
        l1=d['en']
        l2=d['th']
    else:
        l1=d['th']
        l2=d['en']
    if l1==None or l2==None:
        continue
    if len(l1)<3 or len(l2)<3:
        continue
    list_text.append(template.format(l1=l1,l2=l2))
    n+=1
del dataset

n=1
with open("/disk/parallel_data.jsonl","w",encoding="utf-8") as out:
    for t in tqdm(list_text):
        ss = ujson.dumps({"meta": {"src":"parallel-data_"+str(n)}, "text": t}, ensure_ascii=False)
        out.write(ss + "\n")
        n+=1