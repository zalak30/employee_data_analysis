# import libraries and module
import file
import seaborn as sns

# make object of emp from 'file' module
emp = file.emp

# box plot for 'monthly rate' vs 'Department'
fig = sns.boxplot(x=emp['Department'], y=emp['MonthlyRate'])

# save the graph
figure = fig.get_figure()
figure.savefig("DepartmentvsMonthlyrate.png", dpi=400)

"""
CONCLUSION

1.  Employees who are working in Sales have more salaries than R&D and HR.
2.  HR employees have least average salary among all three departments.

"""
