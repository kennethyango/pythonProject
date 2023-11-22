# PYTHON PROGRAMMING
# LISTS
# L = [1,2,3,4,5]
# print(type(L))

# L = eval(input('Enter a list: '))
# print('The sixth element is ', L[5])
# print(type(L))


# Printing a list
# L = [2,4,6,8,0,1,3,5,7,9]
# print(L)

# List of different data types
# L = [1, 2.718, 'abc', [5,6,7]]
# print(L)
# print(type(L))


# print([0] * 5)

# L = [1,2,3,4,5]
# for i in range(len(L)):
# 		print(L[i])

# for item in L:
#     print(item)


# L = [1,2,3,4,5]
# print(max(L))


# L = [ 95,75,88,99,25,79]
# L = eval(input('Enter scores'))
# average = sum(L)/len(L)
# print(average)

#
# L = [95,75,88,99,25,79]
# M = L[:]
# L.sort()
# print('List M: ',M)
# print('List L: ',L)
# L[3] = 100
# print(L)

# L = [6,7,8]
# L[1] = 9          #replace index 1 with item value 9
# print(L)
# L.insert(1,5)
# print(L)
# del L[0]
# print(L)
# del L[:2]
# print(L)

# Example 1 Write a program that generates
# a list L of 50 random numbers between 1 and 100.
# append()	Adds an element at the end of the list

# from random import randint
# L = []
# for i in range(50):
#     L.append(randint(1,100))
# print(L)
# L.sort()
# print(L)
#Example 2 Replace each element in a list L with its square.
# L = [1,2,3,4,5,6] #[1,4,6,8,10,12]
# for i in range(len(L)):
#     L[i] = L[i]**2
# print(L)

# Example 3 Count how many items in a list L are greater than 50.
# from random import randint
# L = []
# for i in range(50):
#     L.append(randint(1,100))
# count = 0
# print(L)
# for item in L:
#     if item>50:
#         count=count+1
# print("The count of items greater than 50 is: ", count)



#Example 4 Given a list L that contains numbers
# between 1 and 100, create a new list whose first
# element is how many ones are in L,
# whose second element is how many twos are in L, etc.
# from random import randint
# L = []
# for i in range(50):
#     L.append(randint(1,100))
# print("List L: ",L)
# frequencies = []
# for i in range(1,101):
#     frequencies.append(L.count(i))
# print("Frequency List: ",frequencies)





#Example 5 Write a program that prints out the two
# largest and two smallest elements of a list called scores.
# from random import randint
# scores = []
# for i in range(20):
#     scores.append(randint(1,100))
# print("List Scores: ",scores)
# scores.sort()
# print("List Scores(sorted): ",scores)
# print("Two highest: ", scores[-1],scores[-2])
# print("Two lowest: ", scores[0],scores[1])


# Example 6 Sample Quiz Play
questions = ['What is the capital of France?',
			'Which state has only one neighbor?']
answers = ['Paris','Maine']
num_right = 0
for i in range(len(questions)):
	guess = input(questions[i])
	if guess.lower()==answers[i].lower():
		print('Correct')
		num_right=num_right+1
	else:
		print('Wrong. The answer is', answers[i])
	print('You have', num_right, 'out of', i+1, 'right.')