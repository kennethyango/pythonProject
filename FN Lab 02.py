# Miscellaneous Topic


# Example 1
# count=0
# for i in range(10):
#     num = eval(input("Enter a number: "))
#     if num>10:
#         count = count + 1
#     print("Count #: ",count)
# print("There are", count, 'numbers greater than 10')

#Example #2
# count1 = 0
# count2 = 0
# for i in range(5):
#     num = eval(input('Enter a number: '))
#     if num>10:
#         count1=count1+1
#     print("Count # (More than 10): ", count1) # track counting
#     if num==0:
#         count2=count2+1
#     print("Count # (Equal to 0): ", count2) # track counting
# print('There are', count1, 'number(s) greater than 10.')
# print('There are', count2, 'zero(es).')

#Example 3
# count = 0
# for i in range(1,101):
#     if (i**2)%10==4:  #Modulus Division  (** exponentiation)
#         print(i**2, end=' ')
#         count = count + 1
# print()
# print("Total # of digits that end in 4:",count)

#
# print(1000000505%10)



# Example #4
# sum = 0
# for i in range(3,101,3):
#     print(i, end=' + ')
#     sum = sum + i
# print()
# print('The sum is', sum)


#Example #5
# s = 0
# for i in range(10):
#     num = eval(input('Enter a number: '))
#     s = s + num
# print('The average is', s/10)
#
#
# x = 5
# y = 3
#
# x,y = y,x
# print(x)
# print(y)

# hold = x        #hold = 5
# x = y            # x = 3
# y = hold         # y = 5


# x=y         #x = 5
# y=x         #y = 5

# # Maxes and Mins
# largest = eval(input('Enter a positive number: '))
# for i in range(9):
#     num = eval(input('Enter a positive number: '))
#     if num>largest:
#         largest=num
#     print("The current largest number: ", largest)
# print('Largest number:', largest)


# Example Programs

# from random import randint
#
# rand_num = randint(5,25)
# print("random number generated: ",rand_num)
# for i in range(rand_num):
#     print('Hello')

# from random import randint
# for i in range(6):
#     rand_num = randint(1, 5)
#     # print("random number generated: ", rand_num)
#     print('Hello' * rand_num)


#


from random import randint
count = 0
for i in range(10000):
    num = randint(1, 100)
    if num%12==0:
        count=count+1       #count += 1
        print('Number of multiples of 12:', count)