# Heart Disease Prediction System

A full-stack web application that predicts the risk of heart disease using machine learning and provides personalized health recommendations.

## Features

- **Machine Learning Prediction**: Advanced algorithm for heart disease risk assessment
- **Interactive Dashboard**: User-friendly interface with real-time results
- **Comprehensive Analysis**: 10 critical health parameters for accurate prediction
- **Personalized Recommendations**: Customized health advice based on risk assessment
- **Responsive Design**: Works seamlessly across all devices

## Technical Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Rule-based prediction system
- **Data Processing**: NumPy, Pandas

## Project Structure

```
Heart-Disease-Prediction/
├── src/
│   ├── app.py              # Main Flask application
│   ├── train.py            # Model training script
│   └── evaluate.py         # Model evaluation script
├── models/                 # Trained models
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   └── result.html
├── static/                 # Static files
│   ├── css/
│   └── js/
└── requirements.txt        # Python dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
cd src
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Features in Detail

### Risk Assessment
- Age analysis
- Blood pressure monitoring
- Cholesterol level evaluation
- Heart rate analysis
- Exercise-induced angina detection
- ST depression analysis
- Resting ECG results
- Fasting blood sugar analysis
- Chest pain type classification
- Maximum heart rate achieved

### Health Recommendations
- Lifestyle modifications
- Dietary suggestions
- Medical consultation guidance
- Exercise recommendations
- Risk factor management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Medical professionals for their insights
- Open-source community for their contributions
- Research papers and datasets used for model development
