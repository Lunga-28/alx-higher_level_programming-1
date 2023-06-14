#!/usr/bin/python3
def best_score(a_dictionary):
    
    max_scor = None
    
    max_key = None

    for key, value in a_dictionary.items():
        
        if max_scor is None or value > max_scor:
            
            max_scor = value
            max_key = key

   
    return max_key
