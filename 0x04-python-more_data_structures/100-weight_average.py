#!/usr/bin/python3
def weight_average(my_list=[]):
    
    if len(my_list) == 0:
        return 0
    
    total_scor = 0
    
    total_weight = 0

    for score, weight in my_list:
        
        total_scor += score * weight
        
        total_weight += weight
    
    weighted_average = total_scor / total_weight
    
    return weighted_average
