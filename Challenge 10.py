timeInput = int(input("Enter a 5 digit time in seconds: "))

seconds = timeInput % 60
timeInput = timeInput // 60
minutes = timeInput % (60)
timeInput = timeInput // 60
hours = timeInput % (60)

print("The time is", hours, "hours,", minutes, "minutes and", seconds, "seconds.")

print("The time is", minutes+hours*60, "minutes and", seconds, "seconds.")


