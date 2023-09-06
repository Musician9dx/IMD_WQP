from tensorflow.keras.models import load_model
import joblib
import tensorflow as tf
import os
import pandas as pd

def predict(data):
    ml=load_model(os.path.join("resource","model","model.h5"))

    transformer=joblib.load(os.path.join("resource","model","transformer.joblib"))

    numerical_features=['fixed acidity', 'volatile acidity', 'citric acid',
            'residual sugar', 'chlorides', 'free sulfur dioxide',
                        'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',]
    
    DataFrame=pd.read_json(data)
    


    tran=transformer.transform(DataFrame)

    return(ml.predict(tran))

predictor=predict

