boxes = [1,2,3,4,5]

def logAllPairsOfArray(array):
  for i in boxes:
    for j in boxes:
      print(f'{i}, {j}')

# The Big O of this function is  O(n*n) so, O(n^2). It is called quadratic time.  