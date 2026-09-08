num=int(input("Enter a number:"))
if num<=1:
    print("Not a prime number")
else:
    for i in range (2,int(num**0.5)+1):
      if num%i==0:
        print("Not a prime number ")
    else:
        print("It is a prime number ")