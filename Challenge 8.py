name = input("Enter your full name, separated by only a space: ")

spaceIndex = name.index(" ")

firstName = name[:spaceIndex]
surname = name[spaceIndex+1:]

print("Your first name is", firstName)
print("Your surname is", surname)
