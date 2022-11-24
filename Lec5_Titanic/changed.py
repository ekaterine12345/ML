# -*- coding: utf-8 -*-
"""Titanic_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iYXe70e8ADtlhPyuoSycGWoOg-Q0NmOq
"""
import pandas as pd
import numpy as np

titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(titanic.head())

titanic.drop("PassengerId", axis=1, inplace=True)
print(titanic.head())

print(titanic.isnull().any())

titanic.describe()

titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

print(titanic.isnull().any())

# titanic.drop("Cabin",axis=1,inplace=True)
titanic['Cabin'] = titanic['Cabin'].fillna(0)
print(titanic.head())

import re
def number_taken(text):
  if text ==    0:
    return 0
  else:
    s = [float(s) for s in re.findall(r'-?\d+\.?\d*', text)]
  return s


mytext = 'i am 17 years'
print(number_taken(mytext))

titanic['Cabin'] = titanic['Cabin'].apply(number_taken)

print(titanic.head())

#titanic['Cabin']


def exact_number(var1):
    if type(var1) == int or type(var1) == float:
        return var1
    elif type(var1) == list and not var1:
        return 0
    else:
        return var1[0]

type([]) == list

for value in titanic['Cabin'].values:
    print(value)

titanic['Cabin'][1][0]

titanic['Cabin'].value_counts()

titanic['Cabin']=titanic['Cabin'].apply(exact_number)

type(5)
type([5.0]) == list

print(titanic.head())

titanic['Embarked'].value_counts()

titanic['Embarked']=titanic['Embarked'].fillna(titanic['Embarked'].value_counts().index[0])
print(titanic['Embarked'].value_counts().index[0])

print(titanic.isnull().any())

titanic['Name'][0].split(' ')[1]

titanic['Name'].str.split()[0][1]


def split_text(text):
    result = text.split(' ')[1]
    result = result.split('.')[0]
    return result

titanic["Status"] = titanic['Name'].apply(split_text)

