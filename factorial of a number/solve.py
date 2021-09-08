#For example factorial of 6 is 6*5*4*3*2*1 which is 720

def factorial(n):
    
    if n == 0 or n == 1:
        return 1 
    return n * factorial(n-1)
    
n = int(input("Ënter a no. to get the factorial\n"))      
f = factorial(n)
print(f)

