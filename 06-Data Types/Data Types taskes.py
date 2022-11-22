#1. What is the differences between ' '' '''
#' '' have no differences but if we use ''' we can whrite the code in several lines

#2. Create a string with the name 'mystero'
name = 'mystro'

#3. Make the string letters capital
name = 'mystro'
print(name.upper())

#4. Create a list of values from 10 to 20
lis=[10,11,12,13,14,15,16,17,18,19,20]
lis.append(30)
print(lis)

#5. Add 30 to the end of the list
lis=[10,11,12,13,14,15,16,17,18,19,20]
lis.append(30)
print(lis)

#6. Add 40 as the second element of the list
lis=[10,11,12,13,14,15,16,17,18,19,20]
lis.append(30)
lis.insert(1,40)
print(lis)

#7. Print how many elements in the list
'''
look to question number 5 and 6
'''

#8. replace the second element in the list with 100

lis=[10,11,12,13,14,15,16,17,18,19,20]
lis[1] = '100'
print(lis)

#9. Create a tuple with values from 1 to 5
mah = (1,2,3,4,5)

#10. Can we add 10 to the end of the tuple?
'''
no we cannot add value to a tuple
'''

#11. Create a dict of value Mahmoud:28, ahmed:30

x = {'mahmoud':28, 'ahmed':30}

#12. Print Mahmoud age from the dict
x = {'mahmoud':28, 'ahmed':30}
print(x['mahmoud'])

#13. What is the differences between mutable and immutable data types?
'''
immutable: we cannot add, remove or replace etc. the Values (Tuple is a immutable)
mutable: we can add, remove or replace etc. the Values (list ist a mutable)
'''
