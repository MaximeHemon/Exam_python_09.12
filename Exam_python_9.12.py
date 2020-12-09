import random
from colorama import init 
init()
from colorama import Fore, Back, Style 


mot1={"c","a","s","t","o","r"}
mot2={"c","i","n","e","m","a"}
mot3={"c","i","t","r","o","n"}
mot4={"l","e","t","t","r","e"}
mot5={"i","n","d","i","c","e"}
mot6={"r","e","l","i","e","f"}

def motrandom (mot1,mot2,mot3,mot4,mot5,mot6)



print(Fore.RED + 'some red text', end=" ") 
print(Back.GREEN + 'and with a green background') 
print(Style.DIM + 'and in dim text') 
print(Style.RESET_ALL) 
print('back to normal now') 
input()