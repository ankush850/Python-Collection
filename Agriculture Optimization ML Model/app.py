import os
from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Resolve dataset path dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data.xlsx")

# Train machine learning model on startup
data = pd.read_excel(DATA_PATH)
y = data['label']
X = data.drop(["label"], axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        req = request.get_json(force=True)
        n = float(req.get('n', 0))
        p = float(req.get('p', 0))
        k = float(req.get('k', 0))
        temperature = float(req.get('temperature', 0))
        humidity = float(req.get('humidity', 0))
        ph = float(req.get('ph', 0))
        rainfall = float(req.get('rainfall', 0))

        features = np.array([[n, p, k, temperature, humidity, ph, rainfall]])
        prediction = model.predict(features)[0]
        return jsonify({'crop': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)

