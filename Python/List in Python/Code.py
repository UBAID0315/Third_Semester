employee_salary = [10000,20000,60000,80000,70000,100000,65000,75000]

result = list(map(lambda salary: (salary*0.1)+salary,employee_salary))
filtered = list(filter(lambda salary: salary < 50000,result))

print(f'Employee Salary less than 50k: {filtered}')
print(f'The budget: {sum(filtered)}')
