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

x=[0,1,2,3,4,5,6,7,8,9,10]

for i in (x):
    print (i)
    if i==5 :
        break

#4. Skip the 5 iteration from print
'''
x=[0,1,2,3,4,5,6,7,8,9,10]
for i in (x):
    
    if i==5 :
        continue
    print(i)
'''
#5. Print multiplication table from 1 to 5
'''
for i in range(1,6):
    print('-----------------------')
    for y in range(1,6):
        print(f"{i} X {y} = {i*y}")
'''
#6. How to get numbers from 10 to 20 using range
'''
for i in range(10, 21):
    print (i)
'''
#7. How to get numbers from 10 to 100 with 3 at each step using range
'''
for i in range(10, 100, 3):
    print (i)
'''
#8. Get a list of even numbers from 1 to 100 using for
'''
start = int(input('enter the stating number: ' ))
end = int(input('enterthe end number: '))

for i in range(start, end, 2):
    print(i)
'''

#9. Get a list of even numbers from 1 to 100 using while
start = int(input('enter the stating number: ' ))
end = int(input('enterthe end number: '))
x=99
while (x<100) in range (start, end,2):
    print (x)
