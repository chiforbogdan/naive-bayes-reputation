from feature_type import *

class feature_header:
    def __init__(self):
        self.__headers = {feature_type.TEMPERATURE: "temperature: ",
                          feature_type.HUMIDITY: "humidity: ",
                          feature_type.CO2: "CO2: "}

    def get_header(self, feature):
        return self.__headers[feature]
