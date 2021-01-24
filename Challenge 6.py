
strings = []

for i in range(2):
  strings.append(input("Please enter a string: "))


for i in range(len(strings)):
  
  strings[i] = strings[i].lower()

  # Method One
  # found = False
  # for j in range(len(strings[i])):
  #   if strings[i][j] == "a":
  #     found = True
  # if found:
  #   print("Found a")
  # else:
  #   print("Did not find a")

  # Method Two
  if strings[i].__contains__("a"):
    print("Found a")
  else:
    print("Did not find a")
