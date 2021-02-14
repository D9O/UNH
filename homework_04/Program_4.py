'''
1. uuid:  https://docs.python.org/3/library/uuid.html - This is nice python library which
generates random numbers using time and hardware for seeds.  It can output the number as 
bytes, an int, or in hex notation. 

***uuid4() is what I will use to create the URL shortner below.***

2. timestamp: https://realpython.com/python-time-module/#python-time-in-seconds-as-a-floating-point-number
This is a component of python's time library. It would genererate sequential values which 
could be used for URL shortening.  However, it is unavoidable that, at scale, the paterns 
underlying this method would create collisions faster than a method which uses more 
entropy (e.g. hashing or uuid above).

3. MD5 hash: https://www.geeksforgeeks.org/md5-hash-python/ - this is a broken hashing 
algorithm that is still used.  If combined with another hash value, the combination of 
the two hash values is still a good indication of uniqueness/authenticity.  It could be 
used to create unique URLs and the odds of a collision would be lower than using a time 
stamp, but I would try to prove this before adopting it as a method.

MY SOLUTION*******************************************************************************

Per RFC 3986, the safe characters	for a URL are:
  Alphanumerics 0-9 a-z A-Z
  Unreserved characters - . _ ~ (does not include blank space)
  
For ease of viewing/typing, this algorithm will not use the unreserved characters.  
Therefore, for each letter "slot" in a shortened URL:
  0-9 -> 10 permutations
  a-z -> 26 permutations
  A-Z -> 26 permutations
  ----------------------
  Total= 62 permutations per slot.
  
Per RFC 4343, Domain Name System (DNS) names are "case insensitive".  I am assuming we 
use a scheme such as www.shorty.com/1234567, where we control how to handle the 1234567
portion, and thus case sensitivity can be used.  Otherwise, subtract out one of the 26's
above and redo the math below.
  
The function for determining number of unique permutations per "slot" is
  Unique Short62^(slots)
  
  i.e. _ = 62^1 =      62 (one slot yields 62 permutations)
      __ = 62^2 =   3,844 (two yields 3,844, etc. etc.)
     ___ = 62^3 = 238,328
  and so forth.
  
Per https://www.internetlivestats.com/total-number-of-websites/, which is 100% 
accurate (jk), there are 1,836,634,607 at this instant.  To account for future growth
and other complexities, we will round this number up and add two zeros to the end.  
Therefore, we need to account for 200,000,000,000 permutations:
  62^x = 200,000,000,000 
  solving for x, we get:
  x ln 62 = ln 200,000,000,000
  x = ln 200,000,000,000 / ln 62
  x = 26 / 4
  x = 6.5 which we will round up to 7, as we can't have half a "slot".
Double check:
  62^7 = 3,521,614,606,208 is much > 200,000,000,000 so we are good to go.
  
With a seven-character URL, we will have ~3.5 trillion unique keys to map to. To make this
work and scale in real life, my idea is to randomize 4 slots, which requires a 
map of size 14,776,336 for URL=>short name and the same for short name=>URL.  When the
container fills up, roll over the 5th digit and create a new container.  Nevertheless,
the python code below will create a full 7-digit random short name for a URL.

''' 
import uuid
import pprint as pp

def Make_Char():
  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUBWXYZ0123456789"
  try:
    return chars[uuid.uuid4().int % 61]
  except:
    sys.exit("something went horribly wrong in Make_Char().")
  
if __name__ == "__main__":
  short_map = {}
  url_map = {}
  dirty_words = {"set", "of", "unacceptable", "words", "here"} #don't want to end up on
                                                               #reddit/fb with a bad word
  while True:
    url_inp = input("What is the URL ([q] to exit)? ").lower()
    if url_inp == "q":
      print("goodbye.")
      break
    if url_inp in url_map.keys():
      print(f"This URL is already mapped to {url_map[url_inp]}.")
    else:
      sh_url = ""  
      while True:
        for i in range(0, 7):
          sh_url += Make_Char()
        if sh_url in dirty_words:
          continue
        if sh_url in short_map.keys():
          continue
        break
      short_map[sh_url] = url_inp
      url_map[url_inp] = sh_url
      print(f"ENTERED shorty.com/{sh_url} <==> {url_inp}")
      pp.pprint(short_map)
      pp.pprint(url_map)

'''
EXAMPLE OUTPUT:
andyd@AndyDs-MacBook-Pro homework_04 % python3 Program_4.py
What is the URL ([q] to exit)? www.cnn.com
ENTERED shorty.com/ePW3Sxa <==> www.cnn.com
{'ePW3Sxa': 'www.cnn.com'}
{'www.cnn.com': 'ePW3Sxa'}
What is the URL ([q] to exit)? www.cnn.com
This URL is already mapped to ePW3Sxa.
What is the URL ([q] to exit)? www.abc.com
ENTERED shorty.com/0u0l98X <==> www.abc.com
{'0u0l98X': 'www.abc.com', 'ePW3Sxa': 'www.cnn.com'}
{'www.abc.com': '0u0l98X', 'www.cnn.com': 'ePW3Sxa'}
What is the URL ([q] to exit)? www.lemmyishardrock.com
ENTERED shorty.com/ySn5n75 <==> www.lemmyishardrock.com
{'0u0l98X': 'www.abc.com',
 'ePW3Sxa': 'www.cnn.com',
 'ySn5n75': 'www.lemmyishardrock.com'}
{'www.abc.com': '0u0l98X',
 'www.cnn.com': 'ePW3Sxa',
 'www.lemmyishardrock.com': 'ySn5n75'}
What is the URL ([q] to exit)? www.mango.com
ENTERED shorty.com/9eCzlJY <==> www.mango.com
{'0u0l98X': 'www.abc.com',
 '9eCzlJY': 'www.mango.com',
 'ePW3Sxa': 'www.cnn.com',
 'ySn5n75': 'www.lemmyishardrock.com'}
{'www.abc.com': '0u0l98X',
 'www.cnn.com': 'ePW3Sxa',
 'www.lemmyishardrock.com': 'ySn5n75',
 'www.mango.com': '9eCzlJY'}
What is the URL ([q] to exit)? q
goodbye.
'''    
     