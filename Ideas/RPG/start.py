from enums import CharacterType
from character import Character
import os

run = True


character = None

CHARACTER_FOLDER = "./Karakterek"
while run:
    if character is None:
        print("Szeretnéd betölteni a karaktered? y/n")
        user_input = input()
        if user_input == "y" or user_input == "Y":
            # TODO print out all
            print("Mi a karakter neved?")
            user_input = input()
            character = Character.load_from_json(os.path.join(CHARACTER_FOLDER, f"{user_input}.json"))
        else:
            print("Mi legyen a karater neve?")
            user_input = input()
            name = user_input
            print("Milyen tipusú legyen a karaktered?")
            
            print("Harcos - 1")
            print("Mágus - 2")
            print("Bárd - 3")

            user_input = input()
            type = CharacterType(int(user_input))
            character = Character(name, type)
            character.save_to_json()



