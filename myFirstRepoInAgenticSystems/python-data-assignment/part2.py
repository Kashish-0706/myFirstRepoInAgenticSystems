# creating a contact book using dictionary
contact_book = {
    "Hania": "9887562438",
    "Ambika": "8765437899",
    "Shivansh": "7549876756",
    "Ayra": "9868954367",
    "ojas": "9888764565" 
}

print("All Contacts:", contact_book)
search_name = input("Enter the name to search:" )
if search_name in contact_book:
    print("Phone number:", contact_book[search_name])
else:
    print("Contact not found")