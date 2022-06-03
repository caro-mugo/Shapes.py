import math
    #Question1
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        A=math.pi*(self.r**2)
        return A
        
    def circumfrence(self): 
        c=math.pi*2*self.r
        return c
    #Question2
class Square:
    def __init__(self,s):
        self.s=s
    def square(self):
        print(self.s*self.s)
    def perimeter(self):
        perimeter=(4* self.s)
        print(f"Square perimeter {perimeter}")
      
       # Question3
class Rectangle:
    def __init__(self,w,l):
        self.w=w.self.l=l
    def rectangle_area(self):
        p=self.w*self.l
        return p
    def perimeter(self):
        L=2*self.l+self.w 
        return L
    
    #question4
class Sphere:
    def __init__(self,r):
        self.r=r
    def area_surface(self):
        W=4*math.pi*self.r**2
        return W
    def The_Volume(self):
        N=4/3*math.pi*self.r**3
        return N
    
        
        