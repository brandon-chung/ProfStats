"""
Slack bot. Given a specific command, responds with gameified professor information
Reference: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
           https://github.com/slackapi/python-slack-events-api/blob/master/example/example.py
           https://github.com/bchung00/Social-Growth-Bot/blob/master/bot.py
"""
import os
import time
import re
import query_RMP
from slackclient import SlackClient
from services.getProfHTML import *
#from services.gameify_prof import *

# instantiate Slack client
slack_token = ''
sc = SlackClient(slack_token)
# starterbot's user ID in Slack
starterbot_id = None

# If connected...
if sc.rtm_connect():
    print('Connected...')

# Response to error
def error_handler(err):
    print("ERROR: " + str(err))

def print_to_slackbot():
        sc.api_call(
        "chat.postMessage",
        channel= event['channel'],
        text= prof_name,  #To be changed
        user= event['user']
        )

if sc.rtm_connect():
    while True:
        events = sc.rtm_read()
        print(events)
        for event in events:
            # Check if new message and channel is #slack-prof-stats-bot
            if ('type' in event and event['type'] == 'message' and event['channel'][0] == 'D'):
                print(event)
                try:
                    # Check if input matches format $profinfo{.*}
                    if (re.match("^\$profinfo\{.*\}$", event['text'])):
                        prof_name =  event['text'][10:-1]
                        professorURL(prof_name)
                    else:
                        sc.rtm_send_message(event['channel'], msg)
                except: 
                    pass
        time.sleep(1)
else:
    print ("Connection Failed")