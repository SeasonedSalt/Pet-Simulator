pet = {"name": "", "type": "", "age": 0, "hunger": 0, "toys": []}

petToys = {"cat": ["scratching post", "toy mouse", "ball of yarn"],
"dog": ["chew toy", "stick", "frisbee"],
"fish": ["undersea castle", "fake coral", "buried treasure"]}

def initPet():
    petType = ""

    petOptions = list(petToys.keys())
    print(petOptions)

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

def quitSimulator():
    print("Quit the simulator. Thanks for playing!")

def feedPet():
    pet["hunger"] -= 10
    print("Fed your pet! Hunger decreased by 10")

def printStats():
    print("Your " + pet["type"] + pet["name"] + "is doing great!")
    print("Your pet currently has: " + str(len(pet["toys"])))
    for toy in pet["toys"]:
        print(toy)
    print("Your pet is currently at hunger of " + str(pet["hunger"]) + "of a max of 100")
    print("Your pet is currently at the age of " + str(pet["age"]) + "days old")

initPet()

def main():
  
  initPet()
  
  menuOptions = {"Q": { "funciton": quitSimulator, "text": "Quit the game"}, 
  "F": { "funciton": feedPet, "text": "Feed " + pet["name"] } }
  
  keepPlaying = True
  while keepPlaying:
      menuSelection = ""
      while menuSelection not in menuOptions.keys():
          printMenu(menuOptions)
          menuSelection = input("Which of these menu options would you like to use? ").upper()

      if menuSelection == "Q":
          keepPlaying = False
  
      menuOptions[menuSelection]["function"]()
      
      pet["hunger"] += 10
      pet["age"] += 1
      print()


main()
