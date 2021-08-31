from flask import Flask, request, jsonify
app = Flask(__name__)


data = [
    {
        'case_id': 000,
        'project_status': 'submitted',
        'project_type': 'shipment in transit'
    },
    {   
        'case_id': 100,
        'project_status': 'submitted',
        'project_type': 'tracking missing'
    },
    {
        'case_id': 111,
        'project_status': 'received'
    },
    {
        'case_id': 222,
        'project_status': 'evaluation'
    },
    {
        'case_id': 333.0,
        'project_status': 'recovery'
    },
    {
        'case_id': 444,
        'project_status': 'quote prepared'
    },
    {
        'case_id': 555,
        'project_status': 'quote not prepared'
    }
]

@app.route('/<get_case>', methods=['GET', 'POST'])
def add_message(get_case):
    content = request.json
    print(content)
    a=content['case_id']
    print(type(a))
    if content['case_id'] == data[0]['case_id']:
        result= data[0]

    if content['case_id'] == data[1]['case_id']:
        result= data[1]

    if content['case_id'] == data[2]['case_id']:
        result= data[2]

    if content['case_id'] == data[3]['case_id']:
        result= data[3]

    if content['case_id'] == data[4]['case_id']:
        result= data[4]

    if content['case_id'] == data[5]['case_id']:
        result= data[5]

    if content['case_id'] == data[6]['case_id']:
        result= data[6]

    return jsonify({"result": result})

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1',port=12345)

