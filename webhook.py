#Sthefany Conceição Duquini 10/jun/2023
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Is this JSON file valid?
    if not request.is_json:
        return 'Message body is not valid JSON', 400

    # Decodes the message body as a JSON object
    json_data = request.get_json()
    print(json.dumps(json_data, indent=4))

    # Verify if the object you want is in the POST
    if 'something' not in json_data or 'thing' not in json_data['something']:
        return 'Theres no "something" in the file', 400

    # Accessing the data
    something = json_data['something']['thing']


    # Saving
    something_file = 'path/to/something.json'

    with open(something_file, 'w') as file:
        json.dump(something, file, indent=4)

    # Returning a message
    response = {'message': 'Data received'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)


