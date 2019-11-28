# O(1) or O of 1 or Constant Time is when we have an array of x elements, but we just take 1 single item in the array, no matter how many items there are in the array

# Example:

items = ['item' for i in range(0,10000)]

def grabber(array):
  print(array[0])

grabber(items)

# So, no matter how many items we add at the array, the function will always take the index 0 element, taking the same amout of time.

def logFirstTwoItems(array):
  print(array[0]) # O(1)
  print(array[1]) # O(1)

# O(1) is very scalable and in the Big-O Complexity Chart  it is rated as excelent just like O(log n)