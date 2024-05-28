import csv

class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Phone:
    contacts = []

    @classmethod
    def load_contacts_from_csv(cls):
        with open('contacts.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls.contacts.append(PhoneContact(row['Name'], row['Phone']))

    @classmethod
    def search_contacts(cls, search_string):
        results = [contact for contact in cls.contacts if search_string.lower() in contact.name.lower()]
        if results:
            for contact in results:
                print(f"{contact.name} ({contact.phone})")
        else:
            print("No contacts found")

# Load contacts from CSV
Phone.load_contacts_from_csv()

# Search for a contact
while True:
    search_string = input("Enter a name to search for: ")
    if search_string == "":
        break
    Phone.search_contacts(search_string)