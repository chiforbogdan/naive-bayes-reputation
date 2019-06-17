from enum import Enum

class feature_type(Enum):
    '''
        This class indicates the Bayes Network (BN) feature type.
        For instance, an IoT node can publish a temperature value along with its' location.
    '''
    TEMPERATURE = 0
    HUMIDITY = 1
    CO2 = 2
