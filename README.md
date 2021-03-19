# Disease-predictor
This is a web based application used to predict diseases based on symptoms. The amount of diseases that can be predicted are limited and the AI is still ruddy. For accurate results please list as many symptoms as possible.

The dataset used is [Kaggle Disease Symptom Prediction Dataset.](https://www.kaggle.com/itachi9604/disease-symptom-description-dataset)  
The app is deployed on heroku [Disease Predictor](https://disease-predictor2.herokuapp.com)

Here's a description of how the application looks like
![app description pic](https://raw.githubusercontent.com/lightknight64bit/Disease-predictor/master/images/app.png)

Here's some demo pictures of the application
![app demo 1](https://raw.githubusercontent.com/lightknight64bit/Disease-predictor/master/images/app_with_values.png)
![app demo 2](https://raw.githubusercontent.com/lightknight64bit/Disease-predictor/master/images/predicted.png)

The model used is a random forest classifier which achieved 99.8% accuracy on the validation dataset and 99.7% cross validation accuracy with k=5

## **Please Fill all possible symptoms for accurate results. The AI might even predict completely wrong results if all possible symptoms values are not filled.**
