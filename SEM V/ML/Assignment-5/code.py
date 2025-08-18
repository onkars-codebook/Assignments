import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE

# 1. Load dataset
df = pd.read_csv('wine-class.csv')

# Separate features (X) and target (y)
X = df.drop(columns=['class'])
y = df['class']

print("X sample:\n", X.head())
print("\ny sample:\n", y.head())
print("Class distribution:\n", df['class'].value_counts())


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
print("Shapes:")
print("  X_train:", X_train.shape)
print("  X_test: ", X_test.shape)
print("  y_train:", y_train.shape)
print("  y_test: ", y_test.shape)
print()

print("Class distribution (train):")
print(pd.Series(y_train).value_counts().sort_index())
print("\nClass distribution (test):")
print(pd.Series(y_test).value_counts().sort_index())
print()

print("Applying smote ")

X_train_res, y_train_res = SMOTE(random_state=42).fit_resample(X_train, y_train)

print("Class distribution (train):")
print(pd.Series(y_train_res).value_counts().sort_index())

lr = LogisticRegression(max_iter=5000, multi_class='multinomial')
lr.fit(X_train_res, y_train_res)
print("Logistic Regression:\n", classification_report(y_test, lr.predict(X_test)))
