from flask import Flask, request, jsonify, render_template, send_from_directory
import joblib
import numpy as np
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Create a simple model instead of loading
scaler = StandardScaler()
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Create Flask app
app = Flask(__name__, 
            static_folder='../static',
            template_folder='../templates')

# Define feature names manually
feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Define the 10 essential features we'll collect from users (added 5 more)
essential_features = ['age', 'sex', 'cp', 'trestbps', 'thalach', 'chol', 'fbs', 'restecg', 'exang', 'oldpeak']

# Feature descriptions for the form
feature_descriptions = {
    'age': 'Age (years)',
    'sex': 'Sex (1 = Male, 0 = Female)',
    'cp': 'Chest Pain Type (0-3)',
    'trestbps': 'Resting Blood Pressure (mm Hg)',
    'thalach': 'Maximum Heart Rate Achieved (bpm)',
    'chol': 'Serum Cholesterol (mg/dl)',
    'fbs': 'Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)',
    'restecg': 'Resting ECG Results (0-2)',
    'exang': 'Exercise Induced Angina (1 = yes; 0 = no)',
    'oldpeak': 'ST Depression Induced by Exercise'
}

# Feature tooltips for additional explanation
feature_tooltips = {
    'cp': '0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic',
    'restecg': '0 = Normal, 1 = ST-T Wave Abnormality, 2 = Left Ventricular Hypertrophy',
    'fbs': 'Whether fasting blood sugar is greater than 120 mg/dl',
    'exang': 'Whether exercise induced angina (chest pain) occurred',
    'oldpeak': 'ST depression induced by exercise relative to rest'
}

# Recommendations based on prediction
recommendations = {
    'lifestyle': [
        'Engage in regular moderate exercise (at least 150 minutes per week)',
        'Maintain a healthy weight',
        'Quit smoking and avoid secondhand smoke',
        'Limit alcohol consumption',
        'Manage stress through meditation, yoga, or other relaxation techniques'
    ],
    'diet': [
        'Follow a heart-healthy diet rich in fruits, vegetables, and whole grains',
        'Limit saturated fats, trans fats, and cholesterol',
        'Reduce sodium intake to less than 2,300 mg per day',
        'Limit added sugars and processed foods',
        'Consider the DASH or Mediterranean diet plans'
    ],
    'medical': [
        'Schedule an appointment with your doctor as soon as possible',
        'Discuss your risk factors and symptoms with your healthcare provider',
        'Consider getting a complete lipid profile and other heart-related tests',
        'Follow your doctor\'s recommendations for medications or treatments',
        'Monitor your blood pressure and cholesterol regularly'
    ]
}

@app.route('/')
def index():
    return render_template('index.html', 
                          features=essential_features,
                          descriptions=feature_descriptions,
                          tooltips=feature_tooltips)

@app.route('/predict', methods=['POST'])
def predict():
    if request.content_type == 'application/json':
        # API request
        data = request.json
        features_dict = data['features']
    else:
        # Form submission
        features_dict = {}
        for feature in essential_features:
            features_dict[feature] = float(request.form.get(feature))
    
    # Create a complete feature vector with default values for non-essential features
    full_features = {}
    for feature in feature_names:
        if feature in features_dict:
            full_features[feature] = features_dict[feature]
        else:
            # Use default values for non-essential features
            # These are median values from the dataset
            default_values = {
                'slope': 1,
                'ca': 0,
                'thal': 2
            }
            full_features[feature] = default_values.get(feature, 0)
    
    # Convert to numpy array in the correct order
    features_array = np.array([full_features[f] for f in feature_names]).reshape(1, -1)
    
    # Enhanced rule-based prediction with all 10 features
    risk_score = 0
    # Original 5 features
    if full_features['age'] > 60:
        risk_score += 1
    if full_features['sex'] == 1:
        risk_score += 1
    if full_features['cp'] > 1:
        risk_score += 1
    if full_features['trestbps'] > 140:
        risk_score += 1
    if full_features['thalach'] < 150:
        risk_score += 1
    
    # Additional 5 features
    if full_features['chol'] > 240:
        risk_score += 1
    if full_features['fbs'] == 1:
        risk_score += 1
    if full_features['restecg'] > 0:
        risk_score += 1
    if full_features['exang'] == 1:
        risk_score += 1
    if full_features['oldpeak'] > 1.0:
        risk_score += 1
    
    prediction = 1 if risk_score >= 5 else 0
    probability = risk_score / 10.0
    
    if request.content_type == 'application/json':
        return jsonify({
            "prediction": prediction,
            "probability": probability,
            "recommendations": recommendations if prediction == 1 else {}
        })
    else:
        return render_template('result.html', 
                              prediction=prediction,
                              probability=probability,
                              recommendations=recommendations)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('../templates', exist_ok=True)
    os.makedirs('../static/css', exist_ok=True)
    os.makedirs('../static/js', exist_ok=True)
    
    app.run(debug=True)
