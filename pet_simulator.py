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