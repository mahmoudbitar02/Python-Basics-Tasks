#1. Print numbers from O to 10 using while
'''
x=0
while x < 11:
    print (x)
    x+=1
'''

#2. Print numbers from O to 10 using for
'''
x=[0,1,2,3,4,5,6,7,8,9,10]

for i in (x):
    print (i)
'''
#3. Stop the loop if the number = 5
'''
x=[0,1,2,3,4,5,6,7,8,9,10]

for i in (x):
    print (i)
    if i==5 :
        break
'''
#4. Skip the 5 iteration from print---------------------
'''
x=[0,1,2,3,4,5,6,7,8,9,10]

for i in (x):
    print (i)
    if i==5 :
        continue
'''
#5. Print multiplication table from 1 to 5--------------------
'''
for i in range(1,6):
    for y in range(1,6):
        print(i*y)
'''
#6. How to get numbers from 10 to 20 using range
for i in range(10, 21):
    print (i)
