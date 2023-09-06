import os
import tensorflow as tf
import sys
import sklearn
import pandas as pd
import numpy as np
from IMD_WQP import logger
from dataclasses import dataclass
import pyfiglet

@dataclass
class ModelTrainerConfig():
    XTrainPath="resource/xtrain.csv"
    YTrainPath="resource/ytrain.csv"
    XTestPath="resource/xtest.csv"
    YTestPath="resource/ytest.csv"

@dataclass
class ModelTrainerParams():
    pass


class ModelTrainer():
    
    def __init__(self) -> None:
        self.config=ModelTrainerConfig()
        self.params=ModelTrainerParams()
    
    def load_data(self):
       
        self.xtrain=pd.read_csv(self.config.XTrainPath)
        self.ytrain=pd.read_csv(self.config.YTrainPath)
        self.xtest=pd.read_csv(self.config.XTestPath)
        self.ytest=pd.read_csv(self.config.YTestPath)
        self.ytrain={
             
             "Classification":self.ytrain[["11"]],
             "Regression":self.ytrain[["12"]]
        }
        self.ytestevaluate=self.ytest

        self.ytest={
             
             "Classification":self.ytest[["11"]],
             "Regression":self.ytest[["12"]]
        }


    
    def create_model(self):
        

        Input_Layer=tf.keras.layers.Input(shape=(11,),name="Input_Layer")

        Dense0_0=tf.keras.layers.Dense(units=128,activation='relu',name="Bus_Processing_1")(Input_Layer)
        Dense0_1=tf.keras.layers.Dense(units=128,activation='relu',name="Bus_Processing_2")(Dense0_0)

        Dense1_1=tf.keras.layers.Dense(units=128,activation='relu',name="Classification_trainer_1")(Dense0_1)
        Dense2_1=tf.keras.layers.Dense(units=256,activation='relu',name="Classification_trainer_2")(Dense1_1)
        Dense3_1=tf.keras.layers.Dense(units=64,activation='relu',name="Classification_trainer_3")(Dense2_1)

        Dense1_2=tf.keras.layers.Dense(units=128,activation='relu',name="Regression_trainer_1")(Dense0_1)
        Dense2_2=tf.keras.layers.Dense(units=256,activation='relu',name="Regression_trainer_2")(Dense1_2)
        Dense3_2=tf.keras.layers.Dense(units=64,activation='relu',name="Regression_trainer_3")(Dense2_2)

        Output1=tf.keras.layers.Dense(units=1,activation='sigmoid',name="Classification")(Dense3_1)
        Output2=tf.keras.layers.Dense(units=1,activation='relu',name="Regression")(Dense3_2)

        ml=tf.keras.Model(inputs=Input_Layer,outputs=[Output1,Output2])

        self.ml=ml
    
    def train_and_save_model(self):

        ml=self.ml

        ml.compile(

                   optimizer='adam',
                   loss={
                       "Classification":"binary_crossentropy",
                       "Regression":"mean_squared_error"
                       }, 
                   metrics = {
                       'Classification' : 'accuracy',
                         'Regression': tf.keras.metrics.RootMeanSquaredError()
                       }
                    
        )

        ml.fit(x=self.xtrain,y=self.ytrain,epochs=100,shuffle=True,validation_split=0.2)

        logger.info("Saving Model")

        ml.save(os.path.join("resource","model","model.h5"))

def initialize_model_trainer():

    try:

        word=pyfiglet.figlet_format("Model Training Initialized")
        print(word)
        

        logger.info("Model Training Initiated")
        obj=ModelTrainer()

        logger.info("Loading Data")
        obj.load_data()
        logger.info("Loading Data Successful")

        logger.info("Creating Model")
        obj.create_model()
        logger.info("Model Creation Successful")

        logger.info("Training Model")
        obj.train_and_save_model()
        logger.info("Model Training and Saving Successful")
        
        word=pyfiglet.figlet_format("Model Training Successful")
        print(word)

    except Exception as e:
        print("Task Couldn't be achieved")
        logger.critical("Model Training Failed stated that "+ str(e))