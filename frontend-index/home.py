from flask import Flask, render_template, request
import requests, json, pickle, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', symptom_list=retSympList())

def retSympList():  
    retList = pickle.load(open('symptom_list.pkl', 'rb'))
    return retList

@app.route('/disease_write', methods=['POST'])
def diseaseWrite():
    aList = request.get_json()
    sympList = pickle.load(open('symptom_dict.pkl', 'rb'))
    retList = []
    for x in range(0, 17):
        if (x < len(aList)):
            retList.append(sympList[aList[x]])
        else:
            retList.append(1)
    symptom_json = json.dumps(retList)
    prediction_pod = os.getenv('PREDICT_DISEASE')
    request_header = {"Content-Type": "application/json; charset=UTF-8"}
    requests.post(prediction_pod, data=symptom_json, headers=request_header)
    bList = json.loads(symptom_json)
    return symptom_json

@app.route('/disease_information', methods=['POST'])
def diseaseInfo():
    input_dict = request.get_json()
    pickle.dump(input_dict['Disease'], open('disease.pkl', 'wb'))
    pickle.dump(input_dict['Information'], open('information.pkl', 'wb'))
    pickle.dump(input_dict['Recommendation'], open('recommendation.pkl', 'wb'))
    return "200"

@app.route('/display_prediction', methods=['GET'])
def display():
    disease = pickle.load(open('disease.pkl', 'rb'))
    information = pickle.load(open('information.pkl', 'rb'))
    recommendation = pickle.load(open('recommendation.pkl', 'rb'))
    return render_template('diseases.html', disease_preded=disease,\
                           disease_info=information, disease_recs= recommendation)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
