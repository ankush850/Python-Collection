# Netflix User Engagement Analysis

A data engineering and validation pipeline to ingest, validate, and analyze user engagement patterns on Netflix.

## Features
- **Configurable Ingestion**: Modular data loading using structured NumPy arrays.
- **Data Validation Suite**: Comprehensive schema, range, null value, and anomaly checks on raw engagement data.
- **Automated Validation Reporting**: Generates formatted terminal reports and exports reports to text files.
- **Analytics Ready**: Prepares and validates datasets for downstream behavioral analysis and modeling.

## Project Structure

```
Netflix-User-Engagement-Analysis/
├── data/
│   └── raw/
│       └── netflix_user_engagement.csv
├── src/
│   ├── config.py
│   ├── ingestion/
│   │   ├── __init__.py
│   │   └── load_dataset.py
│   ├── validation/
│   │   ├── __init__.py
│   │   ├── validate_dataset.py
│   │   └── validation_report.py
│   ├── __init__.py
│   └── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation & Setup

```bash
cd Netflix-User-Engagement-Analysis
pip install -r requirements.txt
```

## Usage

Run the main validation pipeline:
```bash
python -m src.main
```
