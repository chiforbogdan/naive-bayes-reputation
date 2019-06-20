from feature_type import *

class naive_bayes:

    def __init__(self, sensor_name, feature_weights, satisfaction_threshold):
        self.__satisfactions = []
        self.__sensor_name = sensor_name
        self.__feature_weights = feature_weights
        # Conditional Probability Table (CPT)        
        self.__cpt = {}
        self.__satisfaction_threshold = satisfaction_threshold
        # Initialize interaction counters
        self.__total_interactions = 0
        self.__success_interactions = 0
        self.__reputation_history = {}
        self.__simulation_steps = 0


    def add_satisfaction(self, satisfaction):
        self.__satisfactions.append(satisfaction)
        # Init CPT entry
        self.__cpt[satisfaction.get_feature_type()] = 0
        self.__reputation_history[satisfaction.get_feature_type()] = []

    def compute(self, data):
        # Increment the total number of interactions
        self.__total_interactions = self.__total_interactions + 1
        
        # Compute the interactions satisfaction score (taking into consideration all features)
        satisfaction_score = 0
        for satisfaction in self.__satisfactions:
            satisfaction_score = satisfaction_score + self.__feature_weights[satisfaction.get_feature_type()] * satisfaction.get_satisfaction(data)

        if satisfaction_score >= self.__satisfaction_threshold:
            self.__success_interactions = self.__success_interactions + 1

            # Update the CPT
            for satisfaction in self.__satisfactions:
                if satisfaction.get_satisfaction(data) >= self.__feature_weights[satisfaction.get_feature_type()] * self.__satisfaction_threshold:
                    self.__cpt[satisfaction.get_feature_type()] = self.__cpt[satisfaction.get_feature_type()] + 1

    def __get_feature_reputation(self, feature):
        
        if self.__total_interactions == 0 or self.__success_interactions == 0:
            return (0,0)        

        trust_probability = self.__success_interactions / self.__total_interactions

        # Compute the CPT reputation
        feature_probability = self.__cpt[feature] / self.__total_interactions

        return (feature_probability / trust_probability, trust_probability)

    def save_reputation(self):

        # Compute reputation for each feature
        for feature in self.__cpt.keys():
            self.__reputation_history[feature].append(self.__get_feature_reputation(feature))

        self.__simulation_steps = self.__simulation_steps + 1

    def get_reputation_history(self, features):

        reputation_history = []

        for i in range(self.__simulation_steps):
            
            # Init reputation score with trust probability
            reputation_score = self.__reputation_history[features[0]][i][1]

            for feature in features:
                reputation_score = reputation_score * self.__reputation_history[feature][i][0]

            reputation_history.append(reputation_score)
        
        return reputation_history

