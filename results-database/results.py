from flask import Flask, render_template, request
import requests, json, pickle, os

app = Flask(__name__)

@app.route('/disease_parse', methods=['POST'])
def diseaseParse():
    diseaseInt = request.get_json()
    disease_list = pickle.load(open('disease_list.pkl', 'rb'))
    final_disease = disease_list[diseaseInt - 1]
    disease_info_dict = pickle.load(open('disease_description.pkl', 'rb'))
    disease_information = disease_info_dict[final_disease]
    disease_recs = diseaseRecs(final_disease)
    home_pod = os.getenv('WRITE_DISEASE')
    request_header = {"Content-Type": "application/json; charset=UTF-8"}
    final_dict = {"Disease": final_disease,
                  "Information": disease_information,
                  "Recommendation": disease_recs}
    final_json = json.dumps(final_dict)
    requests.post(home_pod, data=final_json, headers=request_header)
    return final_json

def diseaseRecs(disease):
    recs = pickle.load(open('disease_recs.pkl', 'rb'))
    return recs[disease]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
