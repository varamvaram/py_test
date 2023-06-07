"""
program to create a histogram from a given list of integers
"""
length_value=int(input("Enter the length values:"))
LST = []

for i in range(length_value):
    NUMBER=int(input("Enter the item: "))
    LST.append(NUMBER)

print("Histogram:")
HISTOGRAM = "* "
for i in LST:
    print(HISTOGRAM * i)
