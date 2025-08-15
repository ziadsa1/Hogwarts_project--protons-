c = 1
class MagicalContact:
    def __init__(self,name,email,phone):
        self.__name = name
        self.__phone = phone
        self.__email = email
    
    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone
    
    def set_email(self):
        self.__email = input("New Email: ")
        print("Changes Have Been Saved Successfully.")
    
    def set_phone_number(self):
        self.__phone = input("New Phone Number: ")
        print("Changes Have Been Saved Successfully.")
    
    def describe(self):
        print(f"{self.__name} - {self.__email} - {self.__phone}")


class Wizard(MagicalContact):
    def __init__(self, name, age, phone, house, wand):
        super().__init__(name, age, phone)

        houses = ['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']
        if (house.lower() in houses):
            self.__house = house
        else:
            raise ValueError("Invalid house")
        
        self.__wand = wand

    def get_wand(self):
        return self.__wand

    def get_house(self):
        return self.__house
    
    def describe(self):
        print("Wizard Contact")
        print("=================")
        print(f"Name: {self.get_name()}")
        print(f"Phone Number: {self.get_phone_number()}")
        print(f"Email: {self.get_email()}")
        print(f"Wand: {self.__wand['core']} , {self.__wand['wood']} , {self.__wand['length']}")
        print(f"House: {self.get_house()}")


class Magical_Creature(MagicalContact):
    def __init__(self, name, age, phone,species,is_tame):
        super().__init__(name, age, phone)
        self.__species = species
        self.__is_tame = is_tame #bool
    
    def get_species(self):
        return self.__species

    def get_is_tame(self):
        return self.__is_tame
    
    def describe(self):
        print("Magical Creature Contact")
        print("===========================")
        print(f"Name: {self.get_name()}")
        print(f"Phone Number: {self.get_phone_number()}")
        print(f"Email: {self.get_email()}")
        print(f"Creature Type: {self.get_species()}")
        if self.get_is_tame():
            print("Yes, it is tame!")
        else: print("No, it isn't tame.")
        
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


