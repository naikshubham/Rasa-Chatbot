# takes chatito json file and create markdown file for training


import json
import argparse

parser = argparse.ArgumentParser(description='Python program to add reg expression rules to the training data.')
parser.add_argument('--json_file', help='json file', type=str)

args = parser.parse_args()
json_file = args.json_file

f = open(json_file)
data = json.load(f)['rasa_nlu_data']['common_examples']
intents = set(["## intent:"+d['intent'] for d in data])
md_dict = {}
for intent in intents:
    md_dict[intent] = []
for d in data:
    text = d['text']
    if len(d['entities']) != 0:
        buffer = 0
        for i in range(len(d['entities'])):
            if i !=0:
                start = d['entities'][i]['start'] + buffer
                end = d['entities'][i]['end'] + buffer
            else:
                start = d['entities'][i]['start']
                end = d['entities'][i]['end']
            entity = d['entities'][i]['entity']
            text = text[:start] + '[' + text[start:end] + ']('+entity+')' + text[end:]
            buffer = buffer + 4 + len(entity)
            
    md_dict["## intent:"+d['intent']].append('- '+text)
    

with open('../nlu.md', 'w') as f:
    for k,v in md_dict.items():
        f.write(k)
        f.write('\n')
        for val in v:
            f.write(val)
            f.write('\n')
        f.write('\n')
