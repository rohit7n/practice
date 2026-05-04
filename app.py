from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route (loads HTML)
@app.route('/')
def home():
    return render_template('index.html')

# API route (for JS to call)
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Python backend!"})

# POST example (form or fetch)
@app.route('/api/send', methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(debug=True)