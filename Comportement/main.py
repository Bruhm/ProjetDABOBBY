"""Main file used to run implementations of code"""

from random import randint
from codebot import CodeBot
from can import Can

def main():
    bot = CodeBot()
    cans = []
    for i in range(10):
        cans.append(Can(randint(400, 1000), randint(0, 360)))

    bot.cansInEnvironement = cans

    bot.start()

main()
