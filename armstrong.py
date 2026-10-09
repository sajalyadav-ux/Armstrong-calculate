def armstrong(n,digit):
    if n==0:
        return 0
    last_digit=n%10
    return pow(last_digit,digit)+armstrong(n//10,digit)
n=int(input("enter the value :"))
digit=len(str(n))
result=armstrong(n,digit)
if result==n:
    print("Armstrong number")
else:
    print("not armstrong number")
