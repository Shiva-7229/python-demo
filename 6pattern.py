# half pyramid in python
"""a = "python"
b = ""
for i in a:
    b = i+b
    print(b)"""
"""for i in range(5):
    for j in range(i+1):
        print(j, end="")
    print("")"""
"""for i in range(5):
    for j in range(i+1):
        print(i, end="")
    print("")"""

for i in range(5):
    for j in range(i):
        print(""*j,"*", end="")
    print("")