def fiboRecurr(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRecurr(n-1) + fiboRecurr(n-2)
        
        # if __name__ == "_main_":
num = int(input("Enter A number\n")) 
print(f"Using recurrsion vale of fib({num}) is {fiboRecurr(num)}")

