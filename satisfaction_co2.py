from feature_header import *
from feature_type import *

class satisfaction_co2:

    def __init__(self, target_val):
        self.__target_val = target_val 

    def __extract_co2(self, data):
        co2_header = feature_header().get_header(feature_type.CO2)

        # Try to extract CO2 level value
        value = data.get_value().split('\n')

        for line in value:
            if line.startswith(co2_header):
                return float(line.replace(humidity_header, ""))

        return 0

    def get_feature_type(self):
        return feature_type.CO2

    def get_satisfaction(self, data):
        
        co2 = self.__extract_co2(data)
        if co2 == 0:
            return 0
        
        # Compute
        diff = abs(self.__target_val - co2)

        # Satisfaction mapping function        
        if diff == 0:
            return 1
        elif diff < 20:
            return 0.9
        elif diff < 40:
            return 0.8
        elif diff < 60:
            return 0.7
        elif diff < 80:
            return 0.6
        elif diff < 100:
            return 0.5
        elif diff < 120:
            return 0.4
        elif diff < 140:
            return 0.3
        elif diff < 160:
            return 0.2
        elif diff < 180:
            return 0.1

        # Default
        return 0
