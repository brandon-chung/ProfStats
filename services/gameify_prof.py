"""
Gameify's professor information and stores it into database
Machine learning stuff. Sentiment analysis, NLP, key phrase detection.
"""
import requests
from config import (AZURE_TEXT_ANALYTICS_NAME, AZURE_TEXT_ANALYTICS_KEY1, AZURE_TEXT_ANALYTICS_KEY2,
                    AZURE_TEXT_ANALYTICS_URL)
from pprint import pprint
headers   = {"Ocp-Apim-Subscription-Key": AZURE_TEXT_ANALYTICS_KEY2}

query_types = ['languages', 'keyPhrases', 'entities', 'sentiment']

def analyze_text(query_type: str, input_texts: [str], api_key: str = AZURE_TEXT_ANALYTICS_KEY1):
    if query_type not in query_types:
        return ''
    url = AZURE_TEXT_ANALYTICS_URL + query_type
    data = {'documents': []}
    doc_id = 1
    for text in input_texts:
        str_id = str(doc_id)
        doc = {'id': str_id, 'text': text}
        data['documents'].append(doc)
        doc_id += 1
    r = requests.post(url, headers=headers, json=data)
    response = r.json()
    pprint(response)

# analyze_text('entities', ['HEY WHAT UP. How are you doing. Dogs are great', 'Hi. My name is Jeff.', 'Bonjour'])

