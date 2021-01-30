def UnSnargle(s, ind):
  if len(s) != len(ind):
    return -1
  g = {}
  for i in range(0, len(ind)):
    g[ind[i]] = s[i]
  return "".join([ g[k] for k in sorted(g.keys()) ])

if __name__=="__main__":
  s = "codeleet"
  #          0 1 2 3 4 5 6 7
  #          c o d e l e e t
  indices = [4,5,6,7,0,2,1,3]
  print("{} => {}".format(s, UnSnargle(s, indices)))
  
  s = "aiohn"
  indices = [3,1,4,2,0]
  print("{} => {}".format(s, UnSnargle(s, indices)))
  
  s = "aaiougrt"
  indices = [4,0,2,6,7,3,1,5]
  print("{} => {}".format(s, UnSnargle(s, indices)))
  
  s = "art"
  indices = [1,0,2]
  print("{} => {}".format(s, UnSnargle(s, indices)))
  
  #no help from google, this is the best idea I could think up 
  
  #if we hadn't covered list comprehensions in this class, I would've had 3 - 4 more lines 
  #at line 7... 