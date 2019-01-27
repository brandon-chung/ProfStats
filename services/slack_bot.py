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

# instantiate Slack client
slack_token = 'xoxb-535205496215-534355130885-NXgj2IqsGIEhanXPebaxjC1l'
sc = SlackClient(slack_token)
# starterbot's user ID in Slack
starterbot_id = None

# If connected...
if sc.rtm_connect():
    print('Connected...')

# Response to error
def error_handler(err):
    print("ERROR: " + str(err))

if sc.rtm_connect():
    while True:
        events = sc.rtm_read()
        print(events)
        for event in events:
            if ('type' in event and event['type'] == 'message'):
                print(event)
                try:
                    # Check if input matches format $profinfo{.*}
                    if (re.match("^\$profinfo\{.*\}$", event['text'])):
                        prof_name =  event['text'][10:-1]
                    # Check if channel is #slack-prof-stats-bot
                    if (event['channel'][0] == 'D'|'C'): #CFR61EQPR
                        sc.api_call(
                            "chat.postMessage",
                            channel= event['channel'],
                            text= prof_name,  #To be changed
                            user= event['user']
                            )
                    else:
                        sc.rtm_send_message(event['channel'], msg)
                except: 
                    pass
        time.sleep(1)
else:
    print ("Connection Failed")

# def dummy():
#     if input == ______:
#         result = query_RMP
#         if input is in result:
#             return "input was found in query_RMP"
#         else: 
#             new_result = query_RMP
#             if input is in new_result:
#                 return "something else..."
#             else:
#                 return "No professor found."