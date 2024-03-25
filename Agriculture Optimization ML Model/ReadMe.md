# 🌱 Agriculture Optimization ML Model

## Description
Agriculture Optimisation ML app performs KMeans clustering on input agricultural data to identify clustering patterns for given parameter values, and utilizes a Supervised Learning based **Logistic Regression Model** to predict the most suitable crop for specific soil and environmental conditions.

## Project Structure
- `agriculture.ipynb`: Jupyter notebook containing EDA, data visualization, clustering, and model training.
- `streamlit.py`: Interactive Streamlit frontend web app.
- `app.py`: Flask web server backend providing a REST API (`/predict`) and serving the HTML UI.
- `templates/index.html`: Responsive HTML5/CSS3 frontend web interface.
- `data.xlsx`: Dataset containing soil nutrients (N, P, K), temperature, humidity, pH, rainfall, and crop labels.
- `requirements.txt`: Python dependencies required for this project.

## Installation
```bash
cd "Agriculture Optimization ML Model"
pip install -r requirements.txt
```

## Running the Application

### Option 1: Streamlit Interface
```bash
streamlit run streamlit.py
```

### Option 2: Flask Web App
```bash
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

