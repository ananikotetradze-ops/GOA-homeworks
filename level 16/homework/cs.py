#1
number = int(input("Enter a number: "))
if number >=90 and number <= 100:
    print("A")
elif number >= 80 and number < 89:
    print("B")
elif number >= 70 and number < 79:
    print("C")
elif number >= 60 and number < 69:
    print("D") 
elif number >= 0 and number < 59:
    print("F")


#2
number = int(input("Enter a number: "))
if number > 0:
    print("dadebiti")
elif number < 0: 
    print("uaryofiti")
else:    print("nuli")

#3
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
if first_number > second_number:
    print("First Number is Greater than second one")
elif first_number < second_number:
    print("Second Number is Greater than first one")   

#4
number = int(input("Enter a number: ")) 
if number % 2 == 0:
    print("luwi")
else:    print("kenti")

#5
number = int(input("Enter temperature: "))
if number < 0:
    print("cold")
elif number >= 0 and number < 30:
    print("normal") 
elif number >= 30:
    print("hot")
