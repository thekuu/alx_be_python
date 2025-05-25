monthly_income = int(input("Enter your monthly income:"))
monthly_expense = int(input("Enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expense
projected_saving = monthly_savings * 12 + (monthly_savings * 12 * 0.05) #Calculate the projected savings after one year, assuming a fixed interest rate
print(f"Projected savings after one year, with interest, is: ${projected_saving}.")