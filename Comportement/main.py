#!/usr/bin/python
"""Main file used to run implementations of code"""

from random import randint
from canbotbehaviour import CanBot
from can import Can
from IGrabable import IGrabable
import time

def main():
    
    bot = CanBot()

    bot.start()

main()
