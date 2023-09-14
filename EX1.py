# cook your dish here
t = int(input())
while t>0:
    n=int(input())
    if n%3==1:
        if (n-1)/3!=2:
            print(2,int((n-1)/3),int((n-1)/3),sep=" ")
        else:
            print(2,int((n/3)),int((n-1)/3),sep=" ")
    elif n%3==2:
        print(n//3,n//3,n-2*(n//3))
    t-=1
