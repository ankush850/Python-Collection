# Electricity Price Prediction

A machine learning project and FastAPI service to predict electricity costs based on site metrics, structure type, resource consumption, and environmental factors.

## Features
- **Data Pipeline**: Preprocessing with `ColumnTransformer` and `OneHotEncoder`.
- **Model Comparison**: Baseline benchmarking with Linear Regression, Decision Trees, and Random Forest.
- **Optimized Model**: Tuned `RandomForestRegressor` with 5-fold cross-validation.
- **REST API**: Built with `FastAPI` and `Pydantic` for request validation and inference.

## Installation

```bash
cd Electricity-Price-Prediction
pip install -r requirements.txt
```

## Model Training

```bash
python train.py --data electricity_cost_dataset.csv --model-output model2.pkl
```

## Running the API

```bash
uvicorn final_api:app --reload
```

Interactive API documentation will be available at `http://127.0.0.1:8000/docs`.
