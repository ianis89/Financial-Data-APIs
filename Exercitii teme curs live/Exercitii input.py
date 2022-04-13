
import sys

print(sys.argv)

#exercitiu 1 /tema
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')


sum = int (num1) + int (num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

#exercitiu1 alta varianta  /tema
a=int(input("enter first number : "))

b=int(input("enter second number : "))

print("sum of",a, "and",b,"is",a+b)

#exercitiu2 /tema
num1 = 12
num2 = 14
num3 = 20

if (num1 >= num2) and (num1 >= num3):
    biggest = num1
elif (num2 >= num1) and (num2 >= num3):
    biggest = num2
else:
    biggest = num3
print ("The biggest number is " , biggest)

#exercitiu 3

name =  input ("Enter your name :")
age = int (input ("Enter your age :"))
print(name)
print ("Nice to meet you")
if age >= 18:
    print ("you are allowed to drink")


#exercitiu4
sentence = input("Type a sentence of at least 5 words")
words = sentence.split()
if len(words) < 6:
    print("You need to type more words!")


#exercitiu 5

import random
number = random.randint(0,9)

print("Try to guess  the number (between 0  and 9) in three guesses! ")

guess1 = int(input(" Enter you first guess:"))

if guess1 ==  number:
    print ("you guessed it on the first try!!! You must be good !!")
    sys.exit()
elif guess1 > number:
    print ("your guess is to high!")
else:
    print ("your guess is to low !")


guess2 = int (input(" Enter you second  guess:"))
if guess2 ==number:
    print ("you guessed on the second try! Nice job ")
    sys.exit()
elif guess2 > number:
    print ("your guess is to high!")
else:
    print ("your guess is to low !")

guess3 = int (input(" Enter you third  guess:"))
if guess3 ==number:
    print ("you guessed it! Great Job!!")
    sys.exit()
elif guess3 > number:
    print ("your guess is to high!")
else:
    print ("your guess is to low !")








