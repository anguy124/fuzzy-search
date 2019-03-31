#An Nguyen
#Fuzzy Search
import time

def BuildShiftTable(pattern):
    table = {}
    m = len(pattern)
    for j in range(0,m-1):
        table[pattern[j]] = m - 1 - j
    return table

#will return the index of the left end of the first matching substring
def horspool(searchPhrase,fileContents):
    testTable = BuildShiftTable(searchPhrase)
    i = len(searchPhrase) - 1
    while i <= len(fileContents)-1:

        numMatching = 0   #indicates number of matched characters
        while (numMatching <= len(searchPhrase) - 1) and (searchPhrase[len(searchPhrase) - 1 - numMatching] == fileContents[i-numMatching]):
            numMatching = numMatching + 1
        if numMatching == len(searchPhrase):
            return i - len(searchPhrase) + 1
        elif fileContents[i] in testTable:
            i = i + testTable[fileContents[i]]
        else:
            i = i + len(searchPhrase)
    return -1

#makes a function that will do the same as horspool, but on the deleted phrases
def horspoolDeletion(searchPhrase,fileContents):
    found = False
    testTable = BuildShiftTable(searchPhrase)
    i = len(searchPhrase) - 1
    while i <= len(fileContents)-1:
        numMatching = 0  # indicates number of matched characters
        while (numMatching <= len(searchPhrase) - 1) and (
            searchPhrase[len(searchPhrase) - 1 - numMatching] == fileContents[i - numMatching]):
            numMatching = numMatching + 1
        if numMatching == len(searchPhrase):
            found = True
            print("Deleted characters:", searchPhrase, " Matching Index: ", i - len(searchPhrase) + 1)
        if fileContents[i] in testTable:
            i = i + testTable[fileContents[i]]
        else:
            i = i + len(searchPhrase)
    if (found == False):
        print("Deleted characters:", searchPhrase, " Matching Index: Not Found")

def horspoolSwap(searchPhrase,fileContents):
    found = False
    testTable = BuildShiftTable(searchPhrase)
    i = len(searchPhrase) - 1
    while i <= len(fileContents)-1:
        numMatching = 0  # indicates number of matched characters
        while (numMatching <= len(searchPhrase) - 1) and (
            searchPhrase[len(searchPhrase) - 1 - numMatching] == fileContents[i - numMatching]):
            numMatching = numMatching + 1
        if numMatching == len(searchPhrase):
            found = True
            print("Swapped Characters:", searchPhrase, " Matching Index: ", i - len(searchPhrase) + 1)
        if fileContents[i] in testTable:
            i = i + testTable[fileContents[i]]
        else:
            i = i + len(searchPhrase)
    if (found == False):
        print("Swapped characters:", searchPhrase, " Matching Index: Not Found")

def horspoolReplace(list_of_pattern,fileContents):
    found = False
    for searchPhrase in list_of_pattern:
        print("Searching for: ", searchPhrase)
        testTable = BuildShiftTable(searchPhrase)
        i = len(searchPhrase) - 1
        while i <= len(fileContents)-1:
            numMatching = 0  # indicates number of matched characters
            while (numMatching <= len(searchPhrase) - 1) and (searchPhrase[len(searchPhrase) - 1 - numMatching] == fileContents[i - numMatching] or searchPhrase[len(searchPhrase) - 1 - numMatching] == '~'):
                numMatching = numMatching + 1
            if numMatching == len(searchPhrase):
                found = True
                print("Replaced character:", fileContents[i - len(searchPhrase) + 1], " Matching Index: ", i - len(searchPhrase) + 1)
            if fileContents[i] in testTable:
                i = i + testTable[fileContents[i]]
            else:
                i = i + len(searchPhrase)
        if (found == False):
             print("Replaced characters:", searchPhrase, " Matching Index: Not Found")

def horspoolAddition(searchPhrase,fileContents):
    found = False
    testTable = BuildShiftTable(searchPhrase)
    mismatch = 0
    i = len(searchPhrase) - 1
    while i <= len(fileContents)-1:
        numMatching = 0  # indicates number of matched characters
        while (numMatching <= len(searchPhrase) - 1):
            if(searchPhrase[len(searchPhrase) - 1 - numMatching] == fileContents[i - numMatching]):
                numMatching = numMatching + 1
            if (searchPhrase[len(searchPhrase) - 1 - numMatching] != fileContents[i - numMatching]):
                mismatch += 1
                break
        if numMatching == len(searchPhrase):
            found = True
            print("Added characters:", searchPhrase, " Matching Index: ", i - len(searchPhrase) + 1)
        if fileContents[i] in testTable:
            i = i + testTable[fileContents[i]]
        else:
            i = i + len(searchPhrase)
    if (found == False):
        print("Added characters:", searchPhrase, " Matching Index: Not Found")


def letterPattern(searchPhrase):
    list_of_pattern = []
    searchList = list(searchPhrase)
    for i in range(len(searchPhrase)):
        searchList[i] = '~'
        ''.join(searchList)
        pstring = ''.join(searchList)
        list_of_pattern.append(pstring)
        searchList = list(searchPhrase)
    return list_of_pattern

def deletion(searchPhrase,fileContents):
    i = 0
    while i < len(searchPhrase):
        length = len(searchPhrase)
        phrase = searchPhrase[0:i] + searchPhrase[i+1:length]
        foundIndex = horspoolDeletion(phrase,fileContents)
        print(phrase)
        print(foundIndex)
        i+=1

def swap(searchPhrase):
    for i in range(0,len(searchPhrase)-1):
        newlist = list(searchPhrase)
        newlist[i],newlist[i+1] = newlist[i+1],newlist[i]
        newWord = ''.join(newlist)
        print(newWord)

def append(searchPhrase,fileContents):
    i = 0
    while i < len(searchPhrase):
        length = len(searchPhrase)
        phrase = searchPhrase[0:i] + searchPhrase[i+1:length]



def main():
    filename = input("Please enter in file name: ")
    phraseToSearch = input("Please enter in phrase to search: ")
    file = open(filename,"r")
    fileContents = file.read()
    print(BuildShiftTable(phraseToSearch))
    start = time.time()

    #single case of delete
    print(horspool(phraseToSearch,fileContents))
    #all cases
    deletion(phraseToSearch,fileContents)

    #single case of swap
    swap(phraseToSearch)
    print(horspoolSwap(phraseToSearch,fileContents))
    #need to do all cases of swap


    #single case of replace
    patternList = letterPattern(phraseToSearch)
    print(horspoolReplace(patternList,fileContents))

    #case of adding
    print(horspoolAddition(phraseToSearch,fileContents))

    end = time.time() - start
    print("Time took to search: ", end)
main()

