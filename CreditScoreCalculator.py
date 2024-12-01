import pandas as pd

file_path = r"C:\Users\dhanu\Downloads\archive\Loan payments data.csv"
data = pd.read_csv(file_path)

data_cleaned = data.drop(columns=['Loan_ID', 'terms'])

data_cleaned['paid_off_time'] = pd.to_datetime(data_cleaned['paid_off_time'], errors='coerce').dt.date
data_cleaned['due_date'] = pd.to_datetime(data_cleaned['due_date'], errors='coerce').dt.date

def calculate_days_in_advance(row):
    if row['loan_status'] == "PAIDOFF" and pd.notnull(row['paid_off_time']) and pd.notnull(row['due_date']):
        return (row['due_date'] - row['paid_off_time']).days
    return None

data_cleaned['days_in_advance'] = data_cleaned.apply(calculate_days_in_advance, axis=1)

def calculate_credit_score(row):
    score = 20
    loan_status = row['loan_status']
    principal = row['Principal']
    education = row['education']
    paid_off_time = pd.to_datetime(row['paid_off_time'], errors='coerce')
    due_date = pd.to_datetime(row['due_date'], errors='coerce')
    past_due_days = row['past_due_days']
    gender = row['Gender']
    age = row['age'] if 'age' in row else None

    if loan_status == "PAIDOFF":
        if education == "No Education":
            score += 2 if principal <= 500 else (3 if principal == 1000 else 0.5)
        elif education == "bechalor":
            score += 0.5 if principal <= 500 else (1 if principal == 1000 else 0)
        else:
            score += 1 if principal <= 500 else (1.5 if principal > 500 else 0)
        if pd.notnull(paid_off_time):
            days_advance = (due_date - paid_off_time).days
            if 0 <= days_advance <= 10:
                score += 2 if principal <= 500 else (3 if principal <= 999 else 4)
            elif 11 <= days_advance <= 20:
                score += 4 if principal <= 500 else (5 if principal <= 999 else 6)
            elif days_advance > 20:
                score += 6 if principal <= 500 else (7 if principal <= 999 else 8)
        if gender == "female":
            score += 1 if principal <= 500 else (2 if principal <= 999 else 2.5)

    elif loan_status == "COLLECTION_PAIDOFF":
        if education == "No Education":
            score += 1 if principal <= 999 else 0.5
        elif education == "bechalor":
            score += 0 if principal <= 999 else 0
        else:
            score += 0.5 if principal <= 999 else 0
        if pd.notnull(past_due_days):
            if 0 <= past_due_days <= 20:
                score -= 2 if principal <= 999 else 4
            elif 21 <= past_due_days <= 40:
                score -= 4 if principal <= 999 else 6
            elif past_due_days > 40:
                score -= 6 if principal <= 999 else 8
        if gender == "female":
            score += 1 if principal <= 999 else 1
        if age is not None:
            if 0 <= age <= 30:
                score -= 0
            elif 31 <= age <= 60:
                score -= 2
            elif age >= 61:
                score -= 3

    elif loan_status == "COLLECTION":
        if education == "No Education":
            score += 0.5 if principal <= 999 else 0
        elif education == "bechalor":
            score += 0 if principal <= 999 else 0
        else:
            score += 0 if principal <= 999 else 0
        if pd.notnull(past_due_days):
            if 0 <= past_due_days <= 30:
                score -= 4 if principal <= 999 else 6
            elif 31 <= past_due_days <= 60:
                score -= 6 if principal <= 999 else 7
            elif past_due_days > 60:
                score -= 8 if principal <= 999 else 9
        if gender == "female":
            score += 0.5 if principal <= 999 else 0.5
        if age is not None:
            if 0 <= age <= 30:
                score -= 2
            elif 31 <= age <= 60:
                score -= 4
            elif age >= 61:
                score -= 6

    return score

data_cleaned['credit_score'] = data_cleaned.apply(calculate_credit_score, axis=1)

output_file_path = r"C:\Users\dhanu\Downloads\archive\Filtered_Loan_Data_With_Credit_Score.csv"
data_cleaned.to_csv(output_file_path, index=False)
