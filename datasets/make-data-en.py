import random
random.seed(42)
from datasets import load_dataset
import os
import glob
import ujson
from tqdm.auto import tqdm
en_list=[]
for i in tqdm(load_dataset("JeanKaddour/minipile", split="train")["text"],total=1010500):
    en_list.append(i)
n=0
with open("/disk/minipile.jsonl","w",encoding="utf-8") as out:
    for t in tqdm(en_list):
        ss = ujson.dumps({"meta": {"src":"JeanKaddour/minipile_"+str(n)}, "text": t}, ensure_ascii=False)
        out.write(ss + "\n")
        n+=1

en_list=[]
for i in tqdm(load_dataset("euirim/goodwiki", split="train")["markdown"],total=44754):
    en_list.append(i)
n=0
with open("/disk/goodwiki.jsonl","w",encoding="utf-8") as out:
    for t in tqdm(en_list):
        ss = ujson.dumps({"meta": {"src":"euirim/goodwiki_"+str(n)}, "text": t}, ensure_ascii=False)
        out.write(ss + "\n")
        n+=1