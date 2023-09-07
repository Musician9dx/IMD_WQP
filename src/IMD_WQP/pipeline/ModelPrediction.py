
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import pandas as pd
import tensorflow

def predict(data):
    ml=load_model(os.path.join("resource","model","model.h5"))

    transformer=joblib.load("D:/INeuron/IMD_WQP/resource/model/transformer.joblib")
    
#       os.path.join("resource","model","model.h5")
#        '''os.path.join("resource","model","transformer.joblib")'''

    tran=transformer.transform(data)

    print("Successful")

    pred=ml.predict(tran)

    z=int(pred[[0][0]][0])

    if z>=0.5:
        z="White"
    else:
        z="Red"

    l=int(pred[[1][0]][0])

    return (

        z,l
    )

predictor=predict

