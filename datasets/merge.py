filename2="/disk/thai_data-4.jsonl"
filename3="/disk/code_data.jsonl"
filename4="/disk/th_culturax_data.jsonl"
filename5="/disk/parallel_data.jsonl"

filename1="/disk/cosmopedia.jsonl"
filename6="/disk/mathpile_dataset.jsonl"
filename7="/disk/minipile.jsonl"
filename8="/disk/goodwiki.jsonl"





outfilename="/disk/numfa_train_dataset.jsonl"

# thank https://stackoverflow.com/a/42480411
from itertools import zip_longest
from tqdm.auto import tqdm
with open(filename1) as f1, open(filename2) as f2, open(filename3) as f3, open(filename4) as f4, open(filename5) as f5, open(filename6) as f6, open(filename7) as f7, open(filename8) as f8, open(outfilename, 'w') as of:
    for lines in tqdm(zip_longest(f1, f2,f6,f3,f8,f4,f5,f7),total=31064744+1):
        for line in lines:
            if line is not None: of.writelines(line.strip()+"\n")