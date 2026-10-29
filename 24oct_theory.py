#lifetime of variable is the duration betweenits memory allocation and delocation
#scope is where variable memory is accessible in the programme

a =12
b=19
def m():
    print("a from function m():",a)
    print("b from the function m(): ",b)
def n():
    print("a from functiion n():",a)
    print("b from function n():",b)
m()
n()


#global and local variable having the same name in python together
a = 1
def m():
    a=2
    print(a)
    print(globals()["a"])
m()

def printdata(x):
    if x==11:
        return
    else:
        print(x) #forward tracking
        printdata(x+1)
printdata(1)
#reverse printing recurssive function
# reccursive function is that type of function which call itself
def printdata(x):
    if x==11:
        return
    else:
        
        printdata(x+1)
        print(x) #backward tracking
printdata(1)



