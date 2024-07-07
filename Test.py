import os,time,json,hashlib,requests,random,subprocess,platform
from bs4 import BeautifulSoup as bs

R='\033[1;91m'
V='\033[1;92m'
J='\033[1;33m'
C='\033[1;96m'
B='\033[1;97m'
Bl='\033[1;34m'
O='\033[38;5;208m'
S='\033[0m'
c='\033[7;96m'
r='\033[7;91m'
v='\033[7;92m'
ro='\033[1;41m'
co='\033[1;46m'



def key():
	global apr
	apr = requests.get("https://raw.githubusercontent.com/Lariot08/Test/blob/main/apr.txt").text
	sys_info=platform.uname()
	module=sys_info.version
	if module in apr:
		pass
	else:
		os.system("clear")
		print(f"{r}Vous n'avez pas l'approbation pour utiliser l'outil{S}")
		exit()
	print(f"{v}mety ilay izy{S}")
	time.sleep(4)
	exit()

key()