# 🏠 California Housing Price Prediction

## 📌 Project Overview
This project focuses on predicting housing prices using the California Housing dataset. Various data preprocessing, feature engineering, and machine learning techniques were applied to improve model performance.

## 📊 Dataset
- Source: Kaggle - California Housing Prices
- Features include:
  - Median Income
  - Total Rooms
  - Population
  - Ocean Proximity, etc.

## ⚙️ Steps Performed
- Data Cleaning (Handling missing values)
- Outlier Detection (IQR, Z-score)
- Feature Engineering (Log Transformation)
- Encoding (One-Hot Encoding)
- Scaling (StandardScaler, MinMaxScaler)
- Feature Selection (Sequential Feature Selector)
- Model Training

## 🤖 Models Used
- Linear Regression
- Ridge Regression
- Lasso Regression
- Polynomial Regression
- Gradient Boosting Regressor

## 📊 Model Comparison

| Model | Train Score | Test Score |
|------|------------|-----------|
| Linear Regression | 0.643 | 0.598 |
| Ridge Regression | 0.642 | 0.608 |
| Lasso Regression | 0.643 | 0.601 |
| Polynomial Regression | 0.737 | 0.704 |
| Gradient Boosting | 0.827 | 0.792 |

👉 Best model: Gradient Boosting (highest test accuracy with low overfitting)

## 📈 Results
- Best Model: Gradient Boosting
- Training Score: ~0.82
- Testing Score: ~0.79

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

## 🚀 Future Improvements
- Hyperparameter tuning
- Try XGBoost / LightGBM
- Deploy model using Flask or Streamlit

## 👨‍💻 Author
Ch Srinidhi
