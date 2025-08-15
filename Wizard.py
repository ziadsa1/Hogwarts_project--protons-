from MagicalContact import MagicalContact
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
        
