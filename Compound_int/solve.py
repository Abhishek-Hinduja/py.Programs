def compound_int(P,R,T):
    print("The principal amount is", P)
    print("The Rate of interest is ", R)
    print("The Time period is ", T)

    A = P * (pow((1+R/100),T))
    CI = A - P
    print("The Compound Interest is", CI)

f = compound_int(1000,10,2)
print(f)

