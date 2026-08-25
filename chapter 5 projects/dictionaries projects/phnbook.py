phonebook = {}

print("Enter 5 contacts: ")
for i in range(5):
    name = input(f"Contact {i+1} name: ")
    phone = input(f"Enter phone number of {name}: ")
    phonebook[name] = phone

print("\nPhonebook:", phonebook)

search_name = input("\nEnter name to search phone number: ")

if search_name in phonebook:
    print(f"{search_name}'s number:", phonebook[search_name])

else:
    print(f"{search_name} not found in phonebook.")