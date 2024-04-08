# Importing necessary libraries
import pandas as pd
import statsmodels.api as sm

# Define the file path
file_path = r'C:\Users\fitchj25\Downloads\Restaurant Revenue.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Define the dependent variables (features) and the independent variable (target)
X = df[['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 'Average_Customer_Spending', 'Promotions', 'Reviews']]
y = df['Monthly_Revenue']

# Add a constant term to the independent variables for the intercept
X = sm.add_constant(X)

# Perform multiple linear regression
model = sm.OLS(y, X).fit()

# Print the regression summary
print("\nRegression Summary:")
print(model.summary())

# Calculate correlation coefficients
correlation_coefficients = df.corr()['Monthly_Revenue'].drop('Monthly_Revenue')

# Print correlation coefficients
print("\nCorrelation Coefficients:")
print(correlation_coefficients)

# Assess the accuracy of the prediction model
predicted_monthly_revenue = model.predict(X)
df['Predicted_Monthly_Revenue'] = predicted_monthly_revenue

# Calculate percent error for each data point
percent_error = ((df['Monthly_Revenue'] - df['Predicted_Monthly_Revenue']) / df['Monthly_Revenue']) * 100

# Calculate the average percent error
average_percent_error = percent_error.mean()

# Print the average percent error
print("\nAverage Percent Error:", average_percent_error)

# Print a comparison of actual and predicted monthly revenues
print("\nComparison of Actual and Predicted Monthly Revenues:")
print(df[['Monthly_Revenue', 'Predicted_Monthly_Revenue']])
