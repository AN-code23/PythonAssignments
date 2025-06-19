#- Implement a phonebook using dictionary
# Hint : name will be a key and phone number will be the value

phonebook = {
    "John": "1234567890",
    "Alice": "9876543210",
    "Bob": "4561237890"
}

print(phonebook)


# To look up a phone number by name:
# name = "Alice"
# print(f"{name}'s phone number is:", phonebook.get(name, "Not found"))

#  To add a new contact:
# phonebook["Emma"] = "5555555555"
# print("Updated Phonebook:", phonebook)

# To remove a contact:
# del phonebook["Bob"]
# print("Phonebook after deletion:", phonebook)