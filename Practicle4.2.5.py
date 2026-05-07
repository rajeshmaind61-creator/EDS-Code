import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')

print(data.head())

# 2. Display the last 5 rows of the dataset

print(data.tail())

# 3. Get the shape of the dataset

print(data.shape)

# 4. Get a summary of the dataset (info)

print(data.info())


# 5. Get basic statistics of the dataset

print(data.describe())


# 6. Check for missing values

print(data.isnull().sum())

# 7. Fill missing values in the ‘Age’ column with the median age

medianage = data['Age'].median()
data['Age'] = data['Age'].fillna(medianage) 


# 8. Fill missing values in the ‘Embarked’ column with the mode
mode_embarked = data['Embarked'].mode()[0]
data['Embarked'].fillna('Embarked',inplace=True)

# 9. Drop the ‘Cabin’ column due to many missing values
data.drop(columns=['Cabin'], axis=1,inplace=True)

# 10. Create a new column 'FamilySize’ by adding ‘SibSp' and ‘Parch'
data['FamilySize'] = data['SibSp'] + data['Parch']


