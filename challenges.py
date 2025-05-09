#Membership Operators
#Checking if given input conyain 2nd in[ut
# thing1=input('Enter something: ')
# thing2=input('Enter something else: ')
# if thing1 in thing2:
#     print(thing1,'is in',thing2)
# elif thing2 in thing1:
#     print(thing2,'has something in',thing1)
# else:
#     print(thing1,'and', thing2,'do not contain similiar things')

#Indentify Operators
#Checking if input is same as 2nd input
l1='diyan'#input('Enter: ')
l2='diyan'#input('Enter something else: ')
g1=str(l1)
g2=str(l2)
print(g1 is g2)
print(type(g1),type(g2))
if g1 is g2:
    print(l1 ,'and', l2,'are same')
elif g2 is g1:
    print(g2 ,'and', g1,'are same')
else:
    print(g1 ,'and',g2,'are not the same')
