class data:

    def __init__(self, sensor_name, value):
        self.__sensor_name = sensor_name
        self.__value = value

    def get_sensor(self):
        return self.__sensor_name

    def get_value(self):
        return self.__value

    def __str__(self):
        return self.__sensor_name + " -> \n\t" + self.__value
