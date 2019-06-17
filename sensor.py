from data import *

class sensor:

    def __init__(self, name):
        self.__name = name
        self.__features = []

    def add_feature(self, feature):
        self.__features.append(feature)

    def get_data(self):
        value = ""

        for feature in self.__features:
            value = value + feature.get_feature_val() + "\n"

        return data(self.__name, value)

    def get_name(self):
        return self.__name
