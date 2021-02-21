def my_range(beg, end, jmp=1):
  x = beg
  while x < end:
    yield x
    x += jmp
    
    
if __name__=="__main__":
  for i in my_range(0, 5):
    print(i)
  
  print("***")
    
  for i in my_range(0,5,2):
    print(i)
    
'''
OUTPUT:
andyd@AndyDs-MBP homework_05 % python3 program_1.py 
0
1
2
3
4
***
0
2
4
'''