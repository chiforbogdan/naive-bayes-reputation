from feature_header import *
from feature_type import *

class satisfaction_temperature:

    def __init__(self, target_val):
        self.__target_val = target_val 

    def __extract_temp(self, data):
        temp_header = feature_header().get_header(feature_type.TEMPERATURE)

        # Try to extract temperature value
        value = data.get_value().split('\n')

        for line in value:
            if line.startswith(temp_header):
                return float(line.replace(temp_header, ""))

        return 0

    def get_feature_type(self):
        return feature_type.TEMPERATURE

    def get_satisfaction(self, data):
        
        temp = self.__extract_temp(data)
        if temp == 0:
            return 0
        
        # Compute
        diff = abs(self.__target_val - temp)

        # Satisfaction mapping function        
        if diff == 0:
            return 1
        elif diff < 0.1:
            return 0.9
        elif diff < 0.2:
            return 0.8
        elif diff < 0.5:
            return 0.7
        elif diff < 0.8:
            return 0.6
        elif diff < 1:
            return 0.5
        elif diff < 1.5:
            return 0.4
        elif diff < 2:
            return 0.3
        elif diff < 2.5:
            return 0.2
        elif diff < 3:
            return 0.1

        # Default
        return 0
