from random import seed
from random import getrandbits

# generate a 8 bits number
# https://stackoverflow.com/questions/22639587/random-seed-what-does-it-do

def random_number(num):
    seed(num)
    return  getrandbits(128)


