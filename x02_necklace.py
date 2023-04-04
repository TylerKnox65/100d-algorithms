#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, 
but if it's greater than 10, you add the sum of those 2 digits again.  
You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made? 

"""

def necklace(a,b):
  """
  inputs: 
  a : int value [0..9]
  b : int value [0..9]
  
  return
  str necklace number
  """
  num_list = [a, b]
  num_str = ""
  #num_str += str(a)
  #num_str += str(b)
  
  while True:
    next = (num_list[-1] + num_list[-2])
    if next > 9:
      next -= 9
    num_list.append(next)
    if num_list[0:2] == num_list[-2:]:
      break 
  num_str = "".join(str(x) for x in num_list)
  return num_str


      
  

def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()
  
  
