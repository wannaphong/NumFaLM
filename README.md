# NumFaLM
NumFaLM (น้ำฟ้า) is a bilingual language model trained in Thai and English.

## NumFaLM 3B
NumFaLM 3B is a bilingual language model trained in Thai and English. The architecture model is Llama model that pretraining from scratch. It was built to open source AI and research for bilingual language models and improve small language models. We released the training script and train datasets so you can research the training and datasets.

- GitHub: [https://github.com/wannaphong/NumFaLM](https://github.com/wannaphong/NumFaLM)
- Training script: [https://github.com/wannaphong/EasyLM/tree/numfa_pretraining](https://github.com/wannaphong/EasyLM/tree/numfa_pretraining)
- Train Datasets: [wannaphong/mark13](https://huggingface.co/datasets/wannaphong/mark13)


We fork EasyLM and added training by HuggingFace datasets, but HuggingFace was down many times during the time we trained the model (april 2024), so we can train just one epoch. The model trained one epoch.


### Steps

#### Datasets

For English, English is bigger than all Thai datasets, so we select the high quality dataset only. We choose [cosmopedia dataset](https://huggingface.co/blog/cosmopedia) that wants to replicate Phi-1.5, [minipile](https://huggingface.co/datasets/JeanKaddour/minipile) is a 6GB subset of the deduplicated The Pile corpus, and [goodwiki](https://huggingface.co/datasets/euirim/goodwiki) is a 179 million token dataset of English Wikipedia articles collected on September 4, 2023.

For Thai, we create many datasets that are part of the Thai corpus. To build a bilingual language model, we add a Thai-English parallel corpus.

We added a Python coding corpus to make the language model have logic coding.

You can see the list dataset at datasets/.


# Acknowledgements

Research supported with Cloud TPUs from Google's [TPU Research Cloud](https://sites.research.google/trc/about/) (TRC). We use TPU4-64 for training model about 4 days / 1 epoch.

Thank you [TPU Research Cloud](https://sites.research.google/trc/about/) and [EasyLM project](https://github.com/young-geng/EasyLM)! We use EasyLM for the pretraining model.