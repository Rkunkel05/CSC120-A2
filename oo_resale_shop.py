from computer import Computer

class ResaleShop:
    # Attribute for class ResaleShop
    inventory = [] # computer objects will go in here

    
    # Constructor for class ResaleShop
    def __init__(self, inventory):
        self.inventory = inventory
    
    # "Buying" a computer, or adding it to the shop's list
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

    # "Selling" a computer, or removing it from the shop's list                      
    def sell(self,item_id):
        for computer in self.inventory:
            if id(computer) == item_id:
                self.inventory.remove(computer)
                description = computer.description
                print("Item", description, "sold! \n")
            else: 
                print("Item", description, "not found. Please select another item to sell \n")

    # Displays the shop's inventory
    def print_inventory(self):
        for computer in self.inventory:
            print(computer.description, computer.processor_type, computer.hard_drive_capacity,computer.memory,computer.operating_system,computer.year_made,computer.price)
        if self.inventory == []:
            print("No inventory to display.")

    # Depending on the computer's age, determines the price. Additionally will update the OS.
    def refurbish(self,item_id,new_os):
        for computer in self.inventory:
            if id(computer) == item_id:
                if int(computer.year_made) < 2000:
                    computer.price = 0 # too old to sell, donation only
                elif int(computer.year_made) < 2012:
                    computer.price = 250 # heavily-discounted price on machines 10+ years old
                elif int(computer.year_made) < 2018:
                    computer.price = 550 # discounted price on machines 4-to-10 year old machines
                else:
                    computer.price = 1000 # recent stuff

                if new_os is not None:
                    computer.operating_system = new_os # update details after installing new OS
            else:
                print("Item", item_id, "not found. Please select another item to refurbish.")


def main():
    # print banner
    print("-----------")
    print("Welcome to the Resale Store")
    print("----------- \n")

    # buy new computer
    new_computer = ResaleShop([]) 
    item_id = new_computer.buy(description = "2019 MacBook Pro",
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
    print("Done. \n")

    # refurbish computer
    new_os = "MacOS Monterey"
    print("Refurbishing", new_computer.inventory[0].description,"Updating OS to", new_os )
    print("Updating inventory...")
    new_computer.refurbish(item_id, new_os)
    print("Done. \n")

    # check inventory
    print("Checking inventory...")
    ResaleShop.print_inventory(new_computer)
    print("Done. \n")

    # sell item
    print("Selling Item ID:",new_computer.inventory[0].description)
    new_computer.sell(item_id)

    # check inventory
    print("Checking inventory...")
    ResaleShop.print_inventory(new_computer)
    print("Done. \n")


main()