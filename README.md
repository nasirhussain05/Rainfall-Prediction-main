# Rainfall-Prediction-main
# 🌧️ Rainfall Prediction using Machine Learning

This project predicts whether it will rain tomorrow based on current weather conditions using a machine learning classification model. It is implemented in Python with scikit-learn and uses a simplified dataset for demonstration.

---



---

## 📊 Dataset

The dataset (`Rainfall.csv`) includes the following columns:

- `MinTemp`: Minimum temperature (°C)
- `MaxTemp`: Maximum temperature (°C)
- `Humidity`: Humidity percentage (%)
- `WindSpeed`: Wind speed (km/h)
- `RainToday`: Whether it rained today (0 = No, 1 = Yes)
- `RainTomorrow`: Target variable (0 = No, 1 = Yes)

---

## ⚙️ Requirements

Install the following Python packages:

```bash
pip install pandas scikit-learn


▶️ How to Run
 1.Open the project in VS Code.

 2.Ensure Rainfall.csv and Simplified_Rainfall_Prediction.py are in the same folder.

 3.Run the script:

bash
Copy
Edit
python Simplified_Rainfall_Prediction.py
The model will:

Load the data.

Train a logistic regression classifier.

Predict and display whether it will rain tomorrow based on test data.

🧠 Model Used
Logistic Regression – suitable for binary classification tasks like predicting rain (yes/no).

📌 Output Example
plaintext
Copy
Edit
Predictions: [0 1]
Actual:      [0 1]
Accuracy:    100.00%
🚀 Author
NASIR HUSSAIN

