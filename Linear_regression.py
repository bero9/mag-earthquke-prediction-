from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np


def LinearRegresionBottom(data, pred):
    # Preprocess the data (drop "place" column and keep only numerical features)
    a = []
    for i in pred:
        a.append(float(i))
    predf = np.array(a).reshape(1, 3)
    numerical_columns = ["magnitudo", "depth", "latitude", "longitude"]
    data_numeric = data[numerical_columns]

 # Separate input features (X) and target variable (y)
    X = data_numeric.drop(columns=["magnitudo"])
    y = data_numeric["magnitudo"]

 # Split the data into a training set and a test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

 # Create the Linear Regression model
    model = LinearRegression()

 # Train the model
    model.fit(X_train, y_train)

 # Predict using the model
    y_predf = model.predict(predf)

    # accuracy1=model.score(X_test,y_test)
    # MAE=metrics.mean_absolute_error(y_test, y_pred)
    # MSE= metrics.mean_squared_error(y_test, y_pred)
    # RMSE=np.sqrt(metrics.mean_squared_error(y_test, y_pred))

    return y_predf
