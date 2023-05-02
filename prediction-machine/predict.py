from flask import Flask, render_template, request
import requests, json, pickle, os
from sklearn.ensemble import RandomForestClassifier
import numpy as np

app = Flask(__name__)

@app.route('/predict_disease', methods=['POST'])
def diseasePredict():
    input_list = request.get_json()
    loaded_model = pickle.load(open('symptom_disease_model.pkl', 'rb'))
    test_pred = loaded_model.predict([input_list])
    pred_json = json.dumps(int(test_pred[0]))
    results_pod = os.getenv('PARSE_DISEASE')
    request_header = {"Content-Type": "application/json; charset=UTF-8"}
    requests.post(results_pod, data=pred_json, headers=request_header)
    return pred_json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
