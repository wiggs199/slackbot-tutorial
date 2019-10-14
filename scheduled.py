import os
import schedule
import time
import logging
from slack import WebClient

import http.client
import json
import click





logging.basicConfig(level=logging.DEBUG)

def sendMessage(slack_client, msg):
  # make the POST request through the python slack client
  updateMsg = slack_client.chat_postMessage(
    channel = 'CM6SPAZJ9',
    text = msg
  )

  # check if the request was a success
  if updateMsg['ok'] is not True:
    logging.error(updateMsg)
  else:
    logging.debug(updateMsg)

if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
  slack_client = WebClient(SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  # For testing

  connection = http.client.HTTPConnection('api.football-data.org')
  headers = { 'X-Auth-Token': 'bb8307273e0a4dc796a6eaa4eb600130' }
  connection.request('GET', '/v2/competitions/SA/scorers',None, headers )
  response = json.loads(connection.getresponse().read().decode())

# Record all keys to the terminal
  for key , value in response.items():
    print(response.keys())


# Best 10 scores of Italy's top league
  def teamschedule():

      name_list = ""

      if response["count"] == 0 :

        print("No games today !")
  
      if response["count"] >= 1: 

        response_data = response

      for item in response_data['scorers']:

      #  print(item["player"]["name"])



        name_list += item["player"]["name"] + "\n"


      #  print(item["player"])

      # print(name_list)

      return("The top 10 scorers of Italy's top league are : " + "\n" + name_list )

         


  msg = teamschedule()
  schedule.every(60).seconds.do(lambda: sendMessage(slack_client, msg))


  # schedule.every().monday.at("13:15").do(lambda: sendMessage(slack_client, msg))
  logging.info("Retrieving Schedule")

  while True:
    schedule.run_pending()
    time.sleep(5) # sleep for 5 seconds between checks on the scheduler
