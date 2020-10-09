# import libraries and module
import file
import seaborn as sns

# make object of emp from 'file' module
emp = file.emp
print(emp['EducationField'].value_counts())


# box plot for 'Education field' vs 'Age'.
fig = sns.boxplot(x=emp['EducationField'], y=emp['Age'])

# save the graph
figure = fig.get_figure()
figure.savefig("EducationField.png", dpi=400)

"""
CONCLUSION

1.  There are five types of education of employees.
2.  Employees above 35 are from marketing field and employees who are below 30 are from technical background.
3.  Least employees are from HR field and most employees are from 'LIFE SCIENCES' field.
4.  Out of 1470 employees, 606 are from 'Life Sciences' field, 464 from Medical,
    159 from Marketing, 132 from Technical Degree, 82 employee's from unknown field
    and 27 from Human Resources 
    
"""
