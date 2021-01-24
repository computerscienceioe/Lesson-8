timeInput = input("Enter a time in the format hh:mm:ss : ")

# Method One
# hours = int(timeInput[:2])
# minutes = int(timeInput[3:5])
# seconds = int(timeInput[6:8])

# timeInMinutes = hours*60 + minutes + seconds/60
# print("The time in minutes is", timeInMinutes)

# timeInSeconds = hours*60*60 + minutes*60 + seconds
# print("The time in seconds is", timeInSeconds)

# Method Two
# This method only requires that the time be split with a :
timeSplit = timeInput.split(":")
print(timeSplit)
hours = int(timeSplit[0])
minutes = int(timeSplit[1])
seconds = int(timeSplit[2])

timeInMinutes = hours*60 + minutes + seconds/60
print("The time in minutes is", timeInMinutes)

timeInSeconds = hours*60*60 + minutes*60 + seconds
print("The time in seconds is", timeInSeconds)
