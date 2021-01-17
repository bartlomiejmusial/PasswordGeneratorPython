import random

# letters, numbers, symbols which will be used to generate the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_list = []
symbols_list = []
numbers_list = []

# adding different values to the list
for i in range(0, nr_letters):
    letters_list.append(letters[i])
for i in range(0, nr_symbols):
    symbols_list.append(symbols[i])
for i in range(0, nr_numbers):
    numbers_list.append(numbers[i])

#  combine all lists and mix them
list1 = letters_list + symbols_list + numbers_list
random.shuffle(list1)

password = ""

# concatenation of all list values into one string
for i in range(0, len(list1)):
    password += str(list1[i])

print(f"\nYour generated password is: {password}")
