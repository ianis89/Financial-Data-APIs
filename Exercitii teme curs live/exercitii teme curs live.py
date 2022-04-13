def create_list(x, y, z, w, t):
    # ex 1  write code that creates a list with the input params of the function
#Rezolvare
   lista = [x,y,z,w,t] #creare lista
   return lista
a = create_list(1,2,3,4,5) #apelare functie cu parametrii
print(a)

# ex2  #the function should return a bool
#     # it should check the condition from the functions name
def is_smaller_than_1_and_is_positive(a):
    #the function should return a bool
    # it should check the condition from the functions name
# Rezolvare
    return a < 1 and a >= 0 # returnare directa  conditie din functie va returna true or false bool

#ex3 # a password can be considered decent if it has at least 8 characters, so goes for the rest
    #write code that will return the strenght of the variable 'password'
def compute_password_strength(password):
    strengths = {"weak": 0, "decent": 8, "good": 16, "strong": 32}
    # a password can be considered decent if it has at least 8 characters, so goes for the rest
    #write code that will return the strenght of the variable 'password'
    pass

    s = {"weak": 0, "decent": 8, "good": 16, "strong": 32}
    length = len(password)
    if length < s["decent"]:
        return "weak"
    if length < s["good"]:
        return "decent"
    if length < s["strong"]:
        return "good"
    return "strong"

print(compute_password_strength("2222222222222222222222222222232d232d2333333333333333"))

#ex4 # create a sentence on this line using the 3 names from the tuple

example_of_tuple = ("Horea", "Closca", "Crisan")
# create a sentence on this line using the 3 names from the tuple
text  = example_of_tuple [0]  + "," + example_of_tuple[1] + "&" + example_of_tuple[2]  #unirea elementelor din tuple

 # ex 5
# #receives a variable 'email' which is a string, checks if there is only one char '@' and after it only 1 '.'
    #returns bool
def is_email(email):

    pass
    arond_index = email.find("@") #cautare caracter
    # if we do not find any @, we exit with false (daca nu gasim nici un @ iesim cu false)
    if not arond_index > 0:
        return False
    # if we find an @, we check that there is a point after it and no @ (daca gasim @ verificam daca e un punct dupa si no @)
    # we do +1 so we ommit the first @
    point_index = email[arond_index+1:].find(".")
    arond_index2 = email[arond_index+1:].find("@")
    return point_index > 0 and arond_index2 == -1



print(is_email("roberto@itschool"))
print(is_email("roberto@itschool.ro"))



if is_email("roberto.judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto@judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")
else:
    print("evaluare gresita")

if not is_email("roberto.judet@itschool"):
    print("Daca se printeaza asta, functia a evaluat corect")

#ex 6  receives 2 params 'm' & 'n'
    # one is a float, the other int, we do not know which one
    # check the following 2 condtions: the int is bigger than 10, the float has after the point a value smaller than 0.5
    # if one condtion is True, return True from the function

def check_int_bigger_than_10_float_smaller_than_0_point_5(m, n):

    pass

    #Rezolvare

    # first we check if one of them is int and bigger than 10

    if bigger_than_10(m) or bigger_than_10(n):
        return True
    # second we check if one is float and smaller than 0.5
    elif type(m) == float and m <= 0.5 and m > 0 or type(n) == float and n <= 0.5 and n > 0:
        return True
    else:
        return False

def bigger_than_10(a):

    return  type(a) == int and a > 10
print (bigger_than_10(11))



#ex 7 # check that the variable `number` is divisible by `divisor`
    # return True or False
 def is_divisible(number, divisor):
    return number % divisor == 0

print(is_divisible(7,3))
print(is_divisible(100,10))

#ex 8 create a function which receives a number
# if the number is odd (impar) multiply by 3, if not divide it by 2

#rezolvare

def ex2(nr):
    if nr % 2 == 0:
        return nr // 2
    else:
        return nr * 3

def number(x):
    if x % 2: # if 0 -> False, if 1 -> True
        print(x * 3)
    else:
        print(x // 2)

print(number(4))
print(number(5))

#EX 9
# write a for to say(print) hello to all names

def say_hello_to_all(list_of_names):
    # write a for to say(print) hello to all names

    for name in list_of_names:
        print(name)


names = ["Bob", "Jane", "Bill", "George", "Ryan"]

print(say_hello_to_all(names))

#EX 10 # print only the odd numbers from the list (numerele impare)
def print_only_odd_numbers(list_of_numbers):
    # print only the odd numbers from the list (numerele impare)
    pass
    for nr in list_of_numbers:
        if nr % 2 != 0:
            print(nr)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_only_odd_numbers(numbers)

#EX 11 # return a new list with only the even numbers
    # example of code to add element to the end of a list
    #   lista.append(4)
def return_even_numbers(list_of_numbers):
    # return a new list with only the even numbers
    # example of code to add element to the end of a list
    #   lista.append(4)
    pass


even_numbers = return_even_numbers(numbers)
print(even_numbers)
    #Rezolvare
    lista = [] # create a new empty list
    for nr in list_of_numbers:
        if nr % 2 == 0: # check nr is divisible by 2, rest equals 0
            lista.append(nr)
    return lista

 #ex 12 #create a function which returns the number of elements in a list
def count_list(lista):
    length = 0
    for element in lista:
        length = length + 1
    print(length)

my_list = [22, 89, 12, 0, 28, 15]


# print("Number of elements in the list: ", get_number_of_elements(my_list))

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count_list(x)
print (len(x))


# ex 13
# create a function which multiplies all the numbers in the list

list_to_try = ["hello", 2, 1, -4, "alt string", True]
def multiply(lista):
    result = 1
    for el in lista:
        if type(el) == int or type(el) == float:
            result = result * el
    return result

print(multiply(list_to_try))


#Ex 14
# create a function which creates a text with all the strings from the list

def create_sentence(lista):
    sentence = ""
    for el in lista:
        if type(el) == str:
            sentence = sentence + el + " "
    print(sentence)

lista8 = ["hey", 1, False, "there", "do", 0, "you", -0.9, "know", "the", "clock", 77, 88.9]
create_sentence(lista8)

#Ex15 #15# create a function which returns the maximum and minimum number from a list
def min_and_max(lista):
    min = lista[0]
    max = lista[0]
    for el in lista:
        if min > el:
            min = el
        if max < el:
            max = el
    return (min, max)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min_and_max(numbers))

#EX 16
# write a function which returns a dict containg the 2nd largest number & 2nd smallest number
def min_and_max(lista):
    min1 = lista[0] # the smallest one
    min2 = lista[0] # the 2nd smallest one
    max1 = lista[0] # the biggest one
    max2 = lista[0] # the 2nd biggest one
    for el in lista:
        if min1 > el:
            min1 = el
        if max1 < el:
            max1 = el
    # until now, the function determines the maximum and minimum
    for el in lista:
        if el > min1 and el < min2:
            min2 = el
        if el < max1 and el > max2:
            max2 = el
    return (min2, max2)
list2 = [1, -2, 3, -4, 10, 8, 99, -23, 55, 100, -0.6, 27.6]
print(min_and_max(list2))

#Exercitiu 17 Difficult
# write code that returns a list of ordered numbers (0, 1, 2, 3, ...)


def return_an_ordered_list(numbers):
    index1 = 0
    index2 = 0
    for el1 in numbers:
        for el2 in numbers:
            if index1 < index2 and numbers[index1] > numbers[index2]:
                aux = numbers[index2] # we save one of the numbers in a variable
                numbers[index2] = numbers[index1]
                numbers[index1] = aux # aux is the initial value of numbers[index2]
            index2 = index2 + 1
        index1 = index1 + 1
        index2 = 0
    return numbers

numbers = [0, -4, 56, 7.0, 89, 203.45, 0.45, -0.3, 5, 8]
ordered_numbers = return_an_ordered_list(numbers)

#Ex 18

# create a function which removes duplicate items from a list

list_with_duplicates = [1, 1, 2, 3, 3, 2, 5, 6, 7, "a", 5, 2]
list_without = [1, 2, 3, 5, 6, 7, "a"]


def is_in_list(element, lista):
    for el in lista:
        if el == element:
            return True  # when we find the first element, we exit and return True
    return False  # means we did not find the element


def remove_duplicates(lista):
    new_list = []
    for el in lista:
        if el in new_list:
            pass
        else:
            new_list.append(el)
    return new_list

if remove_duplicates(list_with_duplicates) == list_without:
    print("we removed the duplicates")
else:
    print("we did NOT remove")

#ex 19   # write a function which returns a list without the empty strings (do not use remove function for this exercise)
list1 = ["Michael", "", "Ellie", "Ken", "", "Gunter"]
# write a function which returns a list without the empty strings (do not use remove function for this exercise)
def without(lista):
    new_list = []
    for el in list1:
        if el != "":
            new_list.append(el)
    return new_list

print(without(list1))

#EX20
# write a function which counts every element and returns a dict {"a": 3, "b": ...
def count_el(lista):
    d = {}
    for el in lista:
        if el in d: #check a key is in dictionary
            d[el] = d[el] + 1
        else:
            d[el] = 1
    return d
#EX 21 INPUt Exercitii
# take 2 numbers from the user
# print the sum back

def input_sum():

    num1 = input("Enter first number: ")  # ask for the first number, num1 equals user's input

    num2 = input("Enter second number: ")
    sum = float(num1) + float(num2)  # we have to convert the user's input from string to float

    print("The sum is " + str(sum))

#EX22

# take 3 numbers from the user
# print the biggest one

numbers = input("Type the numbers separated by space: ")

 lista = numbers.split(" ")  # split function returns a list of substrings

 lista_int = [float(x) for x in lista]  # this will do append for the code before `for`

  lista_int = [] # create an empty list to put the number values
 for x in lista:

     lista_int.append(float(x)) # add every string from lista after we transform it

 print(lista_int)
 biggest_number = max(lista_int)  # provide the list of the numbers to max function, will return the biggest number

 print("Biggest number = " + str(biggest_number))

#ex23
#Ask the user's name
# ask him his age
# print if he is allowed to drink

name = input("What is your name? ")
 age = int(input("What is your age?"))
if age >= 18:
    print(name + " is allowed")
 else:
    print(name + " is not allowed")

#EX 24

#ask the user for at least 5 words
#put them in a sentence

sentence = ""
 for x in range(5):  # range(5) -> [0, 1, 2, 3, 4]
     sentence = sentence + " " + input("Type a word")
 print(sentence)

#Ex25
#create a guessing game, the user must tell a number between 0 and 9 and you must tell him if he guessed it
x = random.randint(0, 9)  # this will pick a random number between 0 and 9
# create a guessing game, the user must tell a number between 0 and 9 and you must tell him if he guessed it

tries = 0

max_tries = 3

user_nr = int(input("Guess a number between 0 and 9: "))  # ask the user for a number
while user_nr != x and tries <= max_tries:  # check if the user guessed the number, if not ask for another number
    tries = tries + 1
    user_nr = int(input("You were wrong! Try again: "))

if tries > max_tries:
    print("You lost! The number was " + str(x))
else:
    print("You guessed it!")

##########