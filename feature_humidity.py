from random import *
from feature_type import *
from feature_header import *

class feature_humidity:
    '''
        This class simulates a humidity sensor
    '''

    def __init__(self, target_val, error_val):
        self.__feature_type = feature_type        
        # Indicates the himidity level (percent)        
        self.__target_val = target_val
        self.__error_val = error_val

    def set_target_error(self, target_val, error_val):
        self.__target_val = target_val
        self.__error_val = error_val

    def get_feature_val(self):
        
        # Generate a random value and compute a value within the error_val range
        rand = random()
        if rand > 0.5:
            sign = 1
        else:
            sign = -1

        humidity_level = self.__target_val + sign * random() * self.__error_val

        return feature_header().get_header(feature_type.HUMIDITY) + str(humidity_level)
