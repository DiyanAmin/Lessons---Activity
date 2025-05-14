#Checking if temperature is appropriate for wearing light clothes
print('Temperatures suitable for wearing light clothes:\n24 degrees celcius and above')
temp=int(input('Enter temperature in degrees celcius: '))
if temp>=24:
    print('Temperature is suitable for light clothes.')
else:
    print('Temperature is not suitable for light clothes')