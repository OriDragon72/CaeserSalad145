mgs = input("What is the message you want to decrypt? ")

matrix = list(range(1,25))

def decrypted(m, k):
  base = 97
  Dmgs = ""
  for char in m:
    Dchar = chr((ord(char) - base - k) % 26 + base)
    Dmgs += Dchar
  return Dmgs
  
for num in matrix:
  key = num
  print("["+ str(num) +"]" +decrypted(mgs, key)+ "\n")