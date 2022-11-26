#1.Create a new class names SciCalc with 3 methods , sum , mull , power all of them takes 2 argument x, y
class SciCalc():
    def sum(self,x,y):
        pass
    def mull(self,x,y):
        pass
    def power(self,x,y):
        pass
#2. Sum return the sum of x and y
#3. Mull return the multiplication of x and y
#4. The power return x power y
class SciCalc():
    def sum(self,x,y):
        return(x+y)
    def mull(self,x,y):
        return(x*y)
    def power(self,x,y):
        return(x**y)
#5. Take an object from the class and call the 3 methodswith any numbers
'''
class SciCalc():
    def sum(self,x,y):
        return(x+y)
    def mull(self,x,y):
        return(x*y)
    def power(self,x,y):
        return(x**y)

s=SciCalc()
s.sum(2,4)
s.mull(3,5)
s.power(2,3)
print(s.sum(2,4))
print(s.mull(3,5))
print(s.power(2,3))
'''
#6. Can we inherit from the class we created in the first task Calc
'''
yes we can
'''
#7. Inherit from the Calc class , now remove theunneeded code the the SciCalc after inheriting
class calc:
    def sum(self,x,y):
        return(x+y)
    def mull(self,x,y):
        return(x*y)

class SciCalc(calc):
   
    def power(self,x,y):
        return(x**y)

s=calc()
s.sum(2,4)
s.mull(3,5)
print(s.sum(2,4))
print(s.mull(3,4))
s=SciCalc()
s.power(2,3)
print(s.power(2,3))

#8.call the 3 methods again from the SciCalc object

s=SciCalc()
s.power(2,3)
print(s.power(2,3))
print(s.sum(2,4))
print(s.mull(3,4))

#9. Now you should see the same result as before
'''
yes it is the saame result
'''

#10.Explain in few words what happened after inheriting
'''
Inheritance enables us to define a class that takes all the functionality from a parent class and allows us to add more
'''
