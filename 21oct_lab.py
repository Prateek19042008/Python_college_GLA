#fuction can be assigned to anouther function
def add(a,b):
    return a+b
def sub(a,b):
    return  a-b
def cal(func,a,b):
    return func(a,b)
print(cal(add,10,20))
print(cal(sub,10,20))

#function can be defined into anouther function
def outer_function():
    print("Tjis is outer function")
    def inner_fuction():
        print("This is inner function")
    inner_fuction()
outer_function()



#fuction can be return from anouther function
def outer_function():
    print("Tjis is outer function")
    def inner_fuction():
        print("This is inner function")
    return inner_fuction
func1=outer_function()
func1()


#list use in functions
l1=[add(80,90),10,20]
print(l1[0],(l1[1],l1[2]))


#keyword arguments
def details(name,age):
    print("name: ",name)
    print("age:",age)


details("Amit",25)#passing an positional argument
details(name="amit",age=25)#passing an keyword argument

#default  arguments
def details(name,age=18):
    print("name:",name)
    print("age:",age)
details(name="Amit")#passing only name,age will be defaultly set

#variable length arguments
def add(x,*y):
    print(type(y))
    sum = 0
    for i in y:
        sum+=i
        return sum+x

print(add(10,20))
print(add(10,20,30))

#keyword variable length variable
def details(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key," :",value)
details(name="amit",age=25,city="delhi") #error
details(a=10,b=20,c=30)
details(id=101,name="suraj",age=25)