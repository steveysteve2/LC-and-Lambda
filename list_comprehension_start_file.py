'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''

original_list = ['Todd', 'Brad', 'Steven']
new_list = []
# for i in original_list:
#     if filter(i):
#         new_list.append((i))

#You can obtain the same thing using list comprehension:

#new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

#There are 3 parts to list comprehension:

#*result*  = [*transform/expression*    *iteration*         *filter*     ]

#The filter part answers the question if the item should be transformed.

x = [i for i in range(10)]
print(x)

#add an expression
squares = [x**2 for x in range(10)]
print(squares)

list1 = [3,4,5]

multilist = [i*3 for i in list1]
print(multilist)

listwords = ['this', 'is', 'a', 'list', 'of', 'words']

results = [word[0].upper() for word in listwords]
print(results)

#adding an IF condition
#sqaure of all even numbers 1-10

squarelist = [(i)**2 for i in range(1,11) if i % 2 == 0]
print(squarelist)

string = 'Hello world 1234'

numbers = [int(x) for x in string if x.isdigit()]
print(numbers)

list3 = range(1,21)
# for x in list3:
#     if x%2 == 1:
#         y = x * 100
#         list3.append(y)

# print(list3)

list4 = [x*100 for x in list3 if x%2 == 1]
print(list4)

#using list comprehension

infile = open('test.txt','r')

results = [i.rstrip('\n') for i in infile if 'line3' in i]
print(results)

def double(x):
    return x*2

print(double(10))

result = [double(x) for x in range(10) if x%2 == 0]

print(result)

result1 = [double(x+y) for x in [10,20,30] for y in [20,30,40]]
print(result1)

## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)

## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
words1 = [len(word) for word in words if word != 'the']
print(words1)

## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict1={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

newlist1 = [k.upper() for k,v in dict1.items() if v<5000]
print(newlist1)

## Find all the numbers from 1 to 1000 that have a 4 in them
newlist2 = [num for num in range(1,1000) if '4' in str(num)]
print(newlist2)

## count how many times the word 'the' appears in the text file - 'sometext.txt'
infile = open('sometext.txt', 'r')

text = infile.read()
textlist = text.split()

the_list = [word for word in textlist if word == 'the']
print(len(the_list))

## Extract the numbers from the following phrase ##

phrase = 'In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each event, with about 3 or 4 that were classifled as serious per event.'

numbers2 = [int(x) for x in phrase if x.isdigit()]
print(numbers2)

