#Innner functions
"""

def outer_function(x,y):
    def inner_func(x,y):
        return x+y
    x = inner_func(x,y)
    return x

x=outer_function(4,6)
print(x)


def function_outer():
    def inner_function():
        return"pawan kalyan"
    xx= inner_function()
    return xx

xx= function_outer()
print(xx)



def function_outer():
    def inner_func():
        return "hey prabhu"
    dx= inner_func()
    return(dx)

dx= function_outer()
print(dx)#hey prabhu

"""
#DECORATORS

def akhil_leo(func):
    def inner_func(x,y):
        if x>y:
            kk = func(x,y)
            return kk
        return" naa anveshana"
    return inner_func



@akhil_leo
def func(x,y):
    return x*y
xy = func(7,8)
print(xy)




def bumrah_goat(func):
    def inner_func(a,r):
        if a<r:
            ll= func(a,r)
            return ll
        return "a is graeter than r"
    return inner_func


@bumrah_goat
def func_og(a,r):
    return a*r
aa = func_og(20,10)
print(aa)




def healius_emp(syed):
    def inner_func(x,y):
        if x<y:
            ag= syed(x,y)
            return ag
        return "kukkarasipalli"
    return inner_func



@healius_emp
def syed_firdos(x,y):
    return(x*y)
zz = syed_firdos(23,45)
print(zz)
