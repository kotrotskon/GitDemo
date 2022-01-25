#Random list with functions:

import random

def list_sum(mylist):
    print("\n>Sum of list elements = ", sum(mylist))
    
def list_highest_lowest(mylist):
    print("\n>Lowest of list elements = ", min(mylist))
    print("\n>Highest of list elements = ", max(mylist))
    
def create_rand_list(user_int):
    randomlist = []
    for i in range(len(randomlist)):
        randomlist[i] = int(randomlist[i])

    for j in range(user_int):
        n = random.randint(1,101)
        randomlist.append(n)
    return randomlist

user_input = int(input('>Enter amount of elements to be added to list: '))

randlist=create_rand_list(user_input)
print("\n>Random list elements: {}".format(randlist))
list_sum(randlist)
list_highest_lowest(randlist)