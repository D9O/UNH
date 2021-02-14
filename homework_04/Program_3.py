'''
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
''' 

def Solve(testx):
  #This is my original brute force solution with a terrible Big O.  I didn't get hired.
  #
  #at = 0
  #for i in range(at, len(testx["list"])):
  #  if at + 1 > len(testx["list"]): return [-1, -1]
  #  for j in range(at+1, len(testx["list"])):
  #    if testx["list"][i] + testx["list"][j] == testx["target"]:
  #      return [i, j]
  #  at += 1

  #Read hint 2, made this.  Maybe I can get hired with a hint. Using the dict obj makes it
  #  harder to read.  -5 from Dr. Fischer, but it works in 5 lines!
  
  for t in range( 0, len(testx["list"]) ):
    try:
      return [t, testx["list"][(t+1):].index(testx["target"]-testx["list"][t]) + (t+1) ]
    except:
      continue

  #I didn't read hint 3, will wait for class.
      
if __name__ == "__main__":
  test1 = {'list': [4, 7, 11, 15, 21, -12], 'target': 3}
  test2 = {'list': [3,2,4], 'target': 6}
  print(Solve(test1))
  print()
  print(Solve(test2))