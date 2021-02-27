import os
import sys
from time import sleep

def There_Is(path_str):
  if os.path.exists(path_str) == False:
    sys.exit(f"Alert: file >{path_str}< is not there.")
  return True
  
if __name__=="__main__":
  if len(sys.argv) < 2:
    sys.exit("usage: python3 program_01.py <path to watch file>")
  
  while There_Is(sys.argv[1]):
    sleep(1)
