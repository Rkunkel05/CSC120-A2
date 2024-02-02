class Computer:
    # What attributes will it need?
    # Any computer is going to need these attributes - Somewhere to store the description, price, etc.
    # Calling constructor -> Take ingrediants from __init__ and put them in here
    description: str
    processor_type: str
    hard_drive_capacity: str
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # - Want to retain a description for each computer 
    # - Be able to keep track of the OS and update it
    # - Keep track of the memory and update it
    # - Keep track of the price and update it when the computer is refurbished 

    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                 processor_type: str,
                 hard_drive_capacity: str,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        # self.[blank] sort of groups it all together; i.e. here self.description is referring to the specific description that belogns to yourself
        self.description = description
        self.processor_type = processor_type
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price 
        
    # What methods will you need?
def main():
    my_computer = Computer("Macbook Air","Intel","250GB","16GB","Sierra","2019","$900")
    print(my_computer)

main()