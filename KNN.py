from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np




def KNeighborsBottom(data,pred):
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

    knn = KNeighborsRegressor(n_neighbors=6)
    knn.fit(X_train, y_train)
    y_predf = knn.predict(predf)

   #  accuracy3=knn.score(X_test,y_test) 
   #  MAE=metrics.mean_absolute_error(y_test, y_pred3)
   #  MSE= metrics.mean_squared_error(y_test, y_pred3)
   #  RMSE=np.sqrt(metrics.mean_squared_error(y_test, y_pred3))

    return y_predf


