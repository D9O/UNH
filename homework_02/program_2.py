import sys  # I use this for sys.exit()

#get an answer to a yes or no question; return True for yes, and False for no
def Get_Answer(yesno_q):
  while 1:
    answer = str(input("{} (yes/no)? ".format(yesno_q)))
    if "yes" == answer.lower():
      return True
    elif "no" == answer.lower():
      return False

#recursive binary search that get to the answer
def Binary_Search(low, hi, counter):
  #print("I see range {}-{}".format(low, hi))
  if(low > hi):
    print("You're cheating!")
    return False
  counter += 1
  half = (hi + low) // 2
  if Get_Answer("Is the number {}".format(half)):
    print("Your secret number is {}".format(half))
    print("It took me {} guesses".format(counter))
    return True
  else:
    if Get_Answer("Is the number larger than {}".format(half)):
      Binary_Search(half+1, hi, counter)
    else:
      Binary_Search(low, half-1, counter)
  

if __name__=="__main__":
  
  try:
    player = input("Hi, what is your Name? ")
  except:
    sys.exit("Invalid entry; to play, please restart me and try again.")

  play = True
  while play:
    print("Hello {}! Let's play a game!".format(player))
    print("Think of a random number from 1 to 100, and I'll try to guess it!")
    Binary_Search(0, 100, 0):
    play = Get_Answer("Do you want to play again?")
  
  print("bye bye.")
    
    