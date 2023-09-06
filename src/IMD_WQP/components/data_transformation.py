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
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import joblib

@dataclass
class DataTransformationConfig():
    
    DataSourcePath="resource/data.csv"
    XTrainDataPath="resource/xtrain.csv"
    XTestDataPath="resource/xtest.csv"
    YTrainDataPath="resource/ytrain.csv"
    YTestDataPath="resource/ytest.csv"

class DataTransformation():

    def __init__(self):

        self.config=DataTransformationConfig()

        self.numerical_features=['fixed acidity', 'volatile acidity', 'citric acid',
        'residual sugar', 'chlorides', 'free sulfur dioxide',
                    'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',]
        
        self.categorical_features=["type","quality"]

        self.columns=['type', 'fixed acidity', 'volatile acidity', 'citric acid',
        'residual sugar', 'chlorides', 'free sulfur dioxide',
                    'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',
                    'quality']
    
    def get_data(self):

        df=pd.read_csv(self.config.DataSourcePath)


        df.drop(["_id"],inplace=True,axis=1)

        return df
    
    def Build_Transformer(self,DataFrame):

        self.df=DataFrame

        numerical_pipeline=Pipeline([

            ("Imputer",SimpleImputer(strategy="median")),
            ("Standard Scaler",StandardScaler())

        ])


        categorical_pipeline=Pipeline([

            ("Imputer",SimpleImputer(strategy="most_frequent")),
            ("OneHotEncoder",OneHotEncoder(sparse=False))

        ])




        Tranformer=ColumnTransformer([

            ("Numerical Pipeline",numerical_pipeline,self.numerical_features),

        ])

        return Tranformer
    
    def apply_transformation(self,data,transformer):
        
        self.transformer=transformer
        self.data=data

        transformed_data=transformer.fit_transform(data)

        joblib.dump(transformer,"resource/model/transformer.joblib")


        x=pd.DataFrame(transformed_data)
        y_quality=pd.DataFrame(data['quality'])
        y_type=pd.DataFrame(data['type'].replace({

            'red':0,
            'white':1
        }))


        y=pd.concat(objs=[y_type,y_quality],axis=1,ignore_index=True)

        data=pd.concat(objs=[x,y],ignore_index=True,axis=1)

        data=data.sample(frac=1).reset_index(drop=True)

        return (
            data
        )
    
    def split_and_save(self,data):
        
        train,test=train_test_split(data)

        x_train=pd.DataFrame(train[list(range(11))])

        y_train=pd.DataFrame(train[[11,12]])


        x_test=pd.DataFrame(test[list(range(11))])


        y_test=pd.DataFrame(test[[11,12]])

        x_train.to_csv(self.config.XTrainDataPath,index=False,header=True)
        y_train.to_csv(self.config.YTrainDataPath,index=False,header=True)
        x_test.to_csv(self.config.XTestDataPath,index=False,header=True)
        y_test.to_csv(self.config.YTestDataPath,index=False,header=True)


def initialize_data_transformation():

    logger.info("Data Transformation Initiated")

    progress_bar=tqdm.tqdm(total=100)

    word=pyfiglet.figlet_format("DATA TPREPROCESSING SUCCESSFUL")

    try:
        
        progress_bar.update(0)
        logger.info("Data Transformation Initiated")

        obj=DataTransformation()
        logger.info("Getting Data")

        DataFrame=obj.get_data()
        logger.info("Data Successfull")

        progress_bar.update(25)

        logger.info("Building Transformer")
        transformer=obj.Build_Transformer(DataFrame)
        logger.info("Transformer Ready")

        logger.info("Applying TRansformation")
        data=obj.apply_transformation(data=DataFrame,transformer=transformer)
        logger.info("Transformation applied successfully")

        progress_bar.update(60)

        logger.info("Creating Train and Test Data Sets for X and Y")
        obj.split_and_save(data)
        logger.info("Train and Test Data Sets are ready")
        logger.info("Data Preprocessing/Transformation Successfull")


        progress_bar.update(100)

        progress_bar.close()

        print('\n','\n')

        print(word)
        print('\n','\n')



    
    except Exception as e:

        logger.critical("Error In Data Transformation and stated that "+ str(e))
        print('Error')
        print(e)

        








