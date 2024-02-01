from typing import Dict, Optional

class ResaleShop:

    # What attributes will it need?
    inventory = [] # computer objects will go in here

    def __init__(self, inventory):
        self.inventory = inventory 
    
    def inventory(self, inventory):
        self.inventory : Dict[int, Dict] = {}
        itemID = 0 # We'll increment this every time we add a new item 
           # so that we always have a new value for the itemID
        
    def buy(self, computer: Dict):
        global itemID
        itemID += 1 # increment itemID
        self.inventory[itemID] = computer
        return itemID
    
    def update_price(self, inventory, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(self, inventory, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self, inventory):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")
    
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