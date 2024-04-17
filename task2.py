from flask import Flask, jsonify, render_template, request
from task1 import compute_similarity

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text1 = data['text1']
    text2 = data['text2']
    
    similarity_score = compute_similarity(text1, text2)
    
    response = {
        'text1': text1,
        'text2': text2,
        'similarity_score': similarity_score
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()

