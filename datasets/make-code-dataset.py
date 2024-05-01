import random
random.seed(42)
from datasets import load_dataset
import os
import glob
import ujson
from tqdm.auto import tqdm
import pandas as pd

list_text = load_dataset("codeparrot/codeparrot-clean",split="train", streaming=True)

n=1
with open("/disk/code_data.jsonl","w",encoding="utf-8") as out:
    for t in tqdm(list_text):
        ss = ujson.dumps({"meta": {"src":"codeparrot-clean_"+str(n)}, "text": t["content"]}, ensure_ascii=False)
        out.write(ss + "\n")
        n+=1
df=pd.read_csv("learnxinyminutes.csv")
print(df)

n=1
with open("/disk/code_data.jsonl","a",encoding="utf-8") as out:
    for t in tqdm(df["text"]):
        ss = ujson.dumps({"meta": {"src":"learnxinyminutes_"+str(n)}, "text": t}, ensure_ascii=False)
        out.write(ss + "\n")
        n+=1