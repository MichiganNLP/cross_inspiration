Cross-cultural Inspiration Detection and Analysis in Real and LLM-generated Social Media Data
=================================================================================

This repository contains the dataset and code for our paper.

## Task Description

[//]: # (![img/main_idea.png]&#40;img/main_idea.png&#41;)

<p align="center" width="100%">
    <img src="img/main_idea.png">
</p>

We compare AI-generated and human-written inspiring Reddit content across India and the UK. 
Although there may not be any visible differences to the human eye, by using 
linguistic methods, we find significant syntactic and lexical cross-cultural differences 
between generated and real inspiring posts.

## Data

The final data is available at [`all_data`](data/all_data.csv)
All annotations are available in [`all_annotations'](data)

## Features

Topic Modeling features can be accessed interactively in [`topic_analysis`](topic_analysis)

## Models

### GPT-4 generation
All generation code is available at [LLM_generation](LLM_generation.py).

### Inspiration Detection models
Random Forest, Naive Bayes, SVM models are available at [baselines](baselines.ipynb).

XLM-Roberta is available at [roberta](xlm_roberta_multilabel.ipynb).

Llama-2-7b model with LoRA fine-tuning is available at [llama](llama.ipynb).

## Citation

```bibtex
@inproceedings{ignat-etal-2025-inspaired,
    title = "{I}nsp{AI}red: Cross-cultural Inspiration Detection and Analysis in Real and {LLM}-generated Social Media Data",
    author = "Ignat, Oana  and
      Lakshmy, Gayathri Ganesh  and
      Mihalcea, Rada",
    editor = "Prabhakaran, Vinodkumar  and
      Dev, Sunipa  and
      Benotti, Luciana  and
      Hershcovich, Daniel  and
      Cao, Yong  and
      Zhou, Li  and
      Cabello, Laura  and
      Adebara, Ife",
    booktitle = "Proceedings of the 3rd Workshop on Cross-Cultural Considerations in NLP (C3NLP 2025)",
    month = may,
    year = "2025",
    address = "Albuquerque, New Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.c3nlp-1.4/",
    pages = "35--49",
    ISBN = "979-8-89176-237-4",
    abstract = "Inspiration is linked to various positive outcomes, such as increased creativity, productivity, and happiness. Although inspiration has great potential, there has been limited effort toward identifying content that is inspiring, as opposed to just engaging or positive. Additionally, most research has concentrated on Western data, with little attention paid to other cultures. This work is the first to study cross-cultural inspiration through machine learning methods. We aim to identify and analyze real and AI-generated cross-cultural inspiring posts. To this end, we compile and make publicly available the InspAIred dataset, which consists of 2,000 real inspiring posts, 2,000 real non-inspiring posts, and 2,000 generated inspiring posts evenly distributed across India and the UK. The real posts are sourced from Reddit, while the generated posts are created using the GPT-4 model. Using this dataset, we conduct extensive computational linguistic analyses to (1) compare inspiring content across cultures, (2) compare AI-generated inspiring posts to real inspiring posts, and (3) determine if detection models can accurately distinguish between inspiring content across cultures and data sources."
}
```
