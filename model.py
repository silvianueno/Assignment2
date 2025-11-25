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

df=pd.read_csv("reservations.csv")

#DATA PREPARATION
# 1. Contruction of label
df["label"] = (df["status"] == "checked out").astype(int)

# 2. Data cleaning

# 3. Feature engineering

# 4. Train/Validation/Test

#MODELS 

#1. Models tested
#Regularization
#Cross Validation
#Pipeline

#METRICS


