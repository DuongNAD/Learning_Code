# # Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

# C1:
cp = 0
cn = 0
for i in data1:
    if i > 0 :
        cp += 1
    else:
        cn += 1

# C2:
cp = sum(1 for i in data1 if i > 0)
cn = sum(1 for i in data1 if i < 0)

# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

result2 =[]
for i in data2:
    a = data2.count(i)
    if a > k and i not in result2 :
        result2.append(i)
print(result2)

# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

result3 =[]
for i in range(len(data3) - 1 ):
    if data3[i] > data3[i+1] :
        result3.append(data3[i])
    else:
        result3.append(data3[i + 1])
print(result3)

# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

for i in data4:
    for j in data4:
        for k in data4:
            print(i,j,k)

# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

result5 =[]
for i, j in zip(data5_list1, data5_list2):
    result5.append(i+j)

# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# C1
result6 =[]
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0 :
        result6.append(str(i))
result6 = ', '.join(result6)
print(result6)

# C2
result6 = [str(num) for num in range(2000,3201) if num % 7 == 0 and num % 5 != 0 ]
result6 = ', '.join(result6)

print(result6)

# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

result7 = []
for i in range(1000,3001):
    a = i % 10
    b = (i//10) % 10
    c = ( i // 100 ) % 10
    d = i // 1000
    if a % 2 == 0 and a != 0 and b % 2 == 0 and b != 0 and c % 2 == 0 and c != 0 and d % 2 == 0 and d != 0 :
        result7.append(str(i))

result7 = ', '.join(result7)
print(result7)
































