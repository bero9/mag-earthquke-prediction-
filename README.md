# mag-earthquke-prediction-
Earthquake Prediction is a way of predicting the magnitude of an earthquake based on parameters such as longitude, latitude, , and depth using machine learning to give   warnings of potentially damaging earthquakes early enough to allow appropriate response to the disaster, enabling people to minimize loss of life and property.
Earthquake-prediction-using-Machine-    learning-models : 
Abstract
Earthquake Prediction is a way of predicting the magnitude of an earthquake based on parameters such as longitude, latitude, , and depth using machine learning to give   warnings of potentially damaging earthquakes early enough to allow appropriate response to the disaster, enabling people to minimize loss of life and property.
Dataset
The dataset used in this project is called the "SOCR Earthquake Dataset", and it contains information about all the earthquakes recorded worldwide from 1990 to 2023.
•	time in millisecconds
•	place 
•	status 
•	tsunami (boolean value)
•	significance
•	data_type
•	magnitudo 
•	state 
•	longitude 
•	latitude 
•	depth 
•	date
The dataset comprises approximately three million rows, with each row representing a specific earthquake event. Each entry in the dataset contains a set of relevant attributes related to the earthquake, such as the date and time of the event, the geographical location (latitude and longitude), the magnitude of the earthquake, the depth of the epicenter, the type of magnitude used for measurement, the affected region, and other pertinent information.
Introduction	

The SOCR Earthquake Dataset can be used to build machine learning models to predict earthquakes or to better understand earthquake patterns and characteristics. Here are a few possible ways machine learning models can be used with this dataset:

1.	Magnitude prediction: You can use this dataset to build a model that predicts the magnitude of an earthquake based on other factors such as location, depth, or the number of seismic stations that recorded the earthquake. You could use regression techniques to build this model.
2.	Data visualization: You can use this dataset to create visualizations of earthquake data, which could help you identify patterns and relationships in the data. You could use techniques such as scatter plots, heat maps, or geographic information systems (GIS) to visualize the data.
3.	Anomaly detection: You can use this dataset to detect anomalies or outliers in the data, which could represent earthquakes that are unusual or unexpected. You could use techniques such as clustering or classification to identify patterns in the data and detect anomalies

These are just a few examples of the many ways that machine learning models can be used with the SOCR Earthquake Dataset. The specific approach you take will depend on your research question and the goals of your analysis. In this project we focus mainly on Magnitude prediction.
Data visualization

 
            Magnitude of Earthquakes per Year(1990-2023)
 
                                            Earthquake magnitude and depth over the years

Implementation:

We will use four models in this project: 
•	Linear Regression
•	Decision Tree
•	K-Nearest Neighbors
1.Linear Regression

Linear regression is a type of supervised machine learning algorithm that is used to model the linear relationship between a dependent variable (in this case, earthquake magnitude) and one or more independent variables (in this case, latitude, longitude, depth,).
The basic idea behind linear regression is to find the line of best fit through the data that minimizes the sum of the squared residuals (the difference between the predicted and actual values of the dependent variable). The coefficients of the line of best fit are estimated using a method called ordinary least squares, which involves minimizing the sum of the squared residuals with respect to the coefficients.
In this situation, we have used multiple linear regression to model the relationship between earthquake magnitude and latitude, longitude, depth, . The multiple linear regression model assumes that there is a linear relationship between the dependent variable (magnitude) and each of the independent variables (latitude, longitude, depth,), and that the relationship is additive (i.e., the effect of each independent variable on the dependent variable is independent of the other independent variables).
Once the model has been fit to the data, we can use it to predict the magnitude of a new earthquake given its latitude, longitude, depth,.
The linear regression equation used in our multiple linear regression model for earthquake magnitude prediction with latitude, longitude, depth, and number of seismic stations as independent variables can be written as:
Magnitude = -0.6028 * Latitude + 1.2012 * Longitude - 0.0008 * Depth + 0.1573
Where:
•	Magnitude is the dependent variable, representing the magnitude of the earthquake
•	Latitude, Longitude, Depth, and 
•	The intercept (0.1573) represents the predicted magnitude when all independent variables are zero.
•	This equation allows us to predict the magnitude of an earthquake based on its latitude, longitude, depth, By plugging in the values of the independent variables for a given earthquake, we can obtain an estimate of its magnitude.
The results we obtained from the linear regression model were as follows:
•	Mean squared error (MSE): 0.899104931417553
•	R-squared (R2) score: 0.948211438138959

 
	 
2.Decision Tree
A Decision tree is a tree-like structure that represents a set of decisions and their possible consequences. Each node in the tree represents a decision, and each branch represents an outcome of that decision. The leaves of the tree represent the final decisions or predictions.
The results we obtained from the linear regression model were as follows:
•	Mean squared error (MSE 0.6583186294580764
•	R-squared (R2) score 0.8113683685343399
 

       

3.K-Nearest Neighbors

The K-NN algorithm works by finding the K nearest neighbors to a given data point based on a distance metric, such as Euclidean distance. The class or value of the data point is then determined by the majority vote or average of the K neighbors. This approach allows the algorithm to adapt to different patterns and make predictions based on the local structure of the data.
The results we obtained from the linear regression model were as follows:
•	Mean squared error (MSE 0.39129073019317534
•	R-squared (R2) score 0.6255323574309928

  

 

Comparison Graphs
 
This image shows the difference between the three algorithms depending on Accuracy
Conclusion	
When comparing two models, both the mean squared error (MSE) and R-squared (R2) score can be used to evaluate the performance of the models.

In general, a model with a lower MSE and a higher R2 score is considered a better model. This is because the MSE measures the average difference between the predicted and actual values, and a lower MSE indicates that the model is making more accurate predictions. The R2 score measures the proportion of the variance in the target variable that is explained by the model, and a higher R2 score indicates that the model is able to explain more of the variability in the target variable.

From the results of this project we can conclude that Linear Regression is the most accurate model for predicting the magnitude of Earthquake compared to all other models used in this project.
However, it's important to keep in mind that the relative importance of MSE and R2 score may vary depending on the specific problem and the context in which the models are being used. For example, in some cases, minimizing the MSE may be more important than maximizing the R2 score, or vice versa. It's also possible that one model may perform better on one metric and worse on another, so it's important to consider both metrics together when evaluating the performance of the models.
