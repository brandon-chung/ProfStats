"""
Slack bot. Given a specific command, responds with gameified professor information
Reference: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
           https://github.com/slackapi/python-slack-events-api/blob/master/example/example.py
           https://github.com/bchung00/Social-Growth-Bot/blob/master/bot.py
"""
import time
import re
import io
from slackclient import SlackClient
from services.getProfHTML import professorURL
from services import gameify_prof as game

# instantiate Slack client
slack_token = 'xoxb-535205496215-534355130885-jruRa9Wmhrrx9mELeMyWpKZQ' # enter access ID
sc = SlackClient(slack_token)
# starterbot's user ID in Slack
starterbot_id = None

# If connected...
if sc.rtm_connect():
    print('Connected...')

# Response to error
def error_handler(err):
    print("ERROR: " + str(err))

def print_to_slackbot(input):
    image_url = "https://i.imgur.com/Med1pYx.png" # choose file link
    attachments = [{"title":"Data Image", "image_url": image_url}] 
    sc.api_call(
    "chat.postMessage",
    channel= event['channel'],
    text= input,  #To be changed
    user= event['user'],
    attachments = attachments
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
                        prof_name = event['text'][10:-1]
                        print_to_slackbot(game.slackbot_query_print(prof_name))
                    else:
                        #sc.rtm_send_message(event['channel'], "RTM")
                        print("forloop else")
                except Exception as e:
                    print(e)
                    print("forloop except")
                    pass
        time.sleep(1)
else:
    print ("Connection Failed")