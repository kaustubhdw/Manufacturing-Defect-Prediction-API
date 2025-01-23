from flask import Flask, request, jsonify 
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import accuracy_score, f1_score 
import os 
import joblib 
app = Flask(__name__) 
MODEL_PATH = "model.pkl" 
SCALER_PATH = "scaler.pkl" 
DATA_PATH = "data.csv" 
@app.route('/upload', methods=['POST']) 
def upload_data(): 
    if 'file' not in request.files: 
        return jsonify({"error": "No file uploaded"}), 400 
    file = request.files['file'] 
    data = pd.read_csv(file) 
    data.to_csv(DATA_PATH, index=False) 
    return jsonify({"message": "File uploaded successfully.", "columns": list(data.columns)}) 
@app.route('/train', methods=['POST']) 
def train_model(): 
    if not os.path.exists(DATA_PATH): 
        return jsonify({"error": "No dataset uploaded. Use /upload to upload a dataset first."}), 400 
    data = pd.read_csv(DATA_PATH) 
    X = data.drop(columns=['DefectStatus']) 
    y = data['DefectStatus'] 
    scaler = StandardScaler() 
    X_scaled = scaler.fit_transform(X) 
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42) 
    model = LogisticRegression() 
    model.fit(X_train, y_train) 
    y_pred = model.predict(X_test) 
    accuracy = accuracy_score(y_test, y_pred) 
    f1 = f1_score(y_test, y_pred) 
    joblib.dump(model, MODEL_PATH) 
    joblib.dump(scaler, SCALER_PATH) 
    return jsonify({"message": "Model trained successfully.", "accuracy": accuracy, "f1_score": f1}) 
@app.route('/predict', methods=['POST']) 
def predict(): 
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH): 
        return jsonify({"error": "Model not trained. Use /train to train the model first."}), 400 
    model = joblib.load(MODEL_PATH) 
    scaler = joblib.load(SCALER_PATH) 
    input_data = request.json 
    if input_data is None: 
        return jsonify({"error": "No input data provided."}), 400 
    input_df = pd.DataFrame([input_data]) 
    input_scaled = scaler.transform(input_df) 
    prediction = model.predict(input_scaled)[0] 
    confidence = np.max(model.predict_proba(input_scaled)) 
    return jsonify({"Downtime": "Yes" if prediction == 1 else "No", "Confidence": round(confidence, 2)}) 
if __name__ == '__main__': 
    app.run(debug=True)