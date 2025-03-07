def factorial(n):
    if n==0 or n==1 :
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter num: "))
print(f"Factorial of {num} is {factorial(num)}")

def factorial(n):
    fact=1
    for i in range (1,n+1):
     fact*=i
    print(f"Factorial of {n} in {fact}")
n=int(input("Enter n: "))
factorial(n)
