
# Import required libraries
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, classification_report 
import pickle

# Load dataset
data = pd.read_csv("Rainfall.csv")  

# Basic preprocessing: Drop rows with missing values
data = data.dropna()

# Select features and target
# (Change column names as per your dataset if different)
X = data.drop(columns=["RainToday", "RainTomorrow"])  
y = data["RainTomorrow"]

# Convert target variable to binary format if needed
y = y.map({"Yes": 1, "No": 0})

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model
with open("rainfall_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as 'rainfall_model.pkl'")
