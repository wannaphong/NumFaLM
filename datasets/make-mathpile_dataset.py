"""
mathplie_dataset

We use mathplie_dataset from https://huggingface.co/datasets/GAIR/MathPile_Commercial

$ huggingface-cli download --resume-download --repo-type dataset GAIR/MathPile --local-dir /disk/mathpile_dataset --local-dir-use-symlinks False

"""
import random
random.seed(42)
from datasets import load_dataset
import os
import glob
import ujson
from tqdm.auto import tqdm

en_list=[]
def get_StackExchange(k):
    _text = "Question:\n"
    _text+='Title: '+k['question']['Title']+"\n"
    _text+='Body: '+k['question']['Body']+"\n"
    _text+='Id: '+k['question']['Id']+"\n"
    _text+='Score: '+k['question']['Score']+"\n"
    _text+='Tags: '+k['question']['Tags']+"\n\n"
    _text+="Answers:\n"
    for a in k["answers"]:
        _text+="Body: "+a["Body"]+"\n"
        _text+='Id: '+a['Id']+"\n"
        _text+='Score: '+a['Score']+"\n"
        _text+='is_accepted_answer: '+str(a['is_accepted_answer'])+"\n\n"
    return _text.strip()

for i in tqdm(list(glob.glob("/disk/mathpile_dataset/train/*/*.jsonl"))):
    with open(i) as f:
        for line in f:
            temp = ujson.loads(line)
            if temp['subset']=='StackExchange':
                _t = get_StackExchange(temp)
            else:
                _t = temp["text"]
            en_list.append(_t)
n=1
with open("/disk/mathpile_dataset.jsonl","a",encoding="utf-8") as out:
    for t in tqdm(en_list):
        ss = ujson.dumps({"meta": {"src":"data_"+str(n)}, "text": t}, ensure_ascii=False)
        out.write(ss + "\n")
        n+=1