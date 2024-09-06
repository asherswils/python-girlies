def happy_birthday(name):
    print("Happy Birthday to {name}!")
    print("You are old!")
    print()

happy_birthday("Tazmin")
happy_birthday("Tazmin")
happy_birthday("Tazmin")

def greet(name):
    print("Hello,"+name+"! How are you?")

greet("John")

def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)

def get_odd_numbers(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 1 == 0:
            odd_numbers.append(number)
            return odd_numbers
        
numbers = [1, 3, 5, 7, 9]
odd_numbers = get_odd_numbers(numbers)
print(odd_numbers)

name = input("what is your name?")
print("Hello" + name)

name = input("What is your name? ")
print("Hello, " + name)

age = int(input("Enter your age:"))
height = float(input("Enter your height in meters:"))
print("You are " + str(age) + "years old.")

#Add two numbers
a = 5
b = 3
sum = a + b
print("sum:", sum) #output:


