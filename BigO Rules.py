#Big O Rules

# Rules number 1: Worst Case

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