import json

from flask import Flask, request
from flask_cors import CORS

import NLP

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def hello_world():
    params = json.loads(request.data)
    nlp_area_field = params.get('data').get('nlp_area_field')
    proccessed_data = NLP.getKeys(nlp_area_field)

    return json.dumps(proccessed_data)


if __name__ == '__main__':
    app.run()
