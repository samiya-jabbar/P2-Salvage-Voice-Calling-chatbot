from dialogflow_fulfillment import WebhookClient
from flask import Flask, request, Response, jsonify , make_response
import json
import requests

app = Flask(__name__)

def handler(agent: WebhookClient) :
    """Handle the webhook request.."""

    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')

    if intent_name == 'convo_start':
        agent.add('Thanks for calling Salvage data')

    confidence = 2
    x=3 
    url = "http://65fce20f910c.ngrok.io/get_case"

    headers = {
        'Content-Type': 'application/json',
        'x-salvagedata-api-key' : '426ecdf5-31bd-4b75-b529-12ed523cd6db' 
        }

    if intent_name == 'check_status':
      
        case_ID = req.get('queryResult').get('queryText')

        payload = { 
        "projectname" :  case_ID
        }
        
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        #ID = json.loads(r.content)['result']['projectname']
        project_status = json.loads(r.content)['result']['projectstatus']
        print('project_status')

        if  case_ID != ID:
            agent.add('I can not find this case in our system. Could you spell it for me?')

        if project_status == "Quote":
            agent.add(f'I see that we have evaluated your device and deemed that the recovery of your critical data is possible. Our engineers gave a {confidence} that recovery would be successful and expect a difficulty of the recovery to be {x} on the scle of 1 to 12 per device.')
            #agent.setFollowupEvent("transfer_call")


        if project_status == 'file list review':
            agent.add('I see that we have successfully been able to recover your data and have posted a file list for you to review what have been recovered. You may view it at any point by logging into your portal online.')

        if project_status == 'recovery':
            agent.add(f'I see that we have began efforts to recover your data with expected completion of {data}. we apologize for the delay as it seems the case has been more complex than anticipated. Assigned recovery engineer is expecting to have an update by %next_update_due%')

        if project_status == 'recieved':
            agent.add('I see that we have received your media for evaluation but there seems to be an exception in getting the case processed. Let me get you to someone who can help')


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    """Handle webhook requests from Dialogflow."""
    # Get WebhookRequest object
    req = request.get_json(force=True)
    # Handle request
    agent = WebhookClient(req)
    agent.handle_request(handler)
    return agent.response

if __name__ == '__main__':
    app.run(debug=True)
