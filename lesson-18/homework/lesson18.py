#Homework 2:

df = pd.read_csv('task\\stackoverflow_qa.csv')
df.head()

import pandas as pd


df['creationdate'] = pd.to_datetime(df['creationdate'], errors='coerce')

# 1. 
q1 = df[df['creationdate'].dt.year < 2014]

# 2. 
q2 = df[df['score'] > 50]

# 3. 
q3 = df[(df['score'] >= 50) & (df['score'] <= 100)]

# 4. 
q4 = df[df['ans_name'] == "Scott Boston"]

# 5. 
users = ["unutbu", "Mike Pennington", "doug", "Demitri", "Jason Strimpel"] 
q5 = df[df['ans_name'].isin(users)]

# 6. 
q6 = df[(df['creationdate'].between("2014-03-01", "2014-10-31")) &
        (df['ans_name'] == "unutbu") &
        (df['score'] < 5)]

# 7. 
q7 = df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]

# 8. 
q8 = df[df['ans_name'] != "Scott Boston"]

#Homework 3:

titanic_df = pd.read_csv("task\\titanic.csv")
titanic_df.head()

import pandas as pd

# 1. 
female_class1_20_30 = df[(df['Sex'] == 'female') & (df['Pclass'] == 1) & (df['Age'].between(20, 30))]

# 2. 
fare_above_100 = df[df['Fare'] > 100]

# 3. 
survived_alone = df[(df['Survived'] == 1) & (df['SibSp'] == 0) & (df['Parch'] == 0)]

# 4. 
embarked_c_fare_above_50 = df[(df['Embarked'] == 'C') & (df['Fare'] > 50)]

# 5.
sibsp_parch = df[(df['SibSp'] > 0) & (df['Parch'] > 0)]

# 6. 
age15_not_survived = df[(df['Age'] <= 15) & (df['Survived'] == 0)]

# 7. 
cabin_fare_above_200 = df[df['Cabin'].notna() & (df['Fare'] > 200)]

# 8. 
odd_passenger_id = df[df['PassengerId'] % 2 == 1]

# 9. 
unique_tickets = df[df['Ticket'].map(df['Ticket'].value_counts()) == 1]

# 10.
miss_class1 = df[(df['Name'].str.contains("Miss")) & (df['Pclass'] == 1) & (df['Sex'] == 'female')]
