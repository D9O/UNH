# The code that looks like I copied it all came from here:
#        >>>https://cryptography.io/en/latest/fernet.html<<<
# The stuff I cribbed is at the bottom of this website.
# I started with your website (tutorialspoint.com), ran command pip install cryptography
# and ended up going to cryptography.io to learn more.
# I did, however, take what was there and make it my own, as you can see below

# I never understood what the heck decorators were, THANKS for teaching this!

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

salt = os.urandom(16) 
'''
The salt must be global in scope for this implementation to work.  Which is a huge con 
to this implementation.  Were the salt to get lost, or change, the correct password
still will not decrypt the data.  One option may be to get rid of the salt, but this 
would make the data less secure.  Another option would be to securely share the salt from
Alice, to Bob, so to speak.  Diffie-Hellman or RSA-keys could be used to share the salt.
'''
 
def Encrypt(func):
  def inner(m, k):
    f = Fernet(k)
    return f.encrypt(m)
  return inner

def Decrypt(func):
  def inner(m):
    attempts = 0
    while attempts < 3:
      k = Get_PW(True)
      f = Fernet(k)
      try:
        return f.decrypt(m)
      except:
        print("Incorrect password!")
        attempts += 1
    return("Now this data is lost forever...")
  return inner

@Encrypt  
def Alice(m, k):
  return(m)

@Decrypt
def Bob(m):
  return(s)

def Make_Key(pw):
  kdf = PBKDF2HMAC(
       algorithm=hashes.SHA256(),
       length=32,
       salt=salt,
       iterations=100000,)
  return(base64.urlsafe_b64encode(kdf.derive(pw)))
  
def Get_PW(create_new=False):
  if create_new:
    pw = input("Enter Password >")
    return Make_Key(pw.encode("ascii"))
  while 1:
    pw = input("Enter Password >")
    if pw == input("Enter Again >"):
      return Make_Key(pw.encode("ascii"))
    print("Passwords don't match, try again.")

def Get_Line():
  x = input("Enter string to encrypt >")
  return(x.encode("ascii"))

if __name__=="__main__":
  print("Welcome to Encryptinator 1999!")
  m = Alice(Get_Line(), Get_PW())
  print(f"I am sending this across interwebs:\n{m}")
  print("When it is recieved on the other end, it is decrypted...")
  print(f"into: {Bob(m)}")
  
'''
OUTPUT:
andyd@AndyDs-MBP homework_05 % python3 program_4.py
Welcome to Encryptinator 1999!
Enter string to encrypt >This is the string...
Enter Password >abc
Enter Again >abc
I am sending this across interwebs:
b'gAAAAABgMbb7Pf-1FIadROBzGt49Em8QaxqxgfwVb8UOHwe3ZAJhSv4IzPtkuc1DIV8BLx0PHyx5YsWhyqlbopsE27_RVH1WngPVNZugKZz5TtnlYVT57Mo='
When it is recieved on the other end, it is decrypted...
Enter Password >abc
into: b'This is the string...'

andyd@AndyDs-MBP homework_05 % python3 program_4.py
Welcome to Encryptinator 1999!
Enter string to encrypt >This string won't fare as well :(
Enter Password >abc
Enter Again >123
Passwords don't match, try again.
Enter Password >abc
Enter Again >abc
I am sending this across interwebs:
b'gAAAAABgMbd8G78gB7lk8d3pH28pw1b3jE7BSLsqqi19kqOhke47LWmAk9RZ-s6zBEd_AV3HyrPl-uAwHntSfU_8vMexl5EO8eQiPSta11EsSKj_GIiM1D04kOoN4jIYy3yf0PElqpxa'
When it is recieved on the other end, it is decrypted...
Enter Password >123
Incorrect password!
Enter Password >123
Incorrect password!
Enter Password >123
Incorrect password!
into: Now this data is lost forever...
'''