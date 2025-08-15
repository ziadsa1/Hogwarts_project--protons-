from MagicalContact import MagicalContact
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
    