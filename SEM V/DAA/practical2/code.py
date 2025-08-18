import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("./house_data.csv")
 # <-- Use your correct file path

# Drop non-numeric or irrelevant columns
df = df.drop(columns=['id', 'date'])

# Drop rows with missing values
df = df.dropna()

# Split into features and target
X = df.drop(columns='price')
y = df['price']
feature_names = X.columns.tolist()

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Greedy Forward Feature Selection
selected_features = []
remaining_features = list(range(X.shape[1]))
best_overall_score = -np.inf

while remaining_features:
    scores = []
    for feature in remaining_features:
        trial_features = selected_features + [feature]
        model = DecisionTreeRegressor(random_state=42)
        model.fit(X_train.iloc[:, trial_features], y_train)
        preds = model.predict(X_test.iloc[:, trial_features])
        score = r2_score(y_test, preds)
        scores.append((score, feature))

    scores.sort(reverse=True)
    best_score, best_feature = scores[0]

    if best_score > best_overall_score:
        selected_features.append(best_feature)
        remaining_features.remove(best_feature)
        best_overall_score = best_score
        print(f"Added feature: {feature_names[best_feature]}, R² Score: {best_score:.4f}")
    else:
        break


final_model = DecisionTreeRegressor(random_state=42)
final_model.fit(X_train.iloc[:, selected_features], y_train)
final_preds = final_model.predict(X_test.iloc[:, selected_features])
final_score = r2_score(y_test, final_preds)


print("\nSelected features in order:")
for i in selected_features:
    print(f"- {feature_names[i]}")
print(f"\nFinal R² Score with selected features: {final_score:.4f}")
