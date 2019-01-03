#%%
from flask import Flask, request, make_response, render_template, jsonify, send_file
import numpy as np
import pandas as pd
import pickle
import os

#%%
def predict_no_params(test_df):
    # read the features
    with open('features.pkl', 'rb') as fid:
           features =  pickle.load(fid)

    # converting data to required format
    test_df.dropna(inplace = True)

    String_test = test_df[0].values.tolist()
    test_input = []
    for t in String_test:
        test_input.append(t.split(' '))

    # load classifier from disk
    with open('rfc1.pkl', 'rb') as fid:
        classifier_sklearn1 = pickle.load(fid)

    # prepare predictions from classifier
    y_predict = []
    m =len(test_input)

    for index in range(m):
        y_predict.append(classifier_sklearn1.classify(get_feature_dict(test_input[index],features)))

    return y_predict

# funtion to create features dictionary based of most freq words of training set
def get_feature_dict(words,features):
    current_features = {}
    words_set = set(words)
    for w in features:
        current_features[w] = w in words_set
    return current_features

#%%
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/api/text_class_no_params", methods=['POST', 'GET'])
def text_class_no_params():

    if request.method == 'GET':
        return render_template('index.html')
    else:
        got_json = request.files['df_file']
        test_df=pd.read_csv(got_json, sep=',',header = None)
        if test_df.empty:
            return render_template("error.html", error_message='Input file does not have any data')
        else:
            test_df['Document'] = predict_no_params(test_df)
            resp = make_response(test_df.to_csv(index=False))
            resp.headers["Document"] = "attachment; filename=predictions.csv"
            resp.headers["Content-Type"] = "text/csv"
            return resp
            
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)