import pandas as pd 
import numpy as np 
#Loading dataset
dataset=pd.read_csv("Scikit_Learn\House Price Prediction\kc_house_data.csv")
print(dataset.head(10))
#splitting x and y 
x=dataset[["bedrooms","bathrooms","sqft_living","sqft_lot","floors","waterfront","view","condition","grade","sqft_above","sqft_basement","yr_built","yr_renovated","zipcode","lat","long","sqft_living15","sqft_lot15"]].values
y=dataset[["price"]].values

# Displaying shape of x & y 
print('-'*80)
print(f"Shape of x is {x.shape}\n Shape of y is {y.shape}")

#Splitting into training set and dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print('-'*80)
print(f"Length of X test {len(x_test)} \nLength of X train {len(x_train)}") 
print(f"Length of Y test {len(y_test)} \nLength of Y train {len(y_train)}") 

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="mean")
x_train = imputer.fit_transform(x_train)
x_test = imputer.transform(x_test)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train_scaled = sc.fit_transform(x_train)
x_test_scaled = sc.transform(x_test)

# Using Machine Learning Algorithms
# 1. support vector Machine (SVM)
from sklearn.svm import SVR
regressor=SVR()
print(regressor)
regressor.fit(x_train,y_train.ravel())
y_pred=regressor.predict(x_test)
from sklearn.metrics import r2_score
accuracy = r2_score(y_test, y_pred)
print("\n" + "-" * 20 + " Accuracy Score on the Test Set " + "-" * 20)
print("{:.2%}".format(accuracy))

# =========================================================
# 2. LINEAR REGRESSION
# =========================================================
from sklearn.linear_model import LinearRegression
linear_model = LinearRegression()
linear_model.fit(x_train_scaled, y_train.ravel())
y_pred_linear = linear_model.predict(x_test_scaled)
linear_accuracy = r2_score(y_test, y_pred_linear)
print("\n" + "-" * 20 + " Linear Regression Accuracy " + "-" * 20)
print("{:.2%}".format(linear_accuracy))

# =========================================================
# 3. MULTIPLE LINEAR REGRESSION
# =========================================================

# Multiple Linear Regression uses multiple input features.
# Since X contains many features, LinearRegression is
# already performing Multiple Linear Regression.

multiple_linear_model = LinearRegression()
multiple_linear_model.fit(x_train_scaled, y_train.ravel())
y_pred_multiple = multiple_linear_model.predict(x_test_scaled)
multiple_accuracy = r2_score(y_test, y_pred_multiple)
print("\n" + "-" * 20 + " Multiple Linear Regression Accuracy " + "-" * 20)
print("{:.2%}".format(multiple_accuracy))

# =========================================================
# 4. DECISION TREE REGRESSOR
# =========================================================

from sklearn.tree import DecisionTreeRegressor
decision_tree_model = DecisionTreeRegressor(
    random_state=0
)
decision_tree_model.fit(x_train, y_train.ravel())
y_pred_tree = decision_tree_model.predict(x_test)
tree_accuracy = r2_score(y_test, y_pred_tree)
print("\n" + "-" * 20 + " Decision Tree Accuracy " + "-" * 20)
print("{:.2%}".format(tree_accuracy))


# =========================================================
# 5. RANDOM FOREST REGRESSOR
# =========================================================

from sklearn.ensemble import RandomForestRegressor
random_forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=0
)
random_forest_model.fit(x_train, y_train.ravel())
y_pred_forest = random_forest_model.predict(x_test)
forest_accuracy = r2_score(y_test, y_pred_forest)
print("\n" + "-" * 20 + " Random Forest Accuracy " + "-" * 20)
print("{:.2%}".format(forest_accuracy))
