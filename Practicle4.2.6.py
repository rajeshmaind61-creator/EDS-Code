import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']

data['isAlone']=(data['FamilySize']==0).astype(int)

# 2. Convert ‘Sex' to numeric (male: 0, female: 1)
data['Sex']=data['Sex'].map({'male':0,'female':1 })

# 3. One-hot encode the ‘Embarked' column
data=pd.get_dummies(data,columns=['Embarked'],drop_first=True)

# 4. Get the mean age of passengers
mean_age=data['Age'].mean()


# 5. Get the median fare of passengers
median_fare=data['Fare'].median()


# 6. Get the number of passengers by class
pasenger_by_class=data['Pclass'].value_counts()


# 7. Get the number of passengers by gender
pasenger_by_gender=data['Sex'].value_counts()


# 8. Get the number of passengers by survival status
passenger_by_survival=data['Survived'].value_counts()


# 9. Calculate the survival rate
survival_rate=data['Survived'].mean()


# 10. Calculate the survival rate by gender
survival_rate_by_gender=data.groupby('Sex')['Survived'].mean()

print(mean_age)
print(median_fare)
print(pasenger_by_class)
print(pasenger_by_gender)
print(passenger_by_survival)
print(survival_rate)
print(survival_rate_by_gender)