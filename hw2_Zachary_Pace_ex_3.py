'''
Homework 2-3
Name: Zachary Pace
Date: 2/16/2023
Description: playing with lists
'''

# part 1
List = ["Wallet", "Phone", "Keys"]
print(List)

# part 2
List.sort()
print(List)

# part 3
print(List[0])

# part 4
print(List[1:])

# part 5
print(List[-1])

# part 6
print(List.index("Keys"))

# part 7
List.append("Tablet")
print(List)

# part 8
List.insert(1, "Mask")
print(List)

# part 9
List.remove("Phone")
print(List)

# part 10
List.reverse()
print(List)


# part 11
def strList(List):
    Str = List[0]
    index = 1
    while index != len(List)-1:
        Str = Str + ", " + str(List[index])
        index = index + 1
    Str = Str + ", and " + str(List[index])
    return Str


print(strList(List))