print('Backroom: Calculations and INFO \033[31m[RARE FILE]')

ckey='info_view'
ckeyget=raw_input("\033[37m#type-\033[34minfo_view\033[37m  ")
if ckeyget==ckey:


 import sys,time,os

message = "\033[41m\033[30mWall calculation is 5 meters{primary wall}... Climb wall is 6 meters square prism... Next stage building height 1M kilometers long and endless... Long pipe to cursed waters is 30meters long... First stage folder is named [Beginning -B]... more level info's on file named 0 to End."

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char !="\n":
            time.sleep(0.1)
        else:
            time.sleep(1)
          

os.system("") #clear

typewriter(message)