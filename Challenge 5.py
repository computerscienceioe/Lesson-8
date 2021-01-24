
strings = []

for i in range(2):
  strings.append(input("Please enter a string: "))

reverseStrings = []

# Method One
# for i in range(len(strings)):
#   word = ""
#   for j in range(len(strings[i])):
#     word = word + strings[i][len(strings[i])-1-j]
#   reverseStrings.append(word)

# Method Two
# for i in range(len(strings)):
#   word = ""
#   for j in range(len(strings[i])-1, -1, -1):
#     word = word + strings[i][j]
#   reverseStrings.append(word)

# Method Three
for i in range(len(strings)):
  reverseStrings.append(strings[i][::-1])

print(reverseStrings)

