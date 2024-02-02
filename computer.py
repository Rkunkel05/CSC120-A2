from typing import Dict, Optional

class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # - Want to retain a description for each computer 
    # - Be able to keep track of the OS and update it
    # - Keep track of the memory and update it
    # - Keep track of the price and update it when the computer is refurbished 

    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                 processor_type: str,
                 hard_drive_capacity:str,
                 memory: int,
                 operating_system:str,
                 year_made:int,
                 price:int):
        pass
         # You'll remove this when you fill out your constructor

    # What methods will you need?