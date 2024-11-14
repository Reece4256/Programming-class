# input statements
salary = float(input("Please input salary"))
numDependents = float(input("Please enter dependents"))

# calculate taxes here

#State withholding tax
stateTax = salary * 0.065

#Federal withholding tax
federalTax = salary * 0.28

#Calculate dependent deductions
dependentDeduction = salary * 0.025 * numDependents

#Calcualte total withholding
totalWithholding = stateTax + federalTax + dependentDeduction

#Take-home pay
takeHomePay = salary - totalWithholding

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
print(f"State Tax: ${stateTax:.2f}")
print(f"Federal Tax: ${federalTax:.2f}")
print(f"Dependent Deduction: ${dependentDeduction:.2f}")
