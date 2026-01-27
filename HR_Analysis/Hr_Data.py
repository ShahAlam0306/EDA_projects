import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df = pd.read_excel(r'D:\Data analyst\projects\Dashboard_projects\Hr sales\HR Data Set.xlsx')
print('Original Dataset: \n',df)

df.shape
df.columns

df.head()

df.tail()

df.info()

#Checking null values 
df.isnull().sum()

# There is no null values in given Dataset 
df.duplicated().sum()

#Checking how many employees left 
df['Attrition'].value_counts()
df['Attrition'].value_counts(normalize = True)*100

#Attrition Percentage is around 16 % 
sns.countplot(x = 'Attrition' , data = df , hue = 'Gender')
plt.title('Attrition Distribution')
plt.xlabel('Attrition')
plt.ylabel('Employee count')
plt.show()

sns.histplot(df['Age'] , bins = 10 ,kde= True)
plt.title('Age Distribution of Employees')
plt.xlabel('Age')
plt.ylabel('Employee count')
plt.show()

sns.boxenplot(data = df, x = 'Age')
plt.title('Box plot')
plt.show()

sns.countplot(data = df, x = 'Department')
plt.title('Employee Distribution by Department ')
plt.xlabel('Employee Count')
plt.ylabel('Department')
plt.show('The majority of employees belong to Sales and R&D departments.')

plt.figure(figsize = (10,6))
sns.countplot(data =df ,x = 'Education Field', palette = None)
plt.xlabel('Employee Count')
plt.ylabel('Education Field')
plt.title('Employee Distribution by Education field')
plt.show()

plt.figure(figsize = (20,6))
sns.countplot(data =df ,x = 'Job Role')
plt.xlabel('Education Count')
plt.ylabel('Job Role')
plt.title('Employee Distribution by Job role')
plt.show()


plt.figure(figsize= (8,5))
sns.countplot(x = 'Department' , hue = 'Attrition' , data = df)
plt.title('Attrition By Department')
plt.xlabel('Employee Count')
plt.ylabel('Department')
plt.tight_layout()
plt.show()

print('Module 5  Bivariate Analysis')

sns.countplot(data = df, x = 'Gender' , hue = 'Attrition')
plt.title('Attrition by gender ')
plt.xlabel('Gender')
plt.ylabel('Employee Count')
plt.show()

pd.crosstab(df['Education Field'],df['Attrition'] , normalize= 'index') * 100

plt.figure(figsize = (10,6))
sns.countplot(x = 'Education Field' , hue = 'Attrition' , data = df)
plt.title('Attrition by Education Field')
plt.xlabel('Employee Count')
plt.ylabel('Education Field')
plt.show()

pd.crosstab(df['Job Satisfaction'],df['Attrition'],normalize = True) * 100
plt.figure(figsize = (10,6))
sns.countplot(x = 'Job Satisfaction', hue = 'Attrition' , data = df)
plt.title('Attrition by Job Satisfaction')
plt.xlabel('Job Satisfaction level')
plt.ylabel('Employee Count')
plt.show()

print('Module 6 : Age group - Based Attrition Analysis')
bins = [0,24,34,44,54,100]
label = ['Under 25','25-34','35-44','45-54','Over 55']
df['Age Group'] = pd.cut(df['Age'], bins = bins , labels = label)

df['Age Group'].value_counts()
pd.crosstab(df['Age Group'],df['Attrition'],normalize = True) * 100

plt.figure(figsize = (10,6))
sns.countplot(data = df, x = 'Age Group', hue = 'Attrition')
plt.title('Attrition By Age group')
plt.xlabel('Age Group')
plt.ylabel('Employee count')
plt.show()

print('Module 7 : Advance lvl')
pd.crosstab([df['Age Group'], df['Gender']], df['Attrition'],
            normalize = True) * 100
sns.catplot(x = 'Age Group' , hue = 'Attrition', data = df,kind = 'count',
            col = 'Gender',height = 4, aspect = 1)
plt.subplots_adjust(top = 0.85)
plt.suptitle('Attrition by Age Group and Gender')
plt.show()

pd.crosstab([df['Department'] ,df['Job Role']], df['Attrition'] , normalize = True )* 100
plt.figure(figsize = (10,6))
sns.countplot(y = 'Job Role',data = df,hue = 'Attrition')
plt.title('Attrition by Job Role')
plt.xlabel('Employee Count')
plt.ylabel('Job Role')
plt.tight_layout()
plt.show()
