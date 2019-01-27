"""
Gameify's professor information and stores it into database
Machine learning stuff. Sentiment analysis, NLP, key phrase detection.
"""
import requests
from services.config import (AZURE_TEXT_ANALYTICS_NAME, AZURE_TEXT_ANALYTICS_KEY1, AZURE_TEXT_ANALYTICS_KEY2,
                    AZURE_TEXT_ANALYTICS_URL)
from pprint import pprint
#from services.slack_bot import *
from services.database import models
from services.database.db_client import query_prof, insert_item, get_db_session
#from services.getProfHTML import professorURL


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


def slack_prof_query(first_name, last_name) -> models.Prof:
    """
    #Given a professor's name, query for professor 
    """
    session = get_db_session()
    query = query_prof(session, first_name, last_name)
    if query is None:
        # Pull data from RMP and store in database. Then process it.
        name = first_name + ' ' + last_name
        profInfo = professorURL(name)
        prof = models.Prof(url = profInfo['url'], first_name=profInfo['first_name'], last_name=profInfo['last_name'],
                            rating=profInfo['rating'], average_passing = profInfo['average_passing'], take_again=profInfo['take_again'])
        insert_item(session, prof)
        return prof

    else: 
        return query


def gameify_prof(prof: models.Prof):
    response = \
                f'\n\
                Professor: {prof.first_name} {prof.last_name}\n\
                Stats: \n\
                    - Rating: {prof.rating}\n\
                    - Average Passing: {prof.average_passing}%\n\
                    - Take again: {prof.take_again}%\n'
    return response

def slackbot_query_print(prof_name):
    firstName = prof_name.partition(' ')[0]
    lastName = prof_name.partition(' ')[2]
    prof = slack_prof_query(first_name,last_name)
    text = gameify_prof(prof)
    return text

#session = get_db_session()
#rof = models.Prof(url='google.com',first_name='Jeff',last_name='Doug',rating='7.9',average_passing='96',take_again='57')
#gameify_prof(prof)



# analyze_text('entities', ['HEY WHAT UP. How are you doing. Dogs are great', 'Hi. My name is Jeff.', 'Bonjour'])

