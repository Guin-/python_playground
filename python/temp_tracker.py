# Write a class TempTracker with these methods:

# insert()—records a new temperature
# get_max()—returns the highest temp we've seen so far
# get_min()—returns the lowest temp we've seen so far
# get_mean()—returns the mean ↴ of all temps we've seen so far
# get_mode()—returns the mode ↴ of all temps we've seen so far
# Optimize for space and time. Favor speeding up the getter functions (get_max(), get_min(), get_mean(), and get_mode()) over speeding up the insert() function.

# get_mean() should return a float, but the rest of the getter functions can return integers.
# Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..110.

# If there is more than one mode, return any of the modes.

class TempTracker:

    def __init__(self, temp_list):

        # min and max temperatures
        self.min_temp = None
        self.max_temp = None

        # mean temperature
        self.total_temps = 0
        self.total_sum = 0.0
        self.mean = None

        # for mode temperature
        self.mode = None
        self.occurences = [0] * (111)
        self.max_occurences = 0

    def insert(self, temp):

        # for mode
        self.occurences[temp] += 1
        if self.occurences[temp] > self.max_occurences:
            self.mode = temp
            self.max_occurences = self.occurences[temp]

        # for mean
        self.total_temps += 1
        self.total_sum += temp
        self.mean = self.total_sum / self.total_temps

        # for max and min
        if (self.max_temp is None) or (temp > self.max_temp):
            self.max_temp = temp
        if (self.min_temp is None) or (temp < self.min_temp):
            self.min_temp = temp

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


