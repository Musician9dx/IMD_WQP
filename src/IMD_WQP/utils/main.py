import os 
import sys
from IMD_WQP import logger
from IMD_WQP.pipeline.DataIngestion import data_ingestion
from IMD_WQP.pipeline.DataTransformation import data_transformer
from IMD_WQP.pipeline.ModelTrainer import model_trainer

def model_retrain():
    try:
        try:
        
            os.remove(os.path.join("resource","data.csv"))
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
            os.remove(os.path.join("resource","model","model.h5"))
        try:
            os.remove(os.path.join("resource","model","transformer.joblib"))
        except Exception as e:
            print(e)




        logger.info("Model Re-Training Has been Initialized")

        data_ingestion()

        data_transformer()

        model_trainer()

    except Exception as e:
        print(e)
        logger.critical(str(e))


if __name__=="__main__":
    model_retrain()