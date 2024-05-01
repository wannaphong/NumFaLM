import random
random.seed(42)
from datasets import load_dataset
import os
import glob
import ujson
from tqdm.auto import tqdm

en_list=load_dataset("HuggingFaceTB/cosmopedia","stories", split="train")["text"]

en_list.extend(load_dataset("HuggingFaceTB/cosmopedia","auto_math_text", split="train")["text"])

en_list.extend(load_dataset("HuggingFaceTB/cosmopedia","khanacademy", split="train")["text"])

en_list.extend(load_dataset("HuggingFaceTB/cosmopedia","openstax", split="train")["text"])

en_list.extend(load_dataset("HuggingFaceTB/cosmopedia","stanford", split="train")["text"])

_temp=load_dataset("HuggingFaceTB/cosmopedia","web_samples_v1", split="train")["text"]

_temp[3040]='''Chapter 13: Website Traffic Analysis through Channels Configuration\n\n13.1 Introduction\n\nWebsite analytics plays a crucial role in understanding user behavior, optimizing content delivery, and measuring marketing campaigns\' effectiveness in today\'s digital landscape. A key aspect of website analysis involves monitoring and evaluating individual sections\' performance to make informed decisions about resource allocation, design improvements, and promotional strategies. One way to achieve this goal is by configuring channels—a feature provided by various web analytics tools like Google Analytics—that enable you to isolate and study the traffic patterns associated with a particular segment of your website.\n\nThis chapter delves into the concept of channels configuration and its implementation using a fictional web analytics platform called "Traffica." By following the step-by-step instructions outlined below, you will learn how to create custom channels to analyze the traffic generated by specific sections of a website thoroughly.\n\n13.2 What are Channels?\n\nChannels represent virtual containers designed to group different pages or parts of a website based on shared characteristics, enabling analysts to examine their respective traffic data independently. These classifications can include categories like blog posts, product pages, support articles, or any other logical divisions defined according to your project requirements. Creating separate channels allows users to evaluate each portion\'s unique metrics without being influenced by the overall site performance.\n\n13.3 Configuring a Channel in Traffica\n\nFollow these seven steps to create a new channel in the Traffica platform:\n\nStep 1: Log in to your account by visiting <https://www.traffica.com/> and entering your credentials.\n\nStep 2: Once logged in, locate the "Account Management" option in the vertical navigation bar on the left side of the screen (Figure 1). Select "Settings" under Account Management to access the settings panel.\n\n![Figure 1 - Accessing Settings](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAQCAYAAADno+9zAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAABJRU5ErkJggg==)\n\nFigure 1 – Accessing Settings\n\nStep 3: Within the settings panel, find the third item labeled "Features" and click on it to reveal further options. From there, choose "Channels" to navigate to the channels management page (Figure 2).\n\n![Figure 2 - Navigation Path to Channels Management Page](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAIAAAD_O7fAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACbSURBVHgBvZMzEP///z8PDx8P7v1DyAU9Hr//qLlDtjNH7e0/z8/Pz+Pfr7vtDyauhdhc7lh+z7u7trbf3pLliuz6ee++9vfvz+z7u9vb3/z7vDyvfuHDx9vrXv7/P39/f2tra1tbW1tfX1dbW2dnZ3d3d4ubm7u7u7vDzz+fiHz5+fo9PT29vb09fc3Nzc3)'''
en_list.extend(_temp)
del _temp
en_list.extend(load_dataset("HuggingFaceTB/cosmopedia","web_samples_v2", split="train")["text"])

en_list.extend(load_dataset("HuggingFaceTB/cosmopedia","wikihow", split="train")["text"])
n=0
with open("/disk/cosmopedia.jsonl","w",encoding="utf-8") as out:
    for t in tqdm(en_list):
        ss = ujson.dumps({"meta": {"src":"HuggingFaceTB/cosmopedia_"+str(n)}, "text": t}, ensure_ascii=False)
        out.write(ss + "\n")
        n+=1