n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n//2):
        if(n%i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
______________________________________
Enter a number:6
6 is not a prime number

[Program finished]
