#Program 3 
#Prompt user to enter a start path and file name, search recursively for the given file 
#name starting at the given path, when file is found, display the full path to the file. 

import os
import sys
import pprint

def File_Search(dpath, fstr):
  ret_val = []
  for root, dlist, flist in os.walk(sys.argv[1]):
    if fstr in flist:
      ret_val += [os.path.abspath(os.path.join(root, fn)) for fn in flist if os.path.basename(fn) == fstr] 
  return ret_val


if __name__=="__main__":
  if len(sys.argv) < 3:
    sys.exit("usage: python3 <start path> <filename to search for>")
  
  srch_dir = os.path.dirname(sys.argv[1])
  srch_fn = os.path.basename(sys.argv[2]) #gets rid of excess 'stuff'
  if os.path.exists(srch_dir) == False:
    sys.exit(f"Directory >{srch_dir}< does not exist.")
  
  r = File_Search(srch_dir, srch_fn)
  
  if len(r) != 0: 
    for fp in r:
      print(fp)
  else: 
    print(f"{srch_fn} not found in {srch_dir}")
  
'''
OUTPUT:
andyd@AndyDs-MBP homework_06 % python3 program_03.py quotes_output/ Ziggy_1.txt
blah-blah/2021_Spring/PYTHON/GITHUB/homework_06/quotes_output/Ziggy/Ziggy_1.txt
blah-blah/2021_Spring/PYTHON/GITHUB/homework_06/quotes_output/Ziggy/TEST/Ziggy_1.txt

andyd@AndyDs-MBP homework_06 % python3 program_03.py quotes_output/ Ziggy_5.txt
Ziggy_5.txt not found in quotes_output
'''