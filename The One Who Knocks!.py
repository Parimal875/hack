#Starting program
t=int(input())

for T in range(t):
    x,y=map(int,input().split())
    z=abs(x-y)
    if x>y :
        if z%2==0:
            print(1)
        else:
            print(2)
    elif x<y:
        if z%2!=0:
            print(1)
        elif z%4==0:
            print(3)
        else:
            print(2)
    elif x==y:
        print(0)
        
        
        
#End Program
