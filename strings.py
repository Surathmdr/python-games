# course = "Python's for Beginners" #to use ' in middle of a string we should use ""in end and start
# #if you want ot use " in middle of a string we should use ''in start and end and if you want to use ' in middle of a string  we should use ""in the start and end

# # # # to define a string in multiplee length
# # i.e MULTI LINE STRING or MULTI LINE SENTENCE
# # use 3 single ar double quotes
# course = ''' 
# Hi John,

# Here is our first email to you.

# Thank you,
# The support team

# '''

# print(course)


# # to display a word by number
# #use [] brackets
# course =  'Python for Beginners'
# print(course[0])
# # to get word from back use negative number
# course =  'Python for Beginners'
# print(course[-1])

# #to display words from a number to another number
# course = 'Python for
#  Beginners '
# #numbers =0123456789
# another = course[:]
# print(another)

# name = 'Jennifer'
# print(name[1:-1])
# #nit starts from 1that is e and ends at -1 which is e


#   # # # # # # # # # # Formatted strings

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# #using format string
# msg = f'{first} [{last}] is a coder'
# print(msg)

# ### STRING METHODS

# course ='Python for Beginners'
# print(len(course))
# #  len function counts the number of letters in a variables
# print(course.upper())
# # upper function turns all letters into uppers case 
# print(course.lower())
# # lower functionn turns all letters into lower case

# # to find the number of letter by the word 
# course ='Python for Beginners'
# print(course.find('s'))

# # to replace something in the string
# course ='Python for Beginners'
# print(course.replace('Beginners','Absolute Beginners'))

course ='Python for Beginners'
print('Python' in course)