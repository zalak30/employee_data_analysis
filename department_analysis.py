# import libraries and modules
import file
import seaborn as sns

# make object of emp from 'file' module
emp = file.emp

# looking for unique values in 'DEPARTMENT' column
print(emp['Department'].value_counts())

# count plot for 'Department'
fig = sns.countplot(x='Department', hue='Gender', data=emp, palette="Set2")

# save the graph
figure = fig.get_figure()
figure.savefig("Department_graph.png", dpi=400)

"""
CONCLUSION

1.  There are three types of department here. (Research, Sales, Human Resources)
2.  Most employees are working in R&D followed by Sales and HR.

"""
