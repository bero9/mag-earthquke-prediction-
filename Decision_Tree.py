from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np

def DecisionTreeBottom(data,pred):
    a = []
    for i in pred:
        a.append(float(i))
    predf = np.array(a).reshape(1, 3)

    # Preprocess the data (drop "place" column and keep only numerical features)
    numerical_columns = ["magnitudo", "depth", "latitude", "longitude"]
    data_numeric = data[numerical_columns]

 # Separate input features (X) and target variable (y)
    X = data_numeric.drop(columns=["magnitudo"])
    y = data_numeric["magnitudo"]

 # Split the data into a training set and a test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

 # Create the Linear Regression model
    regressor = DecisionTreeRegressor(random_state = 40) 

 # Train the model
    regressor.fit(X_train,y_train)
    y_predf = regressor.predict(predf)

   #  accuracy2=regressor.score(X_test,y_test) 
   #  MAE=metrics.mean_absolute_error(y_test, y_pred2)
   #  MSE= metrics.mean_squared_error(y_test, y_pred2)
   #  RMSE=np.sqrt(metrics.mean_squared_error(y_test, y_pred2))

    return y_predf