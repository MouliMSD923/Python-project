import math
from collections import Counter
def mean(feature):                             # Function for finding the mean of a feature
    sum_features=sum(feature)
    number_of_features=len(feature)
    return sum_features/number_of_features      # It returns the mean values of a feature

def mode(feature):                             # Function for calculating the mode of a feature
    feature_len=len(feature)
    counter_data = Counter(feature)             # Counting the frequency of each element
    freq_data = dict(counter_data)              # converting the frequency into a dictionary with thier corresponding key
    mode = []
    for k, v in freq_data.items():              
        if v == max(list(counter_data.values())): # if the value is maximum which is equal to the max vlaue present in the list
            mode.append(k)                       
    if len(mode) != feature_len:                
        freq_data=mode                           # if it is not equal then assign mode to frequency data
    else:
        freq_data='NO MODE FOUND'                # If both the lengths are equal, it means that there is no mode value in that feature( all are unique elements)
    return freq_data                            

def variance(feature):
    mean=sum(feature)/len(feature)
    var=sum((n-mean)**2 for n in feature) / len(feature) # Finding the variance of a feature
    return var

def standard_deviation(feature):
    return math.sqrt(variance(feature))                 # Finding the standard deviation of a feature

def maximum(feature):
    max=feature[0]
    for x in feature:                                  # Finding the maximum value of a feature
        if x > max:
            max=x
    return max 

def minimum(feature):
    min=feature[0]
    for x in feature:
        if x<min:                                       # Finding the minimum value of a feature
            min=x
    return min



