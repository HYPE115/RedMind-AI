from flask import Flask, request, jsonify, render_template
from chat_engine import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.json['message']
    response = get_response(prompt)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000)