#Program 4:

#Use decorator function you created for the previous homework and estimate how much 
#operation on a dictionary is faster(or slower) than operation on a shelve

import time
import shelve
import json
import pprint

def timer(func, *args):
  def inner(*args):
    t = time.time()
    #z = func(*args)
    t -= time.time()
    #print(f"elapsed time = {-1*t}")
    return(-1*t)
  return inner

@timer    
def add_kv_dic(dic, key, val):
  if key not in dic.keys():
    dic[key] = [val]
  else:
    dic[key].append(val)

@timer
def add_kv_dic_shelve(shelve_loc, key, val):
  sh = shelve.open(shelve_loc)
  if key not in sh.dict.keys():
    sh[item['key']] = [item['val']]
  else:
    sh[item['key']].append([item['val']])
  sh.close()
  

if __name__=="__main__":
  with open("quotes.json", "r") as quotes_file:
    data = json.load(quotes_file)
  new_dic = {}
  sh = shelve.open("my_items")
  sh.close()
  
  elapsed_t = 0
  for node in data:
    elapsed_t += add_kv_dic(new_dic, node['author'], node['text'])
  print(f"time to update a dictionary= {elapsed_t} sec")
  
  elapsed_t = 0
  for node in data:
    elapsed_t += add_kv_dic_shelve(new_dic, node['author'], node['text'])
  print(f"time to update a dictionary= {elapsed_t} sec")


'''
OUTPUT:
andyd@AndyDs-MBP homework_06 % python3 program_04.py
time to update a dictionary= 0.00021195411682128906 sec
time to update a dictionary= 0.0002484321594238281 sec

!!!sometimes, shelf was faster ?!?

explanation:  [1] I have an SSD.  
              [2] My dir I'm running from is in the could (icloud), so maybe OSX puts 
                  as much icloud stuff as it can into RAM.
                  
////////MOVING FILES TO LOCAL HDD AND RERUNNING:
OUTPUT:
time to update a dictionary= 0.0001685619354248047 sec
time to update a dictionary= 0.00017642974853515625 sec

This still seems too wrong, but I can't find an error.
FWIW, OSX kernal has done strange things like this before in other classes.  E.g.
Algorithms and binary searches vs other searches...sometimes, somehow, the timing
one would expect is not what I get when I run the code in Python.  I dunno.  Perhaps
on Centos or something like that, it would be different.  Unless, of course, shelve is
supposed to be close to as fast as a normal dictionary.  Maybe if the file sizes were
super big, it would show up better.  In C++, which sucks to program in, strange things
happen less often.  But so do errors that take hours to fix.
'''