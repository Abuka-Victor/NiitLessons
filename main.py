import re

pattern = r"^([A-Za-z])([\w|\d]){6}[\d]$"
# pattern = re.compile(pattern)
# print(pattern.search("ff12345678"))

string = "f123456"
string2 = input("Enter a string: ")

match = re.search(pattern, string2)

if match:
    print("Found")
    print(match.groups())
else:
    print("Not found")
