#A class to validate todos

import os
import pdb

class Error:
    PRIORITY_NOT_NUMBER = "Priority is not a number"
    PRIORITY_NOT_WITHIN_RANGE = "Priority needs to be between one and five"

class Constant:
    EMPTY_STRING = ""

#Check if a file. True if exists, else false
def does_file_exist(filename):
    returnValue = False
    if not os.path.isfile(filename):
        try:
            with open(filename + ".ser") as f: pass
        except IOError as e:
            returnValue = True
    else:
        returnValue = True
    return returnValue

#Check if it's a number (for priority)
def is_number(anything):
    try:
        float(anything)
        return True
    except ValueError:
        return False

#Check if a number is within range (1-5)
def is_priority_in_range(priority):
    return_value = true
    if priority < 1 or priority > 5: 
        return_value = false
    return return_value

#Check if a priority is valid
def is_valid_priority(priority):
    return_value = Constant.EMPTY_STRING
    if not is_number(priority):
        return_value = Error.PRIORITY_NOT_NUMBER
    elif not is_priority_in_range(priority):
        return_value = Error.PRIORITY_NOT_WITHIN_RANGE
    return return_value
        
        