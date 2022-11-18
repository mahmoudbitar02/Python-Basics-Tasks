#1.Check if 10 is bigger than 15 or not


number = 10
if number > 15 :
    print('number > 15')

#2.If 10 is not bigger than15 print × is smaller than 15
number = 10
if number > 15 :
    print('number > 15')
else:
    print('number<15')
#3. In which cases we will use all
'''
we will use (all) if we have alot of (and), so we can add a list as the example 
x = 5
y = 10
z = 15

if all ([x==5,y==10,z==15]):
    print ('hallo')
'''
#4. What is the differences between all, and
'''
all: we shold use it with list (example see above)
and: we dont nead a list but we should write alle values (example
                                                          x=1
                                                          y=2
                                                          z=3
                                                          if x ==1 and y==2 and z==3
                                                              print ('HI'))

'''
#5. What is the differences between any, or
'''
any: we shold use it with list (example
x = 5
y = 10
z = 15

if any ([x==5,y==10,z==15]):
    print ('hallo'))
or: we dont nead a list but we should write all values (example
                                                          x=1
                                                          y=2
                                                          z=3
                                                          if x ==1 or y==2 or z==3
                                                              print ('HI'))
'''

#6.If we need all the conditions to be true we will use
'''
all
'''
#7.What is the differences between if, elif
'''
we can use (if) one time but we can use (elif) as we wich.
'''
#8. What is the differences between elif else
'''
we can use (elif) alot, as we wich but else one time
'''
#9. Can we use more than one elif
'''
no
'''
#10. Can we use more than one else
'''
in a function we use onle one 
'''
#11. writes simple ternary operator
'''
x=50

print ('50') if x == 50 else  print ('error')
'''
#12. in elif, python will check all the conditions no matter what?
'''
no, if the (elif) inside a (if) it will check it first when the first (if) ably to check
'''

#13 in elif we use else for?
'''
default option if no condition is true
'''
#14. if we have this list [2.4.6.8.10] :

    #1.check to see if 4 in this list or not
'''
list = [2,4,6,8,10]
if 4 in list :
    print('done')
'''
    #2. check to see if 4 and 6 in this list on not
'''
list = [2,4,6,8,10]
if 4 and 6 in list :
    print('done')
'''

    #3. check to see if 3 or 6 in this list
'''
list = [2,4,6,8,10]
if 3 or 6 in list :
    print('done1')
'''

    #4. check to see if 2, 4 and 5 in this list
list = [2,4,6,8,10]
if all ([2, 4, 5]) in list :
    print('done')
else : print ('error')



