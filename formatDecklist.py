import os

def getCardQty(card):
    deckLine = decklist[card].strip().split(" ")
    for x in deckLine:
        if x.isnumeric():
            cardQty = x
    return cardQty

def getCardNum(card):
    deckLine = decklist[card].strip().split(" ")
    cardNum = deckLine.pop()
    return cardNum

def getCardName(card):
    deckLine = decklist[card].strip().split(" ")
    wordsInName = len(deckLine)
    wordsInName -= 2    #removing the first and last element
    cardName = ""
    for y in range(wordsInName):
        cardName += deckLine[y + 1] + " "
    return cardName

def getDeckline(cardQty, cardNum, cardName):
    if len(cardNum) < 6:
        return (cardQty + " " + cardNum + "\t\t" + cardName)
    else:
        return (cardQty + " " + cardNum + "\t" + cardName)

def getDecklist():
    deck = ""
    for x in range(len(decklist)):
        cardQty = getCardQty(x)
        cardNum = getCardNum(x)
        cardName = getCardName(x)
        deck += getDeckline(cardQty, cardNum, cardName) + "\n"
    return deck

def getDate():
    from datetime import date
    todaysDate = date.today().strftime("%Y/%m/%d")
    return todaysDate

def createTxtFile(fileName):
    filePath = r"E:/Documents/Digimon/decklists/"
    if not os.path.exists(filePath):
        os.makedirs(filePath)

    fileName += ".txt"
    createFile = os.path.join(filePath, fileName)
    cleanDeckList = getDecklist()
    with open(createFile, 'w') as file:
        file.writelines(cleanDeckList)
        file.close()

def getRawData(fileName):
    filePath = "E:/Documents/Digimon/decklists/"
    fileName += ".txt"
    completeFilePath = filePath + fileName
    openedFile = open(completeFilePath, 'r')
    rawData = openedFile.read()
    openedFile.close()
    return rawData

def getTxtFileNames():
    filePath = r"E:/Documents/Digimon/decklists/"
    whatsInDirectory = os.listdir(filePath)
    for files in whatsInDirectory:
        if files.endswith('.txt'):
            filesInDirectory = "deckList"

    return filesInDirectory

rawFileName = "rawDecklists"
decklist = getRawData(rawFileName).split("\n")
fileName = "deckList"
formatDecklist = createTxtFile(fileName)
#filesInDirectory = getTxtFileNames()
#print(filesInDirectory)
