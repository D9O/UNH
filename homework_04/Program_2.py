'''
Write a function count_frequency that takes a list of words as an argument, counts how many times each word appears in the list, and then returns this frequency listing as a Python dictionary
Sample function call and output:

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))
 
{'seven': 1, 'one': 2, 'eleven': 3, 'three': 2, 'two': 2}
''' 

from collections import Counter

def lazy_man(list_obj):
  return Counter(list_obj)

def count_frequency(list_obj):
  ks = set(list_obj)
  ret_val = {}
  for k in ks:
    ret_val[k] = list_obj.count(k)
  return ret_val
  
  
if __name__ == "__main__":
  mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]  
  print(count_frequency(mylist))
  print(lazy_man(mylist))