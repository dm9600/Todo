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
    