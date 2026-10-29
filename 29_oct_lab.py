# def sumofdigit(number): #recursive 
#     if number=="":
#         return 0
#     else:
#         return int(number[0])+sumofdigit(number[1:])
# print(sumofdigit("12345"))

# def sod(num):
#     pass
# print(sod(12345)) #q=num//10 r=num%10

# def sumofdigit(number): #recursive 
#     if number==0:
#         return 0
#     else:
#         return (number%10) +sumofdigit(number//10)
# print(sumofdigit(12345))
# def sum(x,n):
#     if n==0:
#         return 1
#     else:
#         return x*sum(x,n-1)
# print(sum(2,3))

# def sod(num,s):
#     if num==0:
#         return s
#     else:
#         return sod(num//10,s+(num%10))
# print(sod(12345,0))

#reversing
def strev(str,rev):
    if str=="":
        return rev
    else:
        return strev(str[1:],str[0]+rev)
print(strev("yes",""))
#to check pallidrome
def ispallidrome(str,end,start):
    if start==end:
        return False
    elif str[start]!=str[-(start+1)]:
        return False
    else:
        return ispallidrome(str,end,start+1)
print(ispallidrome("Raj",len("Raj"),0))