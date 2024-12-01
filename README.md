# Dhanush-s-Credit-Score

Hi. I decided to create my own credit score to include in my resume for my equifax interview.

I found this dataset off of kaggle that contained loan repayment data for a 500-odd observations. closest thing i could find, given my financial prowess.

It has the following features :

loan_ID - ID number for the loan
loan_status - whether the loan has been paid off, went to collection and was then paidoff, or if its still in collection.
Principal - the initial amount borrowed
effective_date - the date the amount was borrowed
due_date - the date the amount was due
paid_off_time - the date and time the amount was repaid.
past_due_days - number of days past the due date in collection_paidoff and collection cases
age - age of the borrower
education - education level of the borrower (High school or lower, Bechalor's (not Bachelor's, im not sure why), and no education)
Gender - gender of the borrower (male or female)

- Removed the loan_ID feature as it was redundant to my simple implementation.

- Using due_date and paid_off_time features in "paidoff" cases, i extracted a feature "days_in_advance" which calculated the number of days in advance in which the loan was paidoff.
- The more in advance the loan was paidoff, the better your credit score got.
- I plotted the days_in_advance values on a graph.

- ![time_difference_graph](https://github.com/user-attachments/assets/e6096a49-53aa-4ef7-81f4-031354f113e1)

- I also plotted the days past due dates for collection and collection_paidoff cases :

- ![collection_paidoff](https://github.com/user-attachments/assets/08cf24af-161e-43ed-9bb7-e9f509efd458)
- ![Collections_graph](https://github.com/user-attachments/assets/de0c1641-d987-4231-84e8-cb8c1a793162)

- I one-hot coded the education level, 
    No education - affected score less
    High school or lower - affected score moderately
    Bechalor's - little to no concession in score.

- If gender was "female," the score was affected less.

- I start with a base score of 20 and,

- If the principal ranges from 0-500,

for "PAIDOFF" entries, 

If education is, 
High school or below, +1 point
bechalor's,+0.5 point
no education, +2 point

if amount was paidoff 0-10 days in advance, +2 points
if amount was paidoff 11-20 days in advance, +4 points
if amount was paidoff 21+ days in advance, +6 points


if borrower is female, +1 point


for "COLLECTION_PAIDOFF" entries, 

If education is, 
High school or below, +0.5 point
bechalor's,+0 point
no education, +1 point

if amount was paidoff 0-20 days later, -2 points
if amount was paidoff 21-40 days later, -4 points
if amount was paidoff 41+ days later, -6 points

if borrower is female, +1 point

for "COLLECTION" entries, 

If education is, 
High school or below, +0 point
bechalor's,+0 point
no education, +0.5 point

if amount is 0-30 overdue, -4 points
if amount is 31-60 overdue, -6 points
if amount is 61+ overdue, -8 points

if borrower is female, +0.5 point



If the principal ranges from 501-999,

for "PAIDOFF" entries, 

If education is, 
High school or below, +1.5 point
bechalor's,+1 point
no education,+2 point

if amount was paidoff 0-10 days in advance, +3 points
if amount was paidoff 11-20 days in advance, +5 points
if amount was paidoff 21+ days in advance, +7 points


if borrower is female, +2 points


for "COLLECTION_PAIDOFF" entries, 

If education is, 
High school or below, +0.5 point
bechalor's,+0 point
no education, +1 point

if amount was paidoff 0-20 days later, -4 points
if amount was paidoff 21-40 days later, -6 points
if amount was paidoff 41+ days later, -8 points

if borrower is female, +1 point

for "COLLECTION" entries, 

If education is, 
High school or below, +0 point
bechalor's,+0 point
no education, +0.5 point

if amount is 0-30 overdue, -6 points
if amount is 31-60 overdue, -7 points
if amount is 60+ overdue, -9 points

if borrower is female, +0.5 point


If the principal is 1000,

for "PAIDOFF" entries, 

If education is, 
High school or below, +2 point
bechalor's,+1.5 point
no education,+3 point

if amount was paidoff 0-10 days in advance, +4 points
if amount was paidoff 11-20 days in advance, +6 points
if amount was paidoff 21+ days in advance, +8 points


if borrower is female, +2.5 points


for "COLLECTION_PAIDOFF" entries, 

If education is, 
High school or below, +0 point
bechalor's,+0 point
no education, +0.5 point

if amount was paidoff 0-20 days later, -5 points
if amount was paidoff 21-40 days later, -7 points
if amount was paidoff 41+ days later, -9 points

if borrower is female, +0.5 point

for "COLLECTION" entries, 

If education is, 
High school or below, +0 point
bechalor's,+0 point
no education, +0 point

if amount is 0-30 overdue, -6 points
if amount is 31-60 overdue, -7 points
if amount is 61+ overdue, -9 points

if borrower is female, +0.5 point


- On top of this, the older the borrower was, the more adversely would their credit score be affected.

- I now trained a RandomForestRegressor on this model, and created a frontend using streamlit to accept principal amount, age, education, loan taken date, due date and repaid date.
- if loan isnt repaid, they check a box and the repaid date disables.
- it then calculates either days in advance or days past due date and calculate credit score based on the model.
