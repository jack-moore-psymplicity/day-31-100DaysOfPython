import pandas as pd
from random import shuffle
data = pd.read_csv('data/spanish_words.csv')

to_learn = data.to_dict(orient = 'records')
current_card = pd.choice(to_learn['Spanish'])
print(current_card)

# import random
#
# def myfunction():
#   return 0.1
#
# mylist = ["apple", "banana", "cherry"]
# shuffle(mylist)
#
# print(mylist)