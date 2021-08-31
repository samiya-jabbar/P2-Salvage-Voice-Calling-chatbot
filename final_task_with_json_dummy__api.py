from dialogflow_fulfillment import QuickReplies, WebhookClient, Payload
from flask import Flask, request, Response, jsonify , make_response
import requests, json

app = Flask(__name__)

def handler(agent: WebhookClient) :
    """Handle the webhook request.."""

    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    all_id = [000,100,111,222,333,444,555]

    url = 'https://be7e95258abe.ngrok.io/get_case'


    headers = {
        'Content-Type': 'application/json'
        }


    if intent_name == 'check_status':
        case_ID = req.get('queryResult').get('parameters').get('any')
        print(type(case_ID))
        data = {"case_id":case_ID}

        res = requests.post(url, data=json.dumps(data), headers=headers)
        project_status = json.loads(res.content)['result']['project_status']
        print(project_status)

        if project_status == 'submitted':
            project_type = json.loads(res.content)['result']['project_type']
            if project_type == 'shipment in transit':
                agent.add("dummy")
                agent.set_followup_event("submitted_status_event_shipment_in_transit")

            if project_type == 'tracking missing':
                project_type = json.loads(res.content)['result']['project_type']
                agent.add("dummy")
                agent.set_followup_event("submitted_status_event_but_tracking_missing")
            
        elif project_status == 'received':
            agent.add("dummy")
            agent.set_followup_event("received_status_event")
            
        elif project_status == 'evaluation':
            agent.add("dummy")
            agent.set_followup_event("evaluation_status_event")

        elif project_status == 'recovery':
            print(case_ID)
            agent.add("dummy")
            agent.set_followup_event("recovery_status_event")

        elif project_status == 'quote prepared':
            agent.add("dummy")
            agent.set_followup_event("quote_prepared_event")
            
        elif project_status == 'quote not prepared':
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
   
