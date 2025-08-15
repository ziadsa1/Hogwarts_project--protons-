class MagicalContactBook:
    def __init__(self):
        self.__contact_book = []

    def add_contact(self, contact):
        self.__contact_book.append(contact)
        print("Contact added successfully!")

    def list_contacts(self):
        if not self.__contact_book:
            print("No contacts in Magical Book!")
        else:
            for i, contact in enumerate(self.__contact_book, 1):
                print(f"\n{i}.")
                contact.describe()
        print('\n')

    def find_contact(self, name):
        for contact in self.__contact_book:
            if contact.get_name().lower() == name.lower():
                print('\n' * 2)
                print("============================")
                print("Contact Found!")
                print("============================")
                contact.describe()
                return
        print('\n' * 2)
        print("Contact not found.")


