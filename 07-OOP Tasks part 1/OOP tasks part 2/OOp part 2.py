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
