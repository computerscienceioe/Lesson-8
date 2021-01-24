
strings = []

for i in range(2):
  strings.append(input("Please enter a string: "))

for i in range(len(strings)):
  strings[i] = strings[i].lower()

for i in range(len(strings)):
  print(len(strings[i]))
  print(strings[i][:2])
  print(strings[i][-2:])
