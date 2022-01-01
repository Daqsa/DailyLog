"""
Reason for switching to programs instead of sheets: logging on Google sheets is too repetitive. I want to automate the process

01-01-22 Project starts



"""
from datetime import datetime
import time
import fetcher

def main():
    store_entry()



def store_entry():
    userInput = get_input()
    formattedUserInput = format_input(userInput)
    usefulInfo = extract_info(formattedUserInput)
    store_input(usefulInfo)



def get_input():
    
    """
    Format required
    Time : {mm-dd-yy hh:mm AM/PM}
    Type : {prdt/rest/sleep}
    Content : {string describing the activity}
    """
    print("Input activity in the following format: {Time}, {Type}, {Content}")

    userInput = input()
    # regex to check format



    return userInput


def get_time():
    print("Input time in the following format: {mm-dd-yy hh:mm AM/PM}")
    inputTime = input()
    return inputTime


def format_input(userInput):
    tokens = userInput.split(",")
    tokens = list(map(str.strip, tokens))
    
    # Time, {mm-dd-yy hh:mm AM/PM}
    formattedTime = time.strptime(tokens[0], "%m-%d-%y %I:%M %p")

    # Type
    formattedType = tokens[1].lower()
    
    # Content
    # nothing to change
    formattedContent = tokens[2]
    
    return (formattedTime, formattedType, formattedContent)



"""
assume format (EndTime, Type, Content)
where EndTime is struct_time
Type is prdt, rest, or sleep
Content is string

Need Date(mm:dd:yy), StartTime(hh:mm), EndTime(hh:mm AM/PM), Duration(mm), Type, Content
"""
def extract_info(userInput):
    startTimeStruct = fetcher.getLastEndTime()
    endTimeStruct = userInput[0]
    date = time.strftime("%m-%d-%y", startTimeStruct)
    startTime = time.strftime("%I:%M %p", startTimeStruct)
    endTime = time.strftime("%I:%M %p", endTimeStruct)
    duration = computeDuration(startTimeStruct, endTimeStruct).total_seconds() / 60
    duration = str(round(duration, 2))
    contentType = userInput[1]
    content = userInput[2]
    
    finalInfo = (date, startTime, endTime, duration, contentType, content)
    finalInfoStr = ",".join(finalInfo)
    return finalInfoStr

    
# computes the duration between two time_struct and returns a timeDelta
def computeDuration(startTime, endTime):
    # convert to dateTime objects first
    st = datetime.fromtimestamp(time.mktime(startTime))
    et = datetime.fromtimestamp(time.mktime(endTime))
    # print("starting time:", st, "\nending time: ", et)
    dt = et - st
    return dt



def store_input(userInput):
    with open('fullData.csv', 'a') as file:
        file.write(userInput + "\n")


    
if __name__ == "__main__":
    main()
