import pandas as pd
from sklearn.metrics import roc_auc_score
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/submit', methods=['POST'])
def evaluate():
    file = request.files['file']
    prediction_df = pd.read_csv(file)
    y_pred = prediction_df['prediction'].values

    test2 = pd.read_csv("test2.csv")
    y_test = test2['SeriousDlqin2yrs'].values

    auc = roc_auc_score(y_pred, y_test)

    return f"ROC AUC score : {str(auc)}\n"