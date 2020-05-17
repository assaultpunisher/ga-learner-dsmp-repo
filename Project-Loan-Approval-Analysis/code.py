# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 

# code starts here

bank = pd.read_csv(path)
print(bank.head())

categorical_var = bank.select_dtypes(include='object')
print(categorical_var.head())

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.head())

# code ends here


# --------------
# code starts here

banks = bank.drop(['Loan_ID'],axis=1)

print(banks.isnull().sum())

bank_mode = banks.mode()

banks['Gender'].fillna(bank_mode['Gender'][0],inplace=True)
banks['Married'].fillna(bank_mode['Married'][0],inplace=True)
banks['Dependents'].fillna(bank_mode['Dependents'][0],inplace=True)
banks['Education'].fillna(bank_mode['Education'][0],inplace=True)
banks['Self_Employed'].fillna(bank_mode['Self_Employed'][0],inplace=True)
banks['ApplicantIncome'].fillna(bank_mode['ApplicantIncome'][0],inplace=True)
banks['CoapplicantIncome'].fillna(bank_mode['CoapplicantIncome'][0],inplace=True)
banks['LoanAmount'].fillna(bank_mode['LoanAmount'][0],inplace=True)
banks['Loan_Amount_Term'].fillna(bank_mode['Loan_Amount_Term'][0],inplace=True)
banks['Credit_History'].fillna(bank_mode['Credit_History'][0],inplace=True)
banks['Property_Area'].fillna(bank_mode['Property_Area'][0],inplace=True)
banks['Loan_Status'].fillna(bank_mode['Loan_Status'][0],inplace=True)

print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],
                                values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)

# code ends here



# --------------
# code starts here

loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]

loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]

Loan_Status = 614

percentage_se = (len(loan_approved_se)/Loan_Status)*100
print(percentage_se)

percentage_nse = (len(loan_approved_nse))*100/Loan_Status
print(percentage_nse)

# code ends here


# --------------
# code starts here

loan_term  = banks['Loan_Amount_Term'].apply(lambda x: x/12)
print(loan_term.head())

big_loan_term = len(banks[banks['Loan_Amount_Term']>=25*12])
print(big_loan_term)

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()
print(mean_values)

# code ends here


