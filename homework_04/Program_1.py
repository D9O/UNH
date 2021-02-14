'''
program 1:
Write a function that converts temperature from Fahrenheit to Celsius using formula
Tc=(5/9)*(Tf-32) 
To test your answer, 68F = 20C
''' 

def Far2Cel(degF):
  return (5.0/9)*(degF-32) 
  
if __name__ == "__main__":
  print(f"0 deg F is {Far2Cel(0):.2f} deg C")
  print(f"32 deg F is {Far2Cel(32):.2f} deg C.  b/c 'mericuh")
  print(f"50 deg F is {Far2Cel(50):.2f} deg C")
  print(f"100 deg F is {Far2Cel(100):.2f} deg C")    
     