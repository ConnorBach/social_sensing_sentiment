import flask
from flask_cors import CORS
from getTweetSentiment import returnSentiment
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/', methods=['GET'])
def home():
    if (request.args.get('query') is None or request.args.get('query') == ''):
        return "Error: No query specified"

    return jsonify(returnSentiment(request.args.get('query')))
            #:return "THIS IS A TEST!!\n" + request.args.get('query') + "\n"

app.run()
