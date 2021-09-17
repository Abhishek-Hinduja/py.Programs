# // 153 = 1 + 125 + 27  True
def armstrong(n):

    # n = 153
    sum = 0
    order = len(str(n))
    copy_n = n
    while (n>0):
        digit = n%10
        sum+= digit**order
        n = n//10

    if (sum == copy_n):
        print("This is an Armstrong no.")
    else:
        print("This is not an Armstrong no.")
n = int(input("Enter a no. to calculate Armstrong\n"))

f = armstrong(n)
print(f)