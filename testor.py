from flask import Flask,request,jsonify
from sklearn.externals import joblib
import numpy as np
import pandas as pd
import json

app = Flask(__name__)


@app.route("/predict",methods=['POST'])
def worker():
    #data=json.loads(request.data)
    data=request.get_json()
    age=data["Age"]
    gf=data["Gender_Female"]
    gm=data["Gender_Male"]
    years_exp=pd.DataFrame(data=np.array([[age,gf,gm]]),columns=["Age","Gender_Female","Gender_Male"])
    print(classifier.predict(years_exp)[0])
    return jsonify(classifier.predict(years_exp)[0].tolist())


if __name__ == '__main__':
    
    classifier=joblib.load("model.pkl")
    model_columns=joblib.load("model_columns.pkl")
    app.run(debug=True,port=12345)