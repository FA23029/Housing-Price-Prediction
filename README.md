# 🏠 California Housing Price Prediction

## 📌 Project Overview

This project predicts California housing prices using Machine Learning techniques. It covers the complete machine learning pipeline, including data preprocessing, feature engineering, model comparison, and a Flask-based web application for real-time house price prediction.

---

## 📊 Dataset

**Source:** Kaggle – California Housing Prices

### Features

* Longitude
* Latitude
* Housing Median Age
* Total Rooms
* Total Bedrooms
* Population
* Households
* Median Income
* Ocean Proximity

**Target Variable:**

* Median House Value

---

## ⚙️ Machine Learning Workflow

* Data Cleaning and Missing Value Handling
* Exploratory Data Analysis (EDA)
* Outlier Detection using IQR
* Log Transformation for Skewed Features
* One-Hot Encoding of Categorical Features
* Feature Scaling using StandardScaler
* Model Training and Evaluation
* Model Comparison
* Deployment using Flask

---

## 🤖 Machine Learning Models

* Linear Regression
* Ridge Regression
* Lasso Regression
* Polynomial Regression
* Gradient Boosting Regressor

---

## 📊 Model Performance

| Model                       | Training Score (R²) | Testing Score (R²) |
| --------------------------- | ------------------: | -----------------: |
| Linear Regression           |               0.643 |              0.598 |
| Ridge Regression            |               0.642 |              0.608 |
| Lasso Regression            |               0.643 |              0.601 |
| Polynomial Regression       |               0.737 |              0.704 |
| Gradient Boosting Regressor |           **0.827** |          **0.792** |

### ✅ Best Performing Model

**Gradient Boosting Regressor**

* Training Score: **0.827**
* Testing Score: **0.792**

The Gradient Boosting model achieved the highest prediction accuracy while maintaining good generalization on unseen data.

---

## 🌐 Flask Web Application

A responsive Flask web application was developed to make predictions in real time.

Users can:

* Enter housing information
* Select Ocean Proximity
* Predict estimated house prices instantly
* View the prediction through a clean and interactive interface

---

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* HTML
* CSS

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/FA23029/Housing-Price-Prediction.git
cd Housing-Price-Prediction
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the Flask application

```bash
python app.py
```

### 4. Open your browser

Visit:

```
http://127.0.0.1:5000/
```

Enter the housing details and click **Predict House Price** to get the estimated property value.

---

## 📁 Project Structure

```
Housing-Price-Prediction/
│
├── app.py
├── Housing_Price_Prediction.ipynb
├── model.pkl
├── housing.csv
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```


## 🚀 Future Improvements

* Hyperparameter tuning using GridSearchCV or RandomizedSearchCV
* Experiment with XGBoost and LightGBM
* Deploy the application on Render or another cloud platform
* Add feature importance visualization
* Improve input validation and error handling

---

## 👨‍💻 Author

**Ch. Srinidhi**
