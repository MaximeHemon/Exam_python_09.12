from colorama import init 
init()
from colorama import Fore, Back, Style 

mot1={"c","a","s","t","o","r"}
mot2={"c","i","n","e","m","a"}
mot3={"c","i","t","r","o","n"}
mot4={"h","u","m","a","i","n"}
mot5={"a","s","p","e","c","t"}
mot6={"r","e","l","i","e","f"}
mot7={"v","a","l","e","u","r"}
mot8={"n","a","t","u","r","e"}
mot9={"h","u","m","e","u","r"}
mot10={"m","a","r","q","u","e"}

import random
def motafficher (mot1,mot2,mot3,mot4,mot5,mot6,mot7,mot8,mot9,mot10):
	from random import shuffle
	motafficher= [[i] for i in range(10)]
	shuffle(motafficher)
print (len(motafficher))
  #  for i in range (0,len(motafficher)):
  #  print random.shuffle(motafficher)
input()