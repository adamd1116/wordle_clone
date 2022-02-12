import os
import random
os.system('')

class colours:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

guesses = 6
WL = []
gameStarted = False
WordL = []
gWord = []
currGuess = []
c = False
b=0

def getword():
    
    with open('things.txt', 'r') as f:
        content = f.readlines()
        linenum = random.randint(0,210)
        
    word = content[linenum]
    return word.lower()
    

rWord = getword()

for i in range(len(rWord)):
	WL.append('_')

for i in rWord:
    WordL.append(i)    

WLconv = "".join(WL)

def startgame():
    print("\n1) You have 6 guesses.")
    print("2) Words must have 5 letters")
    print("3) If you guess a letter right, but it isn't in the right place\n   then it will be yellow, if you guess a correct letter and it is\n   in the same place then it will be green. if the letter is not in\n   the word it will remain grey")

startgame()
gameStarted=True

print(rWord)

if gameStarted==True:
    print("\n\tThe game has started")
    while guesses!=0:
        guesses-=1
        
        colourOfOutput = []
        
        if guesses==5:
            print("\n\tGuess below: ")
        
        while True:
            firstguess = input("\n\t")
            if len(firstguess)!=5:
                print("\n\tGuesses have to be 5 characters long, try again")
            else:
                break

        if firstguess == rWord.strip():
            print(f"\t{colours.fg.black+colours.bg.green+(rWord.strip())+colours.reset}")
            print("\n\tCorrect!")
            c=True
            break
        elif firstguess != rWord:
            for i in firstguess:
                gWord.append(i)
            
            for i in range(0,5):
                if gWord[i]in WordL:
                    if gWord[i]==WordL[i]:
                        colourOfOutput.append("g")
                    else:
                        colourOfOutput.append("o")
                else:
                    colourOfOutput.append("n")

        for i in range(0,5):
            if colourOfOutput[i]=="n"and b!=1:
                b = "".join(gWord)
                if i==0:
                    print(f"\t{b[i]}",end="")
                else:
                    print(f"{b[i]}",end="")
            elif colourOfOutput[i]=="g":
                b = "".join(gWord)
                if i==0:
                    print(f"\t{colours.bg.green+colours.fg.black+b[i]+colours.reset}",end="")
                else:
                    print(f"{colours.bg.green+colours.fg.black+b[i]+colours.reset}",end="")
            elif colourOfOutput[i]=="o":
                b = "".join(gWord)
                if i==0:
                    print(f"\t{colours.bg.orange+colours.fg.black+b[i]+colours.reset}",end="")
                else:
                    print(f"{colours.bg.orange+colours.fg.black+b[i]+colours.reset}",end="")
                
        print(f"\n\tGuesses left: {guesses}")
        gWord.clear()

if guesses==0 and c==False:
    print(f"\n\tBetter luck next time, the word was: {rWord}")