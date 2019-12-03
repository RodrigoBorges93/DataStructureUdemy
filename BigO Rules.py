#Big O Rules

# Rule number 1: Worst Case

# You have to find whats the worst case and it will be your Big O Notation.

# Example: 
names = ['charlie', 'casey', 'nemo']
def findNemo(input):
  for i in input:
    print('Running function')
    if i == 'nemo':
      print('Found Nemo!')
      break

  # In this case, nemo is our 3rd item, but if it was the second element the loop would only have to go through the first 2 items. But, no matter whats the order, we have to find the worst case and put that as our Big O. So, in this case, the Big O is O(lenght of input) no matter the 'nemo' position in this input.


# Rule number 2: Remove Constants

def printFirstItemThanHalfThanSayHello100Times(item):
  print(item[0])

  middleIndex = len(item)/2

  for i in range (0,middleIndex):
    print(item[i])

  for i in range(0,100):
    print('Hi!')

# The Big O of this function is O(1+ n/2 + 100)
# So, by the rule number 2, we have to consider this function with a Big O of O(n)

#Just like the function above, by removing the constants, we'll have oct

def compressBoxesTwice(boxes, boxes2):
  for box in boxes:
    print(box)
  
  for box in boxes2:
    print(box)

# The result would be O(2n) but we have to remove the constants so we'd get O(n)


# Rule number 3: Different terms for inputs

def compressBoxesTwice(boxes):
  for box in boxes:
    print(box)
  
  for box in boxes:
    print(box)

# The Big O is O(a + b) because there are 2 differents groups of items, so we could probably have differente sizes