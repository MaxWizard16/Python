
# print("Twinkle, twinkle little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle little star,\nHow I wonder what you are.")


# first=input("enter your first name:")
# last= input("enter your last name:")
# print(last+" "+first)


# import math
# r=int(input("enter radius;"))
# area=math.pi*r*r
# print(area)


# color_list = ["Red","Green","White" ,"Black"]
# print("first color in the list is:",color_list[0])
# print("last color in the list is:",color_list[3])


# n=int(input("enter a no:"))
# nn=n*n
# nnn=nn*n
# print("n+nn+nnn=",n+nn+nnn)


# seq=input("enter a seq of characters:")
# x=seq.split(',')
# print("given seq can be written in the form of list as:",list(x))
# print("given seq can be written in the form of tuple as:",tuple(x))


# cel=float(input("enter temp in celcius:"))
# fah=(cel*(9/5))+32
# print("this temp in fahr will be:",fah)


# n=int(input("enter 1st no:"))
# m=int(input("enter 2nd no:"))
# x=n
# n=m
# print("after swapping 1st no. is:",n,"and 2nd no. is:",x)
# print("on adding incrementally in 1st var we get:",x+1)


# n=int(input("enter a no:"))
# if n%2==0:
#     print("given no. is even")
# else:
#     print("given no. is odd")


# yr=int(input("enter any year:"))
# if yr%4==0:
#   print("leap year")
# else:
#   print("not a leap year")


# import math
# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print("The Euclidean distance between the points is:", distance)


# x=float(input("enter 1st angle:"))
# y=float(input("enter 2nd angle:"))
# z=float(input("enter 3rd angle:"))
# if x+y+z==180:
#   print("triangle is possible")
# else:
#   print("triangle is not possible")


# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the annual interest rate (in %): "))
# time = float(input("Enter the time in years: "))
# n = int(input("Enter the number of times interest is compounded per year: "))
# amount = principal * (1 + rate / (100 * n)) ** (n * time)
# print("compound interest=",amount-principal)
# print("total amount=",amount)


# N=int(input("enter a no:"))
# if N > 1:
#     for i in range(2, N):
#         if N % i == 0:
#             print(N, "is NOT a Prime Number")
#             break
#     else:
#         print(N, "is a Prime Number")
# else:
#     print(N, "is NOT a Prime Number")


# n=int(input("enter a no:"))
# sq=0
# for i in range(1,n+1):
#   sq+=i**2
# print("sum of sqs of all the nos till n is:",sq)