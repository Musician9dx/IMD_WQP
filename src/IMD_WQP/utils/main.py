import os 
import sys
from IMD_WQP import logger
from IMD_WQP.pipeline.DataIngestion import data_ingestion
from IMD_WQP.pipeline.DataTransformation import data_transformer
from IMD_WQP.pipeline.ModelTrainer import model_trainer
import streamlit as st
import time

def model_retrain():


    mybar=st.progress(0,"Model Retraining Initiated Please wait while the magic happens")
    time.sleep(2)
    mybar.progress(5,"Cleaning up Directories ")
    time.sleep(2)

    try:

        try:
        
            os.remove(os.path.join("resource","data.csv"))
        except Exception as e:
            print(e)
        try:
        
            os.remove(os.path.join("resource","xtest.csv"))
        except Exception as e:
            print(e)
        try:
            os.remove(os.path.join("resource","xtrain.csv"))
        except Exception as e:
            print(e)
            os.remove(os.path.join("resource","ytrain.csv"))
        try:
            os.remove(os.path.join("resource","ytest.csv"))
        except Exception as e:
            print(e)
        
        
        mybar.progress(10,"Brewing Magic")
        time.sleep(2)


        try:
        
            os.remove(os.path.join("resource","model","model.h5"))
        except Exception as e:
            print(e)
        try:
            os.remove(os.path.join("resource","model","transformer.joblib"))
        except Exception as e:
            print(e)

        logger.info("Model Re-Training Has been Initialized")
        mybar.progress(15,"Directories have been reset successfully")

        time.sleep(2)

        mybar.progress(20,"Connecting to Mongodb")
        time.sleep(4)


        data_ingestion()
        mybar.progress(30,"Data Ingestion Successful")
        time.sleep(2)


        mybar.progress(35,"Building Data Transformer")
        time.sleep(4)



        data_transformer()

        mybar.progress(60,"Successfully built Transfromer")
        time.sleep(2)
        mybar.progress(65,"Preparing your Neural Netowrks")
        time.sleep(4)
        mybar.progress(70,"Training Initialized")
        time.sleep(2)

        model_trainer()

        mybar.progress(90,"Model Training Successfull")
        time.sleep(2)
        mybar.progress(95,"Building Pipeline")
        time.sleep(2)
        mybar.progress(100,"Ready to use")
        time.sleep(1)
        mybar.close()

    except Exception as e:
        print(e)
        logger.critical(str(e))


if __name__=="__main__":
    model_retrain()