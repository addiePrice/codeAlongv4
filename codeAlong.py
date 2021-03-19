"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

import random
myList = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose one of the following options. Type a number ONLY!")
            choice = input("""1. Add to list
2. Add a bunch o' numbers to the list
3. Return the value at an index position
4. Print contents of list
5. Random Choice
6. Linear Search
7. End program  """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                print(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            else:
                break
        except:
            print("An error occured! :( ")

        
def addToList():
    newItem = input("What would you like to add? Please enter an integer ")
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input("How many numbers do you want me to add?  ")
    numRange = input("And how high would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete! What else do you want to do?")
    
def indexValues():
    indexPos = input("Choose a position in the list to see the value for!  ")
    print(myList[int(indexPos)-1])

def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the list in THE WORST WAY POSSIBLE MWAHAHAHAH!")
    searchItem = input("What are you looking for? Number-wise?  ")
    indexCount = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            indexCount = indexCount + 1
            print("Your item is at index {}".format(x))
    print("Your item appeared {} times in the list".format(indexCount))

    
if __name__ == "__main__":
    mainProgram()
