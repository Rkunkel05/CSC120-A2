from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory = [] # computer objects will go in here
    
    # How will you set up your constructor?
        # - Multiple functions that work to alter the status of the inventory
        # - Continues list of all computer objects (inventory)
        # - Ability to buy computers to add to the inventory
        # - Ability to sell computers to add to the inventory
    
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        self.inventory = []
         # You'll remove this when you fill out your constructor
    
    # What methods will you need?
    # Doing operations on an already created object - Ex. Buying, selling, checking inventory 
    def buy(self, description,
                 processor_type,
                 hard_drive_capacity,
                 memory,
                 operating_system,
                 year_made,
                 price):
        new_computer = Computer(description,processor_type,hard_drive_capacity,memory,operating_system,year_made,price)
        self.inventory.append(new_computer)
                            
        
    def sell():
        pass

    def print_inventory(self):
        for computer in self.inventory:
            print(computer)


def main():
    print("-----------")
    print("Welcome to the Resale Store")
    print("-----------")
    new_computer = ResaleShop("new_computer") 
    new_computer.buy(description = "2019 MacBook Pro",
    processor_type = "Intel",
    hard_drive_capacity = "256",
    memory = "16",
    operating_system = "High Sierra",
    year_made = "2019",
    price = "1000")
    print("Buying", ResaleShop.inventory[0]["description"])
    print("Adding to inventory...")
    print("Done.\n")


main()