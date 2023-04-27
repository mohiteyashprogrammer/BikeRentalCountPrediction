import os
import sys 
import pandas as pd
import numpy as  np 
from src.logger import logging
from src.exception import CustomException

from src.utils import load_object


class PredictPipline:
    def __init__(self):
        pass

    def Predict(self,features):
        try:
            ## This line Of code Work in Any system
            preproccesor_path = os.path.join("artifcats","preprocessor.pkl")
            model_path = os.path.join("artifcats","model.pkl")

            preprocessor = load_object(preproccesor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            logging.info("Error Occured In Prediction Pipline")
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
            season:str,
            holiday:int,
            weekday:str,
            workingday:int,
            weathersit:str,
            temp:float,
            year:int,
            months:str,
            hours:int,
            humidity:float):

        self.season = season
        self.holiday = holiday
        self.weekday = weekday
        self.workingday = workingday
        self.weathersit = weathersit
        self.temp = temp
        self.year = year
        self.months = months
        self.hours = hours
        self.humidity = humidity

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "season":[self.season],
                "holiday":[self.holiday],
                "weekday":[self.weekday],
                "workingday":[self.workingday],
                "weathersit":[self.weathersit],
                "temp":[self.temp],
                "year":[self.year],
                "months":[self.months],
                "hours":[self.hours],
                "humidity":[self.humidity]
            }

            data = pd.DataFrame(custom_data_input_dict)
            logging.info("DataFrame Gathered")
            return data

        except Exception as e:
            logging.info("Error Occured In Prediction Pipline")
            raise CustomException(e, sys)