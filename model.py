#IMPORTS
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn import metrics


# 1. Load data
df=pd.read_csv("reservations.csv")

#DATA PREPARATION
# 2. Build label
df["label"] = (df["status"] == "checked out").astype(int)

# 3. Identify features
# 4. Train/test split  ← AQUÍ
# 5. Preprocessing pipeline
# 6. GridSearchCV (solo con X_train, y_train)
# 7. Final model = grid.best_estimator_
# 8. Evaluate on X_test

