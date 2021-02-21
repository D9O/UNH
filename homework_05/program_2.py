import program_1 as p1

def bunnyEars2(numBuns):
  if numBuns == 0:
    return(0)
  if numBuns%2 == 0:
    return bunnyEars2(numBuns-1) + 2
  else: 
    return bunnyEars2(numBuns-1) + 3
  
if __name__=="__main__":
  for i in p1.my_range(0,5):
    print(f"{i} -> {bunnyEars2(i)}")


'''
OUTPUT:
andyd@AndyDs-MBP homework_05 % python3 program_2.py
0 -> 0
1 -> 3
2 -> 5
3 -> 8
4 -> 10
'''