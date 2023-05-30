import requests #to establish connection & communicate with API of this program.
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign' #URL for sending message campaign

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType, #there are two usetypes; we will be suing stage as it is used for testing purpose.
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, '4ZLQV0YFX4RV57XIYRHDFWAKBICJPPIB', 'QM92G10OTXQI1X5R', 'stage', '8639721535', 'ranamozammil9@gmail.com', 'Love you, Mozammil. I am Kajal, cannot forget you.' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)
