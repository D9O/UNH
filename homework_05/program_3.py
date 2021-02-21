import time

def timer(func, *args):
  def inner(*args):
    t = time.time()
    z = func(*args)
    t -= time.time()
    return [f"elapsed time = {-1*t}", z]
  return inner

@timer    
def test_func1(a):
  c = a*a
  while a < c:
    a += 1

@timer
def test_func2(a, b):
  c = a*a
  while a < c:
    a += 1
    b = b / a

if __name__=="__main__":
  g = test_func1(3000)
  print(g)
  print(test_func1(3000))
  print(test_func2(3000, 3333333))
  
'''
OUTPUT:
andyd@AndyDs-MBP homework_05 % python3 program_3.py
elapsed time = 0.5111150741577148
elapsed time = 0.817237138748169
'''