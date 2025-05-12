#Swapping User input
a=int(input('Enter number 1st to swap: '))
a_val=a
b=int(input('Enter number 2nd to swap: '))
c=int(input('Enter number 3rd to swap: '))
cval=c
swap_order=int(input('Swap:\n1.left to right\n2. or visa versa:\n '))
if swap_order==1:
    a=b
    b=c
    c=a_val
    print(b,a,c,'Final Output')
elif swap_order==2:
    c=a
    a=b
    b=cval
    
    print(c,a,b,'Final Output')
else:
    print('Enter valid input')
