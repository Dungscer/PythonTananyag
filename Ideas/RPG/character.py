import json
import os

from enums import CharacterType

CHARACTER_FOLDER = "./Karakterek"


class Character():
    def __init__(self, name, type:CharacterType):
        self.name = name
        self.alive = True
        self.type = type
        self.current_page = 0

    def to_dict(self):
        return {
            "name": self.name,
            "alive": self.alive,
            "current_page": self.current_page,
            "type": self.type
            
        }

    @staticmethod
    def from_dict(data):
        character = Character(data["name"])
        character.alive = data["alive"]
        character.current_page = data["current_page"]
        character.type = data["type"]
        return character

    def save_to_json(self):
        filename = os.path.join(CHARACTER_FOLDER, f"{self.name}.json")
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_json(filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return Character.from_dict(data)