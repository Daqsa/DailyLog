"""
Deals with fetching info from csv

"""
from os.path import exists
import logger
import time


# always check if csv file exists
if not exists('fullData.csv'):
    print("fullData.csv not found. Creating file...")
    with open('fullData.csv', 'x') as file:
        pass
# get as time_struct
# activity has the format (date, startTime, endTime, duration, contentType, content)
def getLastEndTime():
    with open('fullData.csv', 'rw') as file:
        try: 
            lastLine = file.readlines()[-1]
            entries = lastLine.split(",")
            lastEndTimeStruct = time.strptime(entries[0] + entries[2], "%m-%d-%y%I:%M %p")
            return lastEndTimeStruct
        # maybe file is empty
        except IndexError:
            # empty so write header
            file.write("date,startTime,endTime,duration,type,content")

            # then ask user for last activity, then try again
            print("Last activity not found. Please input the activity starting time that you remember.")
            lastEndTime = logger.get_time()
            lastEndTimeStruct = time.strptime(lastEndTime, "%m-%d-%y %I:%M %p")
            return lastEndTimeStruct
