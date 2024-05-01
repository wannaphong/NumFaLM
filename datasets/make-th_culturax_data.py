import random
random.seed(42)
from datasets import load_dataset
import os
import glob
import ujson
from tqdm.auto import tqdm
import pandas as pd

list_text = load_dataset("pythainlp/thai-culturax-clean-dataset",split="train", streaming=True)

n=1
with open("/disk/th_culturax_data.jsonl","w",encoding="utf-8") as out:
    for t in tqdm(list_text):
        ss = ujson.dumps({"meta": t["meta"], "text": t["content"]}, ensure_ascii=False)
        out.write(ss + "\n")
        n+=1