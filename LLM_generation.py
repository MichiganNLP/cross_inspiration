import openai
import pandas as pd
import random
from tqdm import tqdm

openai.api_type = "azure"
openai.api_base = "add yours" #TODO
openai.api_version = "2023-09-01-preview"
openai.api_key = "add yours" #TODO


def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=messages,
        temperature=1,
        top_p=1
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages):
    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=messages,
        temperature=1,
        top_p=1
    )
    response_content = response.choices[0].message["content"]
    # print(f"Debug: Response from OpenAI: {response_content}")
    return response_content
    # return response.choices[0].message["content"]

def get_labeled_inspir(culture):
    inspir_annotated = []
    if culture == "uk":
        data = pd.read_csv('data/uk_annotations.csv')
    else:
        data = pd.read_csv('data/india_annotations.csv')
    for txt, ann1, ann2, ann3 in zip(data['Text'], data['Annotator 1'], data['Annotator 2'], data['Annotator 3']):
        if ann1 == 1 and ann2 == 1 and ann3 == 1: # TODO: select which posts (3/3, 2/3, 1/3 inspir annotated) to give as examples for few-shot prompting
        # if ann1 == 1 or ann2 == 1 or ann3 == 1:
        # if (ann1 == 1 and ann2 == 1) or (ann3 == 1 and ann2 == 1) or (ann3 == 1 and ann1 == 1):
            inspir_annotated.append(txt)
    return inspir_annotated

def get_messages(location, example_posts):
    example_random_post = random.choice(example_posts)
    messages = [
        {'role': 'system',
         'content': f"""Imagine you're a person from {location} and use Reddit."""},

        {'role': 'user',
         'content': f"""Please write a short Reddit post or comment of maximum 100 tokens about what inspires you."""},
        {'role': 'assistant', 'content': example_random_post},

        {'role': 'user',
         'content': f"""Please write a short Reddit post or comment of maximum 100 tokens about what inspires you. The style of generated one should be consistent with previous one."""}
    ]
    return messages

def generate(culture):
    if culture == "uk":
        location = "UK"
    else:
        location = "India" #TODO: more fine-grained?

    example_posts = get_labeled_inspir(culture)

    dict_data = {}
    for _ in tqdm(range(1000)):
        try:
            messages = get_messages(location, example_posts) # call each time for randomness
            response = get_completion_from_messages(messages)
            print(response)
            dict_data['prompt'] = ['-']
            dict_data['text'] = [response]
            dict_data['class'] = [culture]
        except Exception as error:
            print("An error occurred:", error)
        df = pd.DataFrame(dict_data)
        df.to_csv(f'data/{culture}_generated.csv', mode='a', index=False, header=False)

def main():
    culture = "india" #uk #TODO select between uk and india
    generate(culture)


if __name__ == "__main__":
    main()