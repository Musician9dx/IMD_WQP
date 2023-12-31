from IMD_WQP import logger
import os
import ensure
from dataclasses import dataclass
import sys
import sklearn
import pymongo
import pandas as pd
import tqdm
import pyfiglet
import time

@dataclass
class DataIngestionConfig:
    DataSourceUrl="mongodb+srv://pymongo:pymongo@cluster0.yksijnk.mongodb.net/"
    DataDestination="D:\INeuron\IMD_WQP\resource\data.csv"



class DataIngestion:

    def __init__(self) -> None:
        self.config=DataIngestionConfig()
        
    def fetch_from_pymongo(self):

        try:


            logger.info("Connecting to Mongo Client")

            client=pymongo.MongoClient(self.config.DataSourceUrl)

            logger.info("Successfully Connectod to Mongo Client")

            database=client['wine']

            collection=database['wine']

            logger.info("Fetching Data")

            cursor=collection.find({})

            logger.info("Converting Fetched Data Into Local Variables")

            data=[]

            for document in cursor:
                
                data.append(document)

            logger.info("Data Comversion Successfull")

            
            return data
        
        except Exception as e:
            
            print(e)

            logger.critical("MongoDB Connection Unsuccessful and stated" + str(e))

        
    def read_into_DataFrame(self,data):

        logger.info("Converting Data Into DataFrame")

        try:
        
            self.data=data

            DataFrame=pd.DataFrame.from_dict(self.data)

            logger.info("DataFrame has been built successfully")

            return DataFrame


        except Exception as e:

            print(e)

            logger.error("Failed to create a data frame and stated that" + str(e))

    def save_csv(self,DataFrame):

        logger.info("saving csv")

        try:

            self.DataFrame=DataFrame

            self.DataFrame.to_csv(os.path.join(os.getcwd()+"/resource/data.csv"),index=False,header=True)

            logger.info("Successfully saved CSV")

        except Exception as e:
            
            print(e)

            logger.error("Failed to save CSV and stated that"+ str(e))



def initialize_data_ingestion():


    try:

        progress_bar=tqdm.tqdm(total=4)

        logger.info("Data Ingestion Has Been Initialized")

        obj=DataIngestion()
        progress_bar.update(1)

        data=obj.fetch_from_pymongo()
        progress_bar.update(1)

        data=list(data)
        
        DataFrame=obj.read_into_DataFrame(data)
        progress_bar.update(1)
        
        obj.save_csv(DataFrame)

        logger.info("Successfully Initiated and Finished the Data Ingestion Process")

        progress_bar.update(1)
        progress_bar.close()

        word=pyfiglet.figlet_format("Data Ingestion Successful")
        print('\n','\n')

        print(word)

        print('\n','\n')

    except Exception as e:
        print(e)













