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

```
