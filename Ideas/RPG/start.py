from character import Character
import os

run = True


CHARACTER_FOLDER = "./Karakterek"
while run:
    print("Szeretnéd betölteni a karaktered? y/n")
    user_input = input()
    if user_input == "y" or user_input == "Y":
        # TODO print out all
        print("Mi a karakter neved?")
        user_input = input()
        character = Character.load_from_json(os.path.join(CHARACTER_FOLDER, f"{user_input}.json"))
    else:





character = Character.load_from_json("./Karakterek/edward.json")
character.name = "rapunzel"
character.save_to_json()


