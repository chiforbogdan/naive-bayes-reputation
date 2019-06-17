
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
        self.__reputation_history = []


    def add_satisfaction(self, satisfaction):
        self.__satisfactions.append(satisfaction)
        # Init CPT entry
        self.__cpt[satisfaction.get_feature_type()] = 0

    def compute(self, data):
        # Increment the total number of interactions
        self.__total_interactions = self.__total_interactions + 1
        
        # Compute the interactions satisfaction score (taking into consideration all features)
        satisfaction_score = 0
        feature_set = []
        for satisfaction in self.__satisfactions:
            satisfaction_score = satisfaction_score + self.__feature_weights[satisfaction.get_feature_type()] * satisfaction.get_satisfaction(data)
            feature_set.append(satisfaction.get_feature_type())

        if satisfaction_score >= self.__satisfaction_threshold:
            self.__success_interactions = self.__success_interactions + 1

            # Update the CPT
            for feature in feature_set:
                self.__cpt[feature] = self.__cpt[feature] + 1

    def get_reputation(self):
        
        if self.__total_interactions == 0 or self.__success_interactions == 0:
            return 0        

        trust_probability = self.__success_interactions / self.__total_interactions

        reputation_score = trust_probability        
        
        # Compute the CPT reputation
        for value in self.__cpt.values():
            feature_probability = value / self.__total_interactions
            reputation_score = reputation_score * feature_probability / trust_probability

        #return self.__success_interactions
        return reputation_score

    def save_reputation(self):
        self.__reputation_history.append(self.get_reputation())

    def get_reputation_history(self):
        return self.__reputation_history
