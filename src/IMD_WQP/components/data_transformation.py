import os 
import sys
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import sklearn as sk
from IMD_WQP import logger
import tqdm
import pyfiglet
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


class DataTransformationConfig():
    
    DataSourcePath="resource/data.csv"
    TrainDataPath="resource/train.csv"
    TestDataPath="resource/test.csv"

class DataTransformation():

    def __init__(self):
        self.config=DataTransformationConfig()
    
    def get_data(self):

        df=pd.read_csv(self.config.DataSourcePath)


        df.drop(["_id"],inplace=True,axis=1)

        return df
    
    def Build_Transformer(self,DataFrame):

        self.df=DataFrame

        numerical_features=[]
        categorical_features=[]

        numerical_pipeline=Pipeline([

            ("Imputer",SimpleImputer),
            ("Standard Scaler",StandardScaler)

        ])


        categorical_pipeline=Pipeline([

            ("Imputer",SimpleImputer),
            ("OneHotEncoder",OneHotEncoder)

        ])




        Tranformer=ColumnTransformer([

            ("Numerical Pipeline",numerical_pipeline,numerical_features),
            ("Categorical Pipeline",categorical_pipeline,categorical_features)

        ])

        return Tranformer

        

if __name__=="__main__":
    
    obj=DataTransformation()

    DataFrame=obj.get_data()

    transformer=obj.Build_Transformer(DataFrame)

    print(type(transformer))