import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer
from helpers import preprocess, postprocess
import numpy as np
import logging
import time


TAGS = ["B-PERSON", "I-PERSON", "B-ORGANIZATION", "I-ORGANIZATION", "B-LOCATION", "I-LOCATION", "B-DATE", "I-DATE",
        "B-COMPETITION", "I-COMPETITION", "B-PRICE", "I-PRICE", "O", "B-PRODUCT", "I-PRODUCT", "B-EVENT", "I-EVENT",
        "B-DISEASE", "I-DISEASE"]

# Load the model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained('hatmimoha/arabic-ner', do_lower_case=False)
model = AutoModelForTokenClassification.from_pretrained("hatmimoha/arabic-ner")

# Tag the text
start_time = time.time()
text = 'رغم الهدنة .. معارك قره باغ متواصلة وأذربيجان تعلن سيطرتها على مزيد من القرى'
test_sentences = preprocess(text)

labels = []
tokenized_sentence = tokenizer(test_sentences, padding=True, truncation=True, return_tensors="pt")
tokenized_sentences = tokenized_sentence['input_ids'].numpy()

with torch.no_grad():
    output = model(**tokenized_sentence)


j = 0
last_hidden_states = output[0].numpy()
outputs = []
for entry in last_hidden_states:
    label_indices = np.argmax(entry, axis=1)
    tokens = tokenizer.convert_ids_to_tokens(tokenized_sentences[j])
    new_tokens, new_labels = [], []
    i = 0
    beginToken = True
    customized_tokens = test_sentences[j].split()

    for token, label_idx in zip(tokens, label_indices):
        if token != '[CLS]' and token != '[SEP]' and token != '[PAD]':
            if token.startswith("##"):
                new_tokens[-1] = new_tokens[-1] + token[2:]
                if new_tokens[-1] == customized_tokens[i]:
                    beginToken = True
                    i += 1
            else:
                if token == customized_tokens[i] or token == '[UNK]':
                    new_labels.append(TAGS[label_idx])
                    new_tokens.append(customized_tokens[i])
                    i += 1
                    beginToken = True
                else:
                    if beginToken:
                        new_labels.append(TAGS[label_idx])
                        new_tokens.append(token)
                        beginToken = False
                    else:
                        new_tokens[-1] = new_tokens[-1] + token
                        if new_labels[-1] == 'O' and TAGS[label_idx] != 'O':
                            new_labels[-1] = TAGS[label_idx]
                        if new_tokens[-1] == customized_tokens[i]:
                            beginToken = True
                            i += 1

    labels.append(new_labels)
    j += 1
    sentence_outputs = []
    for token, label in zip(new_tokens, new_labels):
        sentence_outputs.append({token: label})
    outputs.append(sentence_outputs)

# Post-process the output
result = postprocess(outputs)
logging.info('Text proceeded in %s' % str(time.time() - start_time))

print(result)
