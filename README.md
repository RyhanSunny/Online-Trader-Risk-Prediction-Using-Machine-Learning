# Online Trader Risk Prediction

### Author: Sajib Rayhan Suny
### Student ID: N01654285

## Overview

This repository contains Python programs for data preprocessing and classification to predict the risk of default payment for online purchase orders in an online trader's dataset. The code is organized into sections for data preprocessing, model training and evaluation, cost calculation, and test data prediction. This README provides instructions on how to use the programs.

## Prerequisites

Make sure you have the following libraries installed in your Python environment:

- pandas
- numpy
- scikit-learn
- joblib

You can install these libraries using pip:

```bash
pip install pandas numpy scikit-learn joblib
```
## Usage

### 1. Data Preprocessing

The `preprocess_data` function in the `data_processing.py` script performs data preprocessing on the training and test datasets. Follow these steps:

- Replace "risk-train.txt" and "risk-test.txt" with the actual file paths to your training and test datasets.
- Run the `data_processing.py` script to preprocess the data.

### 2. Model Training and Evaluation

The `model_training.py` script trains a Random Forest Classifier and evaluates its performance using the validation set. Follow these steps:

- Ensure that the data preprocessing is completed.
- Run the `model_training.py` script to train and evaluate the model.
- The script will print a confusion matrix and a classification report for model evaluation.

### 3. Cost Calculation and Model Saving

The `cost_calculation.py` script calculates misclassification costs and saves the trained model and pipeline for future use. Follow these steps:

- Ensure that the model training and evaluation are completed.
- Run the `cost_calculation.py` script to calculate misclassification costs and save the model and pipeline.

### 4. Test Data Prediction

The `test_data_prediction.py` script loads the saved model and pipeline, preprocesses the test data, and predicts the risk of default payment. Follow these steps:

- Ensure that the cost calculation is completed.
- Replace "risk-test.txt" with the actual file path to your test dataset.
- Run the `test_data_prediction.py` script to predict the risk for the test data.
- The predictions will be saved in a text file named "test_predictions2.txt".

## Additional Information

- The code uses a cost matrix to account for different costs of misclassifications. Make sure to adjust the cost matrix in the `cost_calculation.py` script if needed.

- You can customize the code further by adjusting the preprocessing steps, model hyperparameters, and evaluation metrics as per your requirements.

- Feel free to explore the code files for more details on data preprocessing, model training, and prediction.
