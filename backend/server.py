from flask      import Flask, jsonify, make_response, request, abort
from flask_cors import CORS

# from bot import chatbot

app = Flask(__name__)
CORS(app)

error_payload_not_found = {"error": "payload not found"}

def error_in_result(e):
  return {"error in evaluate Result": str(e)}

def prepare_output(a):
  return { "response": str(a)}

@app.route('/')
def index():
  return "Chatbot Say Hi!"

@app.route('/ask/', methods=['POST'])
@app.route('/ask', methods=['POST'])
def evaluateResult():
  if request.json and 'request' in request.json:
    try:
      payload = request.json['request']
      print(payload)
      return jsonify(prepare_output(payload)), 201

    except Exception as e:
      print(e)
      return jsonify(error_in_result(e)), 201

  return jsonify(error_payload_not_found), 201

@app.errorhandler(400)
def payloadNotPassed(error):
  return make_response(jsonify({'error': error}), 400)

@app.errorhandler(405)
def methodNotAllowed(error):
  return make_response(jsonify({'error': 405}), 405)

@app.errorhandler(404)
def notFound(error):
  return make_response(jsonify({'error': 404}), 404)

@app.errorhandler(500)
def internalServerError(error):
  return make_response(jsonify({'error': ('Something went wrong with server' + error)}), 500)

if __name__ == '__main__':
    app.run(debug=True)
