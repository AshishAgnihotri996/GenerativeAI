# Input:
# N = 5
# Output:
# 5 10 15 20 25 30 35 40 45 50

# def multiplicationTable(N):
#     return [i * N for i in range(1, 11)]
#
# multiplicationTable(5)

# Input: s = "DoctorPhenomenal"
# Output: DcoPeoea

# s = "DoctorPhenomenal"
# result=""
# for i in range(len(s)):
#     if i%2==0:
#         result +=s[i]
# print(result)

# Input: x = 3
# Output: 3 2 1 0
# Explanation:
# Numbers in decreasing order from 3
# are 3, 2, 1, 0.

# x= 3
# while x>=0:
#     print(x,end=" ")
#     x-=1

# Input: x = 10
# Output: 1 4 9
# Explanation:From 1 to 10, numbers in powers of 2 are, 12, 22, 32 as 1, 4 and 9.

# x =10
# i = 0
# while i*i<x:
#     print(i*i,end="")
#     i+=1


# n = 0
# Output:
# already Zero


def demo(n):
    if n==0:
        print("zero")
    elif n>0:
        while n>0:
            n=n-1
            print(n)
    else:
        while n<0:
            n=n+1
            print(n)
n= -5
demo(n)