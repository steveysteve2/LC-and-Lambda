''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenlist = list(filter(lambda num: (num%2==0), numbers_list))
oddlist = list(filter(lambda num: (num%2==1), numbers_list))   #produces list object

print(f"Even numbers in list: {evenlist}")
print(f"Odd numbers in list: {oddlist}")


''' 2)
find which days of the week have exactly 6 characters.
'''
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sixlist = list(filter(lambda word: (len(word)==6), weekdays))

print(sixlist)


''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
colorlist = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_words = ['orange','black']

newlist = list(filter(lambda word: (word not in remove_words), colorlist))

print(newlist)


''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

newlist = list(filter(lambda num: (num not in list2), list1))

print(newlist)


''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search: 'ack'
Elements of the said list that contain specific substring: ['black']
Substring to search: 'abc'
Elements of the said list that contain specific substring: []

'''
list3 = ['red', 'black', 'white', 'green', 'orange']
sub = 'lue'

newlist1 = list(filter(lambda word: (sub not in word), list3))

print(newlist1)

''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

#str1 = "Hello8world"
str1 = "HELLo123!!"
#str1 = "hello"

#checks if password has uppercase, lowercase, number, and min of 8 characters
check = lambda s: all([any(char.isupper() for char in s), 
                       any(char.isupper() for char in s),
                       any(char.isupper() for char in s), 
                       len(s)>=8])

val = check(str1)
print(val)


''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

def call(score):
    return score[1]

num_scores = sorted(list(filter(lambda subject: subject, original_scores)), key=call)

print(num_scores)

# def sort(scores):          <--    alternative way without using lambda!
#      return sorted(scores, key=call)

# print(sort(original_scores))
