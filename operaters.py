#Finding Average
#There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?
t1=98
t2=94
t3=41
t4=96
t5=11
added=t1+t2+t3+t4+t5
print('Sum of all tree heights-',added)
average=added/5
print('Average height of tress-',average)
#Write a program to calculate the number of notes in the given amount?
amount=int(input('Enter Amount: '))
note_100=amount//100
note_50=(amount%100)//50
note_10=((amount%100)%50)//10
print('100 rupee note',note_100)
print('50 rupee note',note_50)
print('10 rupee note',note_10)
#Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?
print('Enter Marks for 4 subjects')
maths=int(input('maths: '))
science=int(input('science: '))
Hindi=int(input('Hindi: '))
English=int(input('English: '))
sum=maths+science+Hindi+English
percentage=(sum/400)*100
print('Percentage of Marks obtained in all 4 Subjects:\n',percentage)
