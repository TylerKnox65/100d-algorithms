#!python3

"""
Create a function that takes an integer value from 0-255 and
converts it into a list.  Each element is equal to the power
of 2 that corresponds to that place value
"""

def toBinary(value):
  '''
  input: value (int)
  return : list of values
  '''
  '''
  This is another way to do the same thing, although more difficult then using Python's built in Bin() operator
  #bin_list = []
  #divide_int = value // 2
  #remainder = value % 2
  #bin_list.append(remainder)
  #x = bin(value)[2:]
  #x = '{0:08b}'.format(value)
  '''
  x = bin(value)[2:].zfill(8)
  x = list(x)
  x = [eval(i) for i in x]
  instances = [i for i, o in enumerate(x) if o == 0] #Instances checks the amount of times "0" appears in the list.
  
  instance_length = len(instances)
  if instance_length == 8: #Checks if the entire list is "0" and returns if true. (Sorting a list full of just 0 can lead to undesirable results)
    return x
  else:
    x.reverse()#When using Bin() the binary is stored in the reverse order.
    return x

def toDecimal(myList):
  '''
  input: list of values
  return int
  convert binary to decimal
  '''
  myList.reverse()

  s = ''.join(str(x) for x in myList) #finds and converts each int(x) to str(x) in list
  b = int(s, 2)#Converts the string into int after binary to int.

  return b

def problem1():
  assert toBinary(0) == [0,0,0,0,0,0,0,0]
  assert toBinary(1) == [1,0,0,0,0,0,0,0]
  assert toBinary(2) == [0,1,0,0,0,0,0,0]
  assert toBinary(5) == [1,0,1,0,0,0,0,0]
  assert toBinary(10) == [0,1,0,1,0,0,0,0]
  assert toBinary(30) == [0,1,1,1,1,0,0,0]
  assert toBinary(45) == [1,0,1,1,0,1,0,0]

def problem2():
  assert toDecimal([0,0,0,0,0,0,0,0]) == 0
  assert toDecimal([1,0,0,0,0,0,0,0]) == 1
  assert toDecimal([0,1,0,0,0,0,0,0]) == 2
  assert toDecimal([1,0,1,0,0,0,0,0]) == 5
  assert toDecimal([0,1,0,1,0,0,0,0]) == 10
  assert toDecimal([0,1,1,1,1,0,0,0]) == 30
  assert toDecimal([1,0,1,1,0,1,0,0]) == 45
  
if __name__ == "__main__":
  problem1()
  problem2()
