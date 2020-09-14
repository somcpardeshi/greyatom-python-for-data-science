# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Code starts here

#Reading the file
data=pd.read_csv(path)

#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()

#Plotting bar plot
plt.bar(loan_status.index, loan_status)
plt.show()

#Code ends here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
print(property_and_loan)
property_and_loan.plot.bar(stacked=False)
plt.xlabel("Property Area")
plt.xlabel("Loan Status")
plt.xticks(rotation=45)


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot.bar()
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)


# --------------
#Code starts here

graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
graduate.plot(kind='density',label='Graduate')
not_graduate.plot(kind='density',label='Not Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3, ncols=1)
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])



