a=int(input("value 1="))
b=int(input("value 2="))
c=int(input("value 3="))

t=a+b+c
av=t/3

if av>a and av>b and av>c:
    print('av is greater than a,b,c')
else:    
    print('av is less than a,b,c')