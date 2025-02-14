
class Coordinate(object):
    def __init__(self,input_x,input_y):
        self.x = input_x
        self.y = input_y
        
    def __str__(self):
        return "<{},{}>".format(self.x,self.y)
        #return "<" + str(self.x)+","+str(self.y)+">"
        
    def distance(self,other):
        assert type(other) == Coordinate
        x_2 = (self.x - other.x) ** 2 
        y_2 = (self.y - other.y) ** 2 
        return (x_2 + y_2) ** 0.5
        
        
c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x)
print(origin.y)
print(origin.distance(c))
print(c)


class fraction(object):
    def __init__(self,num,den):
        assert type(num) == int and type(den) == int, "please put an interger"
        assert den != 0, "zero division error"
        self.num = num
        self.den = den
        
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self,other):
        top = self.num * other.den + other.num * self.den
        bottom = self.den * other.den
        
        
        #Simplify
        for i in range(1,bottom):
            if top % i == 0 and bottom % i == 0:
                top = top // i
                bottom = bottom // i
                
        return fraction(top,bottom)
    
    
a = fraction(10,5)
b = fraction(12,5)
c = fraction(5,3)
print(a)
print(a+b)
print(a+c)

#I could rewrite by tic tack toe game using classes to make it way nicer
