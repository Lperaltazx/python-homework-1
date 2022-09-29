#Exercise #1
#Cube Number Test... Print out all cubed numbers up to the total value 1000, so if the cubed number is over 1000 break the loop.

cube = 1000
for i in range(1001):
    if i == 5:
        continue
    print(i)

    #Exercise #2
#Get first prime numbers up to 100

for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')

        #Exercise 3
#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = input("how old are you:")
afe = int(age)
if age >= 18:
	print('kid')
elif age <= 18 and age >= 65:
	print('Adult')
else:
	print('seniors')