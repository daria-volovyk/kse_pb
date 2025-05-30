def is_prime(n):
    s=0
    if(n>2):
        for i in range(1, (n//2)+1):
            if(n%i==0):
                s+=1
        if(s==1):
            print("True")
        else:
            print("False")
    else:
        print("False")
na=10
is_prime(na)