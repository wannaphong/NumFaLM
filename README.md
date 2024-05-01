# NumFaLM
NumFaLM (น้ำฟ้า) is a bilingual language model trained on Thai and English.

## NumFaLM 3B
NumFaLM 3B is a bilingual language model trained on Thai and English. The architecture model is Llama model that pretraining from scratch. It was build to open source AI and research for bilingual language model and improve small language model. We released the training srcipt and train datasets to you can research the training and datasets.

- GitHub: [https://github.com/wannaphong/NumFaLM](https://github.com/wannaphong/NumFaLM)
- Training script: [https://github.com/wannaphong/EasyLM/tree/numfa_pretraining](https://github.com/wannaphong/EasyLM/tree/numfa_pretraining)
- Train Datasets: [wannaphong/mark13](https://huggingface.co/datasets/wannaphong/mark13)


We fork EasyLM and add training by HuggingFace datasets but HuggingFace was down many time in during the time we train the model, so we can trained just 1 epoch. The model trained 1 epoch.

# Acknowledgements

Research supported with Cloud TPUs from Google's [TPU Research Cloud](https://sites.research.google/trc/about/) (TRC). We use TPU4-64 for training model about 4 days / 1 epoch.

Thank you [TPU Research Cloud](https://sites.research.google/trc/about/) and [EasyLM project](https://github.com/young-geng/EasyLM)! We use EasyLM for pretraining model.