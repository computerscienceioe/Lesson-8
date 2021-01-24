
strings = []

for i in range(2):
  strings.append(input("Please enter a string: "))


for i in range(len(strings)):
  
  print("Word length is:",len(strings[i]))
  
  lowerCaseWord = strings[i].lower()
  vowelCount = 0
  for j in range(len(lowerCaseWord)):
    if lowerCaseWord[j] == "a" or lowerCaseWord[j] == "e" or lowerCaseWord[j] == "i" or lowerCaseWord[j] == "o" or lowerCaseWord[j] == "u":
      vowelCount = vowelCount + 1
  print("The word has", vowelCount, "vowels")
  print("Vowels are", round(vowelCount/len(lowerCaseWord)*100, 2), "percent of the word")


  
