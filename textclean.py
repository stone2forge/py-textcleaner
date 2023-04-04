import re
# string with multiple consecutive
print("TEXT NOW!")
print("------------------------------")
s = input()
# make spaces consistent
s = re.sub(" +", " ", s)
print ("------------------------------")
print("TEXT HERE!")
print(s)
print ("------------------------------")
