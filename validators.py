import os

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
    
    