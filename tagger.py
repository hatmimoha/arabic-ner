from transformers import pipeline
from helpers import preprocess
import logging
import time

# Initialize the pipeline
ner_token_classifier = pipeline(
    "ner", model="hatmimoha/arabic-ner"
)

# Tag the text
start_time = time.time()
text = 'رغم الهدنة .. معارك قره باغ متواصلة وأذربيجان تعلن سيطرتها على مزيد من القرى'
sentences = preprocess(text)
result = ner_token_classifier(sentences)
logging.info('Text proceeded in %s' % str(time.time() - start_time))

print(result)
