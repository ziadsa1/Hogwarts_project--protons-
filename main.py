from MagicalContact import MagicalContact
from MagicalcontactBook import MagicalContactBook
from MagicalCreature import Magical_Creature
from Wizard import Wizard

wand1 = {"core": "phoenix feather", "wood": "holly", "length": "11 inches"}
wizard = Wizard("Harry Potter", "HarryPoter@gmail.com", "1234", "Gryffindor", wand1)

creature = Magical_Creature("Buckbeak", "buckbeak@yahoo.com", "1111", "Hippogriff", True)

book = MagicalContactBook()
book.add_contact(wizard)
book.add_contact(creature)

book.list_contacts()

book.find_contact("Harry Potter")
book.find_contact("Hagrid")  