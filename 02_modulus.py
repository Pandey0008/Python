def mod(a,b):
    if b<=0:
     return -1
    div =  a // b
    return a - div*b
a=int(input("Enter a: "))
b=int(input("Enter b: "))
if a >=b:
 print("Modulus of" , a , "and" , b  ,"is" , mod (a,b))
else:
 print(a , "is less than" , b , "please enter a valid number")