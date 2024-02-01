from typing import Dict, Optional

class Computer:

    # What attributes will it need?
    description:str
    operating_system:str
    memory:int
    price:int

    def refurbish(self, inventory, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
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

    # How will you set up your constructor?
    # - Want to retain a description for each computer 
    # - Be able to keep track of the OS and update it
    # - Keep track of the memory and update it
    # - Keep track of the price and update it when the computer is refurbished 

    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory):
        self.inventory = inventory
         # You'll remove this when you fill out your constructor

    # What methods will you need?