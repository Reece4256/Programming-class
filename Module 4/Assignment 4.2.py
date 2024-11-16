# Input details
employee_name = "Jenna Jenkins"
num_shifts = 15
num_transactions = 30
transaction_value = 25000

# Calculate the productivity score
productivity_score = (transaction_value / num_transactions) / num_shifts

# Determine the bonus using a nested if statement
if productivity_score <= 30: bonus = 50.00

elif 31 <= productivity_score <= 69: bonus = 75.00

elif 70 <= productivity_score <= 199: bonus = 100.00

else: # productivity_score >= 200 
    bonus = 200.00
    
# Output the employee's name and bonus
print(f"Employee Name: {employee_name}")
print(f"Productivity Bonus: ${bonus:.2f}")