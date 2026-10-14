def abcd():#defining the function abcd
    print("FF")
abcd() #we have to define a fn before using

def num(a,b):
   print(f"sum is {a+b:.2f}")

num(1.3,2.3)
num(8,9)
#return bring value back to the function
def sum(a,b):
   c=a+b
   return c
x=sum(1,2)
print("sum of two no ",x)


def sum(a,b):
    c=a+b
    return c

x=sum(10,20)
print("sum of two no ",x)

#add or subtract using function
def m1(a,b):
    c=a+b
    d=a-b
    return c,d
x,y=m1(10,5)
print("sum of two number ",x)
print("subtact of two number ",y)
print("subtact of two number ",y)


#assigning a variable to a function
def add():
    print("we assigned two variable")
sum= add
sum()
#bringing one function to anouther
def message(text):
    print(text)

def printmessage(x):
    x("Hello world")
printmessage(message)