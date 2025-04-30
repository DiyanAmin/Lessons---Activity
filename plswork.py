#Average
#Formula -> sum of all inputs divided by no. of inputs;
#input1=87 input2=96 input3=59 => add all inputs and dived by 3
#Ram has got 90 marks , Rijal has got 69 marks , Sam has got 74 marks , Shyam has got 80 marks. Find average amount of marks:
ram=90
rijal=69
sam=74
shyam=80
no_of_inputs=4
sum=ram+rijal+sam+shyam
print('Sum of all marks:\n',sum)
average_marks=sum/no_of_inputs
print('Average marks:\n',average_marks)
#Denominations
amount=int(input('Enter number: '))
note100=amount//100
note50=((amount%100)//50)
note10=((amount%100)%50)//10
#Percentage
p1=int(input('Enter Percenrtage: '))
p2=int(input('Enter Percenrtage: '))
p3=int(input('Enter Percenrtage: '))
p4=int(input('Enter Percenrtage: '))
p5=int(input('Enter Percenrtage: '))
added=p1+p2+p3+p4+p5
percentage=(added/500)*100
print('The percentage is:\n',percentage)