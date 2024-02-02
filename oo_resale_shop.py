from typing import Dict, Optional

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