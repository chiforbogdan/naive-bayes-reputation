from feature_header import *
from feature_type import *

class satisfaction_humidity:

    def __init__(self, target_val):
        self.__target_val = target_val 

    def __extract_humidity(self, data):
        humidity_header = feature_header().get_header(feature_type.HUMIDITY)

        # Try to extract humidity level value
        value = data.get_value().split('\n')

        for line in value:
            if line.startswith(humidity_header):
                return float(line.replace(humidity_header, ""))

        return 0

    def get_feature_type(self):
        return feature_type.HUMIDITY

    def get_satisfaction(self, data):
        
        humidity = self.__extract_humidity(data)
        if humidity == 0:
            return 0
        
        # Compute
        diff = abs(self.__target_val - humidity)

        # Satisfaction mapping function        
        if diff == 0:
            return 1
        elif diff < 2:
            return 0.9
        elif diff < 5:
            return 0.8
        elif diff < 7:
            return 0.7
        elif diff < 9:
            return 0.6
        elif diff < 10:
            return 0.5
        elif diff < 12:
            return 0.4
        elif diff < 15:
            return 0.3
        elif diff < 17:
            return 0.2
        elif diff < 20:
            return 0.1

        # Default
        return 0
