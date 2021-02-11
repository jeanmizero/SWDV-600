wordsFileName = "words_1.csv"
wordsFile = open(wordsFileName, "r")

totalNumberOfEs = 0
nextLine = wordsFile.readline()
while nextLine != "":
    words = nextLine.split(",")
    for word in words:
        numberOfEs = word.count("e")
        totalNumberOfEs = totalNumberOfEs + numberOfEs
    print("Hello")
    nextLine = wordsFile.readline()
wordsFile.close()
print("The total number of e's is {0}".format(totalNumberOfEs))
