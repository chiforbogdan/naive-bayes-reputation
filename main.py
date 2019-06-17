from feature_temperature import *
from feature_humidity import *
from feature_co2 import *
from sensor import *
from satisfaction_temperature import *
from satisfaction_humidity import *
from satisfaction_co2 import *
from naive_bayes import *
import matplotlib.pyplot as plt

def scenario1():
    SIMULATION_LOOP = 10000

    SATISFACTION_THRESHOLD = 0.8

    # Temperature value
    TARGET_TEMP_VAL = 20
    ERR_TEMP_VAL = 1

    # Declare sensors
    sensors = []
    sensor1 = sensor("sensor1")
    sensors.append(sensor1)
    sensor2 = sensor("sensor2")
    sensors.append(sensor2)
    sensor3 = sensor("sensor3")
    sensors.append(sensor3)

    # Declare temperature feature
    temp_sensor1 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL)
    temp_sensor2 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 2)
    temp_sensor3 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 4)

    sensor1.add_feature(temp_sensor1)
    sensor2.add_feature(temp_sensor2)
    sensor3.add_feature(temp_sensor3)

    # Configure satisfaction evaluator
    temp_satisfaction_eval = satisfaction_temperature(TARGET_TEMP_VAL)

    # Configure feature weights
    feature_weights = {feature_type.TEMPERATURE: 1}

    # Create naive bayes reputation model
    nb = {}
    for sensor_item in sensors:
        nb[sensor_item.get_name()] = naive_bayes(sensor1.get_name(), feature_weights, SATISFACTION_THRESHOLD)

        # Add satisfaction evaluator to NB model
        nb[sensor_item.get_name()].add_satisfaction(temp_satisfaction_eval)

    for i in range(0, SIMULATION_LOOP):    
        for sensor_item in sensors:        
            # Generate sensor data        
            data = sensor_item.get_data()
            nb[sensor_item.get_name()].compute(data)
            nb[sensor_item.get_name()].save_reputation()

    # Plot the reputation probability
    legend = []
    for sensor_item in sensors:
        legend.append(sensor_item.get_name())
        plt.plot(nb[sensor_item.get_name()].get_reputation_history())

    plt.xlabel("Steps")
    plt.ylabel("Trust reputation probability")
    plt.legend(legend)
    plt.show()

def scenario2():
    SIMULATION_LOOP = 10000

    SATISFACTION_THRESHOLD = 0.8

    # Temperature value
    TARGET_TEMP_VAL = 20
    ERR_TEMP_VAL = 1

    # Humidity level value
    TARGET_HUMIDITY_VAL = 60
    ERR_HUMIDITY_VAL = 10

    # Declare sensors
    sensors = []
    sensor1 = sensor("sensor1")
    sensors.append(sensor1)
    sensor2 = sensor("sensor2")
    sensors.append(sensor2)
    sensor3 = sensor("sensor3")
    sensors.append(sensor3)

    # Declare temperature feature
    temp_sensor1 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL)
    temp_sensor2 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 2)
    temp_sensor3 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 4)
    
    sensor1.add_feature(temp_sensor1)
    sensor2.add_feature(temp_sensor2)
    sensor3.add_feature(temp_sensor3)

    # Declare humidity feature
    humidity_sensor1 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL)
    humidity_sensor2 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL * 2)
    humidity_sensor3 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL * 4)

    sensor1.add_feature(humidity_sensor1)
    sensor2.add_feature(humidity_sensor2)
    sensor3.add_feature(humidity_sensor3)

    # Configure satisfaction evaluator
    temp_satisfaction_eval = satisfaction_temperature(TARGET_TEMP_VAL)
    humidity_satisfaction_eval = satisfaction_humidity(TARGET_HUMIDITY_VAL)

    # Configure feature weights
    feature_weights = {feature_type.TEMPERATURE: 0.5,
                       feature_type.HUMIDITY: 0.5}

    # Create naive bayes reputation model
    nb = {}
    for sensor_item in sensors:
        nb[sensor_item.get_name()] = naive_bayes(sensor1.get_name(), feature_weights, SATISFACTION_THRESHOLD)

        # Add satisfaction evaluator to NB model
        nb[sensor_item.get_name()].add_satisfaction(temp_satisfaction_eval)
        nb[sensor_item.get_name()].add_satisfaction(humidity_satisfaction_eval)

    for i in range(0, SIMULATION_LOOP):    
        for sensor_item in sensors:        
            # Generate sensor data        
            data = sensor_item.get_data()
            nb[sensor_item.get_name()].compute(data)
            nb[sensor_item.get_name()].save_reputation()

    # Plot the reputation probability
    legend = []
    for sensor_item in sensors:
        legend.append(sensor_item.get_name())
        plt.plot(nb[sensor_item.get_name()].get_reputation_history())

    plt.xlabel("Steps")
    plt.ylabel("Trust reputation probability")
    plt.legend(legend)
    plt.show()

def scenario3():
    SIMULATION_LOOP = 10000

    SATISFACTION_THRESHOLD = 0.8

    # Temperature value
    TARGET_TEMP_VAL = 20
    ERR_TEMP_VAL = 1

    # Humidity level value
    TARGET_HUMIDITY_VAL = 60
    ERR_HUMIDITY_VAL = 10

    # Declare sensors
    sensors = []
    sensor1 = sensor("sensor1")
    sensors.append(sensor1)
    sensor2 = sensor("sensor2")
    sensors.append(sensor2)
    sensor3 = sensor("sensor3")
    sensors.append(sensor3)

    # Declare temperature feature
    temp_sensor1 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL)
    temp_sensor2 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 2)
    temp_sensor3 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 4)
    
    sensor1.add_feature(temp_sensor1)
    sensor2.add_feature(temp_sensor2)
    sensor3.add_feature(temp_sensor3)

    # Declare humidity feature
    humidity_sensor1 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL * 2)
    humidity_sensor2 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL)
    humidity_sensor3 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL * 4)

    sensor1.add_feature(humidity_sensor1)
    sensor2.add_feature(humidity_sensor2)
    sensor3.add_feature(humidity_sensor3)

    # Configure satisfaction evaluator
    temp_satisfaction_eval = satisfaction_temperature(TARGET_TEMP_VAL)
    humidity_satisfaction_eval = satisfaction_humidity(TARGET_HUMIDITY_VAL)

    # Configure feature weights
    feature_weights = {feature_type.TEMPERATURE: 0.9,
                       feature_type.HUMIDITY: 0.1}

    # Create naive bayes reputation model
    nb = {}
    for sensor_item in sensors:
        nb[sensor_item.get_name()] = naive_bayes(sensor1.get_name(), feature_weights, SATISFACTION_THRESHOLD)

        # Add satisfaction evaluator to NB model
        nb[sensor_item.get_name()].add_satisfaction(temp_satisfaction_eval)
        nb[sensor_item.get_name()].add_satisfaction(humidity_satisfaction_eval)

    for i in range(0, SIMULATION_LOOP):    
        for sensor_item in sensors:        
            # Generate sensor data        
            data = sensor_item.get_data()
            nb[sensor_item.get_name()].compute(data)
            nb[sensor_item.get_name()].save_reputation()

    # Plot the reputation probability
    legend = []
    for sensor_item in sensors:
        legend.append(sensor_item.get_name())
        plt.plot(nb[sensor_item.get_name()].get_reputation_history())

    plt.xlabel("Steps")
    plt.ylabel("Trust reputation probability")
    plt.legend(legend)
    plt.show()

def scenario4():
    SIMULATION_LOOP = 10000

    SATISFACTION_THRESHOLD = 0.8

    # Temperature value
    TARGET_TEMP_VAL = 20
    ERR_TEMP_VAL = 1

    # Humidity level value
    TARGET_HUMIDITY_VAL = 60
    ERR_HUMIDITY_VAL = 10

    # Declare sensors
    sensors = []
    sensor1 = sensor("sensor1")
    sensors.append(sensor1)
    sensor2 = sensor("sensor2")
    sensors.append(sensor2)
    sensor3 = sensor("sensor3")
    sensors.append(sensor3)

    # Declare temperature feature
    temp_sensor1 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL)
    temp_sensor2 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 2)
    temp_sensor3 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 4)
    
    sensor1.add_feature(temp_sensor1)
    sensor2.add_feature(temp_sensor2)
    sensor3.add_feature(temp_sensor3)

    # Declare humidity feature
    humidity_sensor1 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL * 4)
    humidity_sensor2 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL)
    humidity_sensor3 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL * 8)

    sensor1.add_feature(humidity_sensor1)
    sensor2.add_feature(humidity_sensor2)
    sensor3.add_feature(humidity_sensor3)

    # Configure satisfaction evaluator
    temp_satisfaction_eval = satisfaction_temperature(TARGET_TEMP_VAL)
    humidity_satisfaction_eval = satisfaction_humidity(TARGET_HUMIDITY_VAL)

    # Configure feature weights
    feature_weights = {feature_type.TEMPERATURE: 0.1,
                       feature_type.HUMIDITY: 0.9}

    # Create naive bayes reputation model
    nb = {}
    for sensor_item in sensors:
        nb[sensor_item.get_name()] = naive_bayes(sensor1.get_name(), feature_weights, SATISFACTION_THRESHOLD)

        # Add satisfaction evaluator to NB model
        nb[sensor_item.get_name()].add_satisfaction(temp_satisfaction_eval)
        nb[sensor_item.get_name()].add_satisfaction(humidity_satisfaction_eval)

    for i in range(0, SIMULATION_LOOP):    
        for sensor_item in sensors:        
            # Generate sensor data        
            data = sensor_item.get_data()
            nb[sensor_item.get_name()].compute(data)
            nb[sensor_item.get_name()].save_reputation()

    # Plot the reputation probability
    legend = []
    for sensor_item in sensors:
        legend.append(sensor_item.get_name())
        plt.plot(nb[sensor_item.get_name()].get_reputation_history())

    plt.xlabel("Steps")
    plt.ylabel("Trust reputation probability")
    plt.legend(legend)
    plt.show()

def scenario5():
    SIMULATION_LOOP = 10000

    SATISFACTION_THRESHOLD = 0.8

    # Temperature value
    TARGET_TEMP_VAL = 20
    ERR_TEMP_VAL = 1

    # Humidity level value
    TARGET_HUMIDITY_VAL = 60
    ERR_HUMIDITY_VAL = 10

    # CO2 level value
    TARGET_CO2_VAL = 1000
    ERR_CO2_VAL = 40

    # Declare sensors
    sensors = []
    sensor1 = sensor("sensor1")
    sensors.append(sensor1)
    sensor2 = sensor("sensor2")
    sensors.append(sensor2)
    sensor3 = sensor("sensor3")
    sensors.append(sensor3)

    # Declare temperature feature
    temp_sensor1 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL)
    temp_sensor2 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 2)
    temp_sensor3 = feature_temperature(TARGET_TEMP_VAL, ERR_TEMP_VAL * 4)
    
    sensor1.add_feature(temp_sensor1)
    sensor2.add_feature(temp_sensor2)
    sensor3.add_feature(temp_sensor3)

    # Declare humidity feature
    humidity_sensor1 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL)
    humidity_sensor2 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL * 4)
    humidity_sensor3 = feature_humidity(TARGET_HUMIDITY_VAL, ERR_HUMIDITY_VAL * 8)

    sensor1.add_feature(humidity_sensor1)
    sensor2.add_feature(humidity_sensor2)
    sensor3.add_feature(humidity_sensor3)

    # Declare CO2 feature
    co2_sensor1 = feature_co2(TARGET_CO2_VAL, ERR_CO2_VAL)
    co2_sensor2 = feature_co2(TARGET_CO2_VAL, ERR_CO2_VAL * 2)
    co2_sensor3 = feature_co2(TARGET_CO2_VAL, ERR_CO2_VAL * 4)

    sensor1.add_feature(co2_sensor1)
    sensor2.add_feature(co2_sensor2)
    sensor3.add_feature(co2_sensor3)

    # Configure satisfaction evaluator
    temp_satisfaction_eval = satisfaction_temperature(TARGET_TEMP_VAL)
    humidity_satisfaction_eval = satisfaction_humidity(TARGET_HUMIDITY_VAL)
    co2_satisfaction_eval = satisfaction_co2(TARGET_CO2_VAL)

    # Configure feature weights
    feature_weights = {feature_type.TEMPERATURE: 0.33,
                       feature_type.HUMIDITY: 0.33,
                       feature_type.CO2: 0.33}

    # Create naive bayes reputation model
    nb = {}
    for sensor_item in sensors:
        nb[sensor_item.get_name()] = naive_bayes(sensor1.get_name(), feature_weights, SATISFACTION_THRESHOLD)

        # Add satisfaction evaluator to NB model
        nb[sensor_item.get_name()].add_satisfaction(temp_satisfaction_eval)
        nb[sensor_item.get_name()].add_satisfaction(humidity_satisfaction_eval)
        nb[sensor_item.get_name()].add_satisfaction(co2_satisfaction_eval)

    for i in range(0, SIMULATION_LOOP):    
        for sensor_item in sensors:        
            # Generate sensor data        
            data = sensor_item.get_data()
            nb[sensor_item.get_name()].compute(data)
            nb[sensor_item.get_name()].save_reputation()

    # Plot the reputation probability
    legend = []
    for sensor_item in sensors:
        legend.append(sensor_item.get_name())
        plt.plot(nb[sensor_item.get_name()].get_reputation_history())

    plt.xlabel("Steps")
    plt.ylabel("Trust reputation probability")
    plt.legend(legend)
    plt.show()

def main():

    # Scenario 1: 3 sensors which deliver temperature value. Sensor1 delivers the best values, followed by sensor2 and sensor3.
    #scenario1()

    # Scenario 2: 3 sensors which deliver temperature and humidity value. Sensor1 delivers the best values, followed by sensor2 and sensor3.
    #scenario2()

    # Scenario 3: 3 sensors which deliver temperature and humidity value. Sensor1 delivers the best temperature value and the second best humidity value. Sensor2 delivers
    # the best humidity value and the second best temperature value. Sensor3 delivers the worst value. In this scenario, the temperature has a bigger weight (it is more important
    # than the humidity value.
    #scenario3()

    # Scenario 4: 3 sensors which deliver temperature and humidity value. Sensor1 delivers the best temperature value and the second best humidity value. Sensor2 delivers
    # the best humidity value and the second best temperature value. Sensor3 delivers the worst value. In this scenario, the humidity has a bigger weight (it is more important
    # than the temperature value.
    #scenario4()

    # Scenario 5: 3 sensors which deliver temperature, humidity and CO2 value. Sensor1 delivers the best values, followed by sensor2 and sensor3.
    scenario5()

if __name__ == "__main__":
    main()
