
# A simple loop through all the items, looking for a specifically item amoung all the items. InThis case, we are looping through test and seeing if it matchs the word 'nemo'. For each item thar correponds with the word nemo, our function will print the sentence "Found nemo".

# The Big O notation of this function is O(n) (Big o of n or Linear time), because we just have to loop once each item and check whether our item is or is not the item we serching for.

# O(n) is a fair function in the Big-O Complexity Chart
from datetime import datetime


test = ['nemo' for i in range(0,10000)]

def findNemo(nemo):
  inicial = datetime.now()
  for i in range(0,len(nemo)):
    if nemo[i] == 'nemo':
      print('Found Nemo')
  print(inicial)
  print(datetime.now())
  

findNemo(test)

