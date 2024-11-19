import random

#the list, always in square brackets

x = [349, "Hello" , 21]

print(random.choice(x))

#from left to right (0,1,2,3)

print (x[0])

#from right to left

print (x[-3])

#len = length- to measure length of variables, e.g print (len(name of list here))

print (len(x))

#to add, e.g. x.append("name of variable here") 

x.append("rock")

#to replace

x.insert(1,"a")

#to remove last value, e.g. x.pop(number inserted here without speech marks)

x.pop()

#Create 2d list, like list inside list, e.g. list name here = [[random stuff in list1],[random stuff in list2],[random stuff in list3]]
#the recognisable index of the things in the list
#          0       1       2
#       [[0,1,2],[0,1,2],[0,1,2]]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print (matrix)

#No. of rows

print(len(matrix))

#No. of columns

print(len(matrix[0]))

for i in range (3):
    for j in range (3):
        print(matrix[i][j], end=" ")
    print("\n")





