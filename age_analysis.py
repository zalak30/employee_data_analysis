# import libraries and module
import file
import seaborn as sns
import matplotlib.pyplot as plt

# make object of emp from 'file' module
emp = file.emp

# check employee of minimum and maximum age.
min_age_emp = emp['Age'].min()
max_age_emp = emp['Age'].max()

# distribution plot for 'age'
fig = sns.distplot(x=emp['Age'])
# plt.show()

# save the graph
figure = fig.get_figure()
figure.savefig("age.png", dpi=400)

"""
CONCLUSION

1.  Younger employee is 18 years old and oldest is 60.
2.  Maximum group of 165 employees who are between 26 to 29.
3.  Most employees are between 26 to 40.

"""