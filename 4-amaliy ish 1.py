x=float(input('x ni kiriting:'))
n=int(input('n ni kiriting;'))
for i in range(0,n):
    if -1<x<1:
        print(x+((2*n-1)*(x**(2*n+1)))/((2*n)*(2*n+1)))
    else:
        print('x notogri oraliqda')


