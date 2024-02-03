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
        self.inventory = inventory
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
        return id(new_computer)
                            
        
    def sell():
        pass

    def print_inventory(self):
        for computer in self.inventory:
            print(computer.description, computer.processor_type, computer.hard_drive_capacity,computer.memory,computer.operating_system,computer.year_made,computer.price)

    def refurbish(self,inventory,item_id,new_os):
        for computer in self.inventory:
            if id(computer) == item_id:
                if int(computer["year_made"]) < 2000:
                    computer["price"] = 0 # too old to sell, donation only
                elif int(computer["year_made"]) < 2012:
                    computer["price"] = 250 # heavily-discounted price on machines 10+ years old
                elif int(computer["year_made"]) < 2018:
                    computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
                else:
                    computer["price"] = 1000 # recent stuff

                if new_os is not None:
                    computer["operating_system"] = new_os # update details after installing new OS
            else:
                print("Item", item_id, "not found. Please select another item to refurbish.")


def main():
    # print banner
    print("-----------")
    print("Welcome to the Resale Store")
    print("-----------")

    # buy new computer
    new_computer = ResaleShop([]) 
    computer_id =new_computer.buy(description = "2019 MacBook Pro",
        processor_type = "Intel",
        hard_drive_capacity = "256",
        memory = "16",
        operating_system = "High Sierra",
        year_made = "2019",
        price = "1000")
    print("Buying", new_computer.inventory[0].description)
    print("Adding to inventory...")
    print("Done.\n")

    # check inventory
    print("Checking inventory...")
    ResaleShop.print_inventory(new_computer)
    print("Done.")

    # refurbish computer
    new_os = "MacOS Monterey"
    print("Refurbishing", computer_id,"Updating OS to", new_os )
    print("Updating inventory...")
    ResaleShop.refurbish(computer_id, new_os)

main()