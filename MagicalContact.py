class MagicalContact: #Origin
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


