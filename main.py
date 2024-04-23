import colorama
from colorama import Back, Fore, Style
from random import randint
from time import sleep

colorama.init(autoreset=True)

guesses = []
answers = []

style = Fore.WHITE + Style.DIM

styleDict = {
    "b" : Back.BLACK + style,
    "y" : Back.YELLOW + style,
    "g" : Back.GREEN + style
}

with open("guesses.txt", "r") as f:
    for line in f:
        guesses.append(line.replace('\n','').upper())

with open("answers.txt", "r") as f:
    for line in f:
        answers.append(line.replace('\n','').upper())


def getCommon(l1:list, l2:list) -> list:
    common = []
    ignoreIndex = []
    for a in l1:
        for j,b in enumerate(l2):
            if j in ignoreIndex:
                continue
            if a == b:
                common.append(a)
                ignoreIndex.append(j)
    return common

def getWord():
    word = answers[randint(0, len(answers))]
    
    return word

def isValid(word):
    return word in guesses or word in answers


def match(guess, word):
    code = ["b","b","b","b","b"]
    codeStr = ""
    guessList = list(guess)
    wordList = list(word)
    res = []

    for i,a in enumerate(guessList):
        if a in wordList:
            if wordList[i] == a:
                code[i] = "g"
                wordList[i] = ""
                guessList[i] = ""
    

    for j,b in enumerate(guessList):
        if b == "":
            continue
        if b in wordList:
            code[j] = "y"
            wordList[wordList.index(b)] = ""

    for i,a in enumerate(code):
        res += styleDict[a] + " " + guess[i] + " "
        codeStr += code[i]

     
    return res, codeStr

word = getWord()
i = 1
while i<7:
    inp = input(f"Guess {i}/6: ").upper()

    if len(inp) < 5:
        print("Word too short")
        continue
    elif len(inp) > 5:
        print("Word too long")
        continue
    elif not isValid(inp):
        print("Word not in list, guess again")
        continue
    output = match(inp, word)
    code = output[1]
    outputStr = ""
    for char in output[0]:
        outputStr += char
        print(outputStr, end='\r')
        sleep(0.035)
    print()
    
    if code == "ggggg":
        print(f"Bravo! You got the word in {i} tries")
        break

    if i == 6:
        print("No more trials left!")
        print(f"The word was {word}")
    
    i += 1
