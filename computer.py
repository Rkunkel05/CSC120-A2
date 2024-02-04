"""
   Filename: computer.py
Description: OOP version of procedural_resale_shop.py that creates the class Computer, establishes 
its attributes, and holds a constructor that "assembles" various parts of the computer into their own 
object.
     Author: Rachel Kunkel
       Date: 4 February 2024  
"""

class Computer:
    # Attributes for computer
    description: str
    processor_type: str
    hard_drive_capacity: str
    memory: int
    operating_system: str
    year_made: int
    price: int

    # Constructor for class Computer
    def __init__(self, description: str,
                 processor_type: str,
                 hard_drive_capacity: str,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        # self.[blank] sort of groups it all together; e.x. here self.description is referring to the specific description that belongs to yourself
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price 

    
    
        