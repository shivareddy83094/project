### How to add new mobile numbers in the contact book?


## Calling the values of the  Phone numbers and the names.


names = []

phone_numbers = []


#Number of Phone numbers to be added in the list.


num = 10



# Taking the input from the user by using the for loop.


for i in range(num):
    
## Taking the name from the user.

    
    name = input("Name: ")
    
## Taking the phone number from user.
    
    phone_number = input("Phone Number: ")
    
## then adding the names to the list.
    
    names.append(name)

## and addimg the numbers to the list.     
    
    phone_numbers.append(phone_number)
    
    
    
print("\nName\t\t\tPhone Number\n")



for i in range(num):
    
    
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))
    
    
    
search_term = input("nEnter Search Term: ")


print("Search Result")


if search_term in names:
    
    
    index = names.index(search_term)
    
    
    
    phone_number = phone_numbers[index]
    
    ## then searching the name and number in the list.
    
    
    print("Name:{}, Phone Number: {}".format(search_term,phone_number))
    
   ## If the name is not found in the list.

else:
    
    
    print("Name not found")