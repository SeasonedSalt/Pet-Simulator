pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

petToys = {"cat": ["scratching post", "toy mouse", "ball of yarn"],
"dog": ["chew toy", "stick", "frisbee"],
"fish": ["undersea castle", "fake coral", "buried treasure"]}

def initPet():
    petType = ""

    petOptions = list(petToys.keys())
  

    while petType not in petOptions:
        print("Please input a type of pet from the following options: ")
        for option in petOptions:
            print(option)
        petType = input("Please input one of the pets: ")

    pet["type"] = petType

    pet["name"] = input("What would you like to name your " + pet["type"] + "? ")


def printMenu(menuOptions):
  optionKeys = list(menuOptions.keys())

  print("Here are your options:")
  print("-------")
  for key in optionKeys:
      print(key + ":\t" + menuOptions[key]["text"])

def playToys():
    print(pet["name"] + " had a great playtime with their toys!")

def getToys():
    print("Let's get new toys!")
    toyOptions = petToys[pet["type"]]
    
    toyNum = -1
    while toyNum < 0 or toyNum > len(toyOptions) - 1:
      for i in range(len(toyOptions)):
          print(str(i) + ": " + toyOptions[i])
      toyNum = int(input("Input the number of the toy you would like: "))

    chosenToy = toyOptions[toyNum]
    pet["toys"].append(chosenToy)
    print("You selected the " + chosenToy + "!")

def quitSimulator():
    print("Quit the simulator. Thanks for playing!")

def feedPet():
    newHunger = pet["hunger"] - 20
    if newHunger < 0:
        newHunger = 0
    pet["hunger"] = newHunger
    print("Fed your pet! Hunger decreased by 10")

def printStats():
    print("Your " + pet["type"] + " " + pet["name"] + " is doing great!")
    print("Your pet currently has: " + str(len(pet["toys"])) + " toys, which are: ")
    for toy in pet["toys"]:
        print(toy)
    print("Your pet is currently at hunger of " + str(pet["hunger"]) + " of a max of 100")
    print("Your pet is currently at the age of " + str(pet["age"]) + " days old")

menuOptions = {"Q": { "function": quitSimulator, "text": "Quit the game"}, 
  "F": { "function": feedPet, "text": "Feed " + pet["name"] },
  "P": { "function": playToys, "text": "Play with " + pet["name"]  },
  "G": { "function": getToys, "text": "Get new toys for " + pet["name"] + "" }}

def main():
  
  initPet()
  
      
  pet["hunger"] += 10
  pet["age"] += 1

  printStats()
  
def looper():
  keepPlaying = True
  while True:
      main()
      menuSelection = ""
      while menuSelection not in menuOptions.keys():
          printMenu(menuOptions)
          menuSelection = input("Which of these menu options would you like to use? ").upper()
        
          menuOptions[menuSelection]["function"]()

      if menuSelection == "Q".upper():
          keepPlaying = False


looper()
