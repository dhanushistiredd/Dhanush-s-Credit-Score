import streamlit as st
import joblib
import pandas as pd
from datetime import datetime

model = joblib.load('credit_score_model.pkl')



def calculate_days(loan_taken_date, due_date, repaid_date, not_repaid):
    if not_repaid:

        return -(datetime.today().date() - due_date).days, None
    else:

        return None, (due_date - repaid_date).days


def calculate_credit_score(age, education, principal, days_past_due, days_in_advance):

    data = pd.DataFrame([[age, education, principal, days_past_due, days_in_advance]],
                        columns=['age', 'education', 'Principal', 'past_due_days', 'days_in_advance'])


    data['education'] = data['education'].map({'No Education': 0, 'High school or below': 1, 'bechalor': 2})


    data = data[['age', 'education', 'Principal', 'past_due_days', 'days_in_advance']]


    score = model.predict(data)
    return score[0]



st.title("Credit Score Prediction")


age = st.number_input("Age", min_value=18, max_value=100, value=30)
education = st.radio("Education Level", ["No Education", "High school or below", "bechalor"])
principal = st.number_input("Loan Principal Amount", min_value=0, value=500)

loan_taken_date = st.date_input("Loan Taken Date", value=datetime.today())
due_date = st.date_input("Due Date", value=datetime.today())
not_repaid = st.checkbox("Loan Not Repaid")
if not_repaid:
    repaid_date = None
else:
    repaid_date = st.date_input("Repaid Date", value=datetime.today())


if st.button("Calculate Credit Score"):

    days_past_due, days_in_advance = calculate_days(loan_taken_date, due_date, repaid_date, not_repaid)


    credit_score = calculate_credit_score(age, education, principal, days_past_due, days_in_advance)


    st.write(f"Predicted Credit Score: {credit_score:.2f}")
