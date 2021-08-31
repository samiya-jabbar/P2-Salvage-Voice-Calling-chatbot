from flask import Flask, request, Response, jsonify , make_response
import json


app = Flask(__name__)

@app.route('/')
def welcome():
    return "WELCOME !! GET YOUR CHEQUE BOOK DETAILS"


fulfillmentMessages = [ { 'platform': 'TELEPHONY',
'telephonySynthesizeSpeech': { 'text': 'Hello World' } },
{ 'platform': 'TELEPHONY',
'telephonyTransferCall': { 'phoneNumber': '+16194784365' } },
{ 'text': { 'text': [ 'ok' ] } } ]

def testing():
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    if intent_name=='tested':
        return { 'FulfillmentMessages': [
            fulfillmentMessages ]}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(testing()))


# run the app
if __name__ == '__main__':
   app.run()

"""

return {
   'fulfillmentMessages': [
    {
        'platform': 'TELEPHONY',
        'telephonySynthesizeSpeech': { 
            'ssml': "<speak>YOUR MESSAGE GOES HERE</speak>"
        }
    }
]
}


return {
   'FulfillmentMessages': [
    {
        'platform': 'TELEPHONY',
        'telephonySynthesizeSpeech': { 
            'ssml': "<speak>YOUR MESSAGE GOES HERE</speak>"},
        "platform": "TELEPHONY", 
        "telephonyTransferCall": 
         { "phoneNumber": "+16194784365" } 
        }
]
}
"""
