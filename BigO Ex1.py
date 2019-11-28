#What is the Big O of the below function? (Hint, you may want to go line by line)

def funChallenge(input):
  a = 10 # O(1)
  a = 50 + 3 # O(1)

  for i in range(0,len(input)): # O(input)
    anotherFunction() # O(input)
    stranger = True # O(input)
    a+=1 # O(input)
  return a # O(1)

  # The Big O of this function is 3 + 4input or O(n)