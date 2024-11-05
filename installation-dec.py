import os,sys,time
vi='\033[1;35m'
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

logo=f'''
{vi}┌──────────────────────────────────────────────────────────┐
│      _____ _   _  _____ _______       _      _           │
│     |_   _| \ | |/ ____|__   __|/\   | |    | |          │
│       | | |  \| | (___    | |  /  \  | |    | |          │
│       | | | . ` |\___ \   | | / /\ \ | |    | |          │
│      _| |_| |\  |____) |  | |/ ____ \| |____| |____      │
│     |_____|_| \_|_____/   |_/_/    \_\______|______|     │
│                                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘{S}
{O}═════════════════════════════════════
 {B}({V}√{B}) {O}Github     {R}=    {vi}Joker16
 {B}({V}√{B}) {O}Tool Name  {R}=    {vi}INSTALLATION
{O}═════════════════════════════════════'''
def menu():
  os.system('clear')
  print(logo)
  print(f"[1] ALL INSTALL PKG")
  print(f"[0] EXIT")
  print(f"{O}═════════════════════════════════════")
  sel=input(f"[?] Choice: ")
  if str(sel)=="1":
    base()
  elif str(sel)=="0":
    exit()
  else:
    print(f"DISO SAFIDY...AVERENO")
    time.sleep(2)
    menu()
def base():
  os.system('termux-setup-storage')
  os.system('apt upgrade -y')
  os.system('pkg install python2')
  os.system('pip install --upgrade pip')
  os.system('pip install requests')
  os.system('pip install mechanize')
  os.system('pip install lolcat')
  os.system('pkg install vget')
  os.system('pkg install php -y')
  os.system('pkg install nano -y')
  os.system('pkg install curl -y')
  os.system('pkg install tor  -y')
  os.system('pkg install openssh')
  os.system('pkg install bash')
  os.system('apt install python-dev -y')
  os.system('apt install ruby -y')
  os.system('apt install nmap -y')
  os.system('apt install clan -y')
  os.system('apt install jq -y')
  os.system('apt install macchanger -y')
  os.system('apt install tar -tar')
  os.system('apt install zip -y')
  os.system('apt install unzip -y')
  os.system('apt install bmon -y')
  os.system('apt instalL proot -y')
  os.system('apt install java -y')
  os.system('apt install figlet -y')
  os.system('clear')
  print(logo)
  print(f"{B}INSTALLATION DONE {V}√")
  input(f"{O}ENTER RETURN MENU")
  menu()
menu()