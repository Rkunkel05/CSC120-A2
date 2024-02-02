class ResaleShop:

    # What attributes will it need?
    inventory = [] # computer objects will go in here
    
    # How will you set up your constructor?
        # - Multiple functions that work to alter the status of the inventory
        # - Continues list of all computer objects (inventory)
        # - Ability to buy computers to add to the inventory
        # - Ability to sell computers to add to the inventory
    
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,inventory):
        pass
         # You'll remove this when you fill out your constructor
    
    def buy(self, inventory, description: str,
                 processor_type: str,
                 hard_drive_capacity: str,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        self.description = description
        self.processor_type = processor_type
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price 
        # self.inventory.append?
        
    def sell():
        pass


def main():
    new_computer = ResaleShop({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2019, "price":1000})   

main()