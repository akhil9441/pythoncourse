#KEY WORDS
"""
def function(*args):
    return(args)
yx=function(1,3,4)
print(yx)#1,3,4

def function(*args):
    return(args)
dd=function(9,9,8)
print(dd)#9,9,8


def function(x,y):
    return(x+y)
mm=function(50,45)
print(mm)#95

def function(x,y):
    return(x-y)
ss=function(85,40)
print(ss)#45



def function(x,y):
    return(x*y)
mi=function(50,6)
print(mi)#300

def  func_akhileswar(x,y):
    return(x+y)
mi=func_akhileswar(100,65)
print(mi)#165

"""


#GENERATORS
"""
def function(*args):
    for x in args:
        return x*x#25

csk= function(5,6,7,8)
print(csk)




def function(*args):
    for x in args:
        yield x/x

rr= function(4,3,9,4)
print(list(rr))#[1.0, 1.0, 1.0, 1.0]



def function(*args):
    for x in args:
        return x*x

rcb= function(45,64,56,67)
print(rcb)#2025


def functionn(*args):
    for x in args:
        return x*x

kkr= function(7,8,3,74)
print(kkr)#49


def function(*args):
    for x in args:
        return x/x

xx= function(7,7,3,2,)
print(xx)#1.0



def function(*args):
    for x in args:
        yield x*x

xy= function(2,4,6,8)
print(list(xy))#[4, 16, 36, 64]
"""


#LAMBDA

"""
pspk= lambda x,y:x+y
print(pspk("akhil","nikhil"))#akhilnikhil


def function (*args):
    return sum(args)
x=function(10,20)
print(x)#30

def function (*args):
    return sum(args)
x = function(6,9,0,7)
print(x)#22


def akhil_eswar(*args):
    return sum(args)
csk= akhil_eswar(7,3,2,4)
print(csk)#16

zz= lambda x,y:x+y
print(zz("rohit","sharma"))#rohitsharma


"""
#ITERATIONS
"""
x= set(range(7))
y= iter(x)
print(set(y))#{0, 1, 2, 3, 4, 5, 6}



x=  set(range(10))
y=  iter(x)

print(next(y))#0
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))#7



m= tuple(range(5))
z= iter(m)

print(tuple(z))#(0, 1, 2, 3, 4)

"""


#INNER FUNCTIONS OR NESTED FUNCTIONS
"""

def function_outer():
    return "python programming"

csk= function_outer()
print(csk)#python programming


def function_outer():
    def function_inner():
        return'akhil'
    yy=function_inner()
    return yy

xx=function_outer()
print(xx)


def function_outer():
    def function_inner():
        return"java script"
    xy=function_inner()
    return xy
yx=function_outer()
print(yx)
"""




















    
        

































































        
































































































