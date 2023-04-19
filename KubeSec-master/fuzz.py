#Fuzzing Python Methods
from scanner import isValidKey
import constants

def fuzz():
   key = ['crt', 'key']
   if any(key):
      print("This is legit key!")
   else:
      print("This is not legit key.")
   
def test():
   res = 'crt'
   print(res)
   
   res = '1234'
   print(res)
   
   res = constants.LEGIT_KEY_NAMES
   print(res)

   res = constants.FORBIDDEN_USER_NAMES
   print(res)

   res = None
   print(res)

def simplefuzz():
   fuzz()
   test()
	
if __name__=='__main__':
   simplefuzz()