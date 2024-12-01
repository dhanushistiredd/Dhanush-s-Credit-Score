import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

data = pd.read_csv(r"C:\Users\dhanu\Downloads\archive\Filtered_Loan_Data_With_Credit_Score.csv")


data['education'] = data['education'].map({'No Education': 0, 'High school or below': 1, 'bechalor': 2})
X = data[['age', 'education', 'Principal', 'past_due_days', 'days_in_advance']]
y = data['credit_score']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")


joblib.dump(model, 'credit_score_model.pkl')
