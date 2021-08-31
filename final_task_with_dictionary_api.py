from dialogflow_fulfillment import QuickReplies, WebhookClient, Payload
from flask import Flask, request, Response, jsonify , make_response
import json
import requests

app = Flask(__name__)

def handler(agent: WebhookClient) :
    """Handle the webhook request.."""

    result = {000: 'subnmitted but shipment in transit', 100 : 'submitted but tracking missing' , 111:'received' , 222: 'evaluation' , 333 : 'recovery' , 444 : 'quote prepared', 555 : 'qote not prepared'}
    case_id = list(dict.keys(result))
    #project_status = list(dict.values(result))
    date = '23-8-21'
    price = '$45'
    eta = '10-14 days'

    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')

    if intent_name == 'check_status':
        case_ID = req.get('queryResult').get('parameters').get('any') 
        print(type(case_ID))
        case_ID = int(case_ID)

        if case_ID in case_id:
            project_status= result.get(case_ID)
            if project_status == 'subnmitted but shipment in transit':
                agent.add("dummy")
                agent.set_followup_event("submitted_status_event_shipment_in_transit")

            if project_status == 'submitted but tracking missing':
                agent.add("dummy")
                agent.set_followup_event("submitted_status_event_but_tracking_missing")

            if project_status == 'received':
                agent.add("dummy")
                agent.set_followup_event("received_status_event")
                
            if project_status == 'evaluation':
                agent.add("dummy")
                agent.set_followup_event("evaluation_status_event")

            if project_status == 'recovery':
                print(case_ID)
                agent.add("dummy")
                agent.set_followup_event("recovery_status_event")

            if project_status == 'quote prepared':
                agent.add("dummy")
                agent.set_followup_event("quote_prepared_event")
                
            if project_status == 'qote not prepared':
                agent.add("dummy")
                agent.set_followup_event("quote_not_prepared_event")   

        else: 
            agent.add("dummy")
            agent.set_followup_event("case_id_not_found")


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    """Handle webhook requests from Dialogflow."""
    req = request.get_json(force=True)
    agent = WebhookClient(req)
    agent.handle_request(handler)
    return agent.response

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1',port=80)
   