# 📘 Price Forecasting Project – README

This project focuses on forecasting future monthly prices using historical data.  
A simple machine-learning model was used to learn trends in the dataset and predict the next month’s average price.

---

## 📂 Dataset Description

- **date** → Monthly timestamp  
- **avg_monthly_price** → Average price for that month  

The dataset contains continuous monthly price values.

---

## 🧹 Data Preprocessing (Actual Steps Used)

### **1. Missing Values Check**
The dataset was checked for missing values.  
**Result:** No missing/null values were found.  
Since no missing data existed, no imputation was necessary.

---

### **2. Duplicate Records Check**
The dataset was checked for duplicate rows.  
**Result:** No duplicate records were found.  
Since duplicates can distort training, this verification step ensures the dataset is clean.

---

### **3. Outlier Detection**
Outliers were checked using the IQR method.  

**Outlier percentage found:** ≈ **2.81%**

#### **Why outliers were NOT removed?**
- The percentage was very small  
- Outliers in price data often represent genuine economic fluctuations  
- Removing them could hide important market changes  

Therefore, the dataset was left **untouched intentionally**.

---

### **4. Date Conversion & Sorting**
- Converted the **date** column into proper datetime format  
- Sorted the dataset based on chronological order  

This ensures correct time-based sequencing before modeling.

---

### **5. Feature Creation (time_index)**
A new column called **time_index** was created to represent each month numerically.

Example:  
- Month 1 → index 0  
- Month 2 → index 1  
- Month 3 → index 2  
- …  

This converts time into a numerical feature that machine-learning algorithms can use.

---

## 🤖 Model Used

### **RandomForestRegressor**
The chosen algorithm was **Random Forest Regression**.

#### **Why this algorithm?**
- Works well on non-linear data  
- Does not require feature scaling  
- Handles noise and small variations effectively  
- Easy to train and deploy  
- Provides stable predictions  

The model was trained using:

- **Feature:** `time_index`  
- **Target:** `avg_monthly_price`  

Once trained, the model was saved as a **pickle (.pkl)** file.

---

## 🔮 Forecasting Future Price
The trained model predicts the price for the **next month** by giving the next time index value to the model.

This approach provides easy and quick forecasting for deployment.

---

## 🧾 Model Deployment (Flask)

A simple Flask application was created where:

- The user enters the next month’s index  
- The model predicts the expected average price  
- The result is displayed on a webpage  

The Flask app loads the pickle model and performs real-time prediction.

---

## 🚀 Running the Project

1. Train the model using the Jupyter notebook  
2. Generate the `model.pkl` file  
3. Run the Flask application  
4. Open the app in your browser to give input and view predictions  

---

## 📁 Project Structure

- Dataset file  
- Jupyter notebook (data preprocessing + model training)  
- Trained model (pickle file)  
- Flask backend  
- HTML template for UI  

---

## ✔ Summary

This project includes:

- Complete data quality checks  
- Outlier analysis (without removal)  
- Simple feature engineering  
- Random Forest Regression training  
- Next-month forecasting  
- Deployment using Flask  
- Clean project workflow for interviews and portfolio  

