# Exception settins
APPLICATION_EXCEPTION_MESSAGE = r"Извините, в приложении возникла какая-то ошибка."
SETTINGS_EXCEPTION_MESSAGE = r"Произошла ошибка, проверьте файл конфигурации."
SERVICE_EXCEPTION_MESSAGE = r"Такого класса не существует"

# Entity settings
LANDSCAPE = [
    "Grass",
    "Rock",
    "Tree",
]
CREATURES = [
    "Herbivore",
    "Predator",
]
HEALTH = {
    "Grass": 20,
    "Rock": 10,
    "Tree": 10,
    "Herbivore": 10,
    "Predator": 10,
}
SPEED = {
    "Grass": 0,
    "Rock": 0,
    "Tree": 0,
    "Herbivore": 10,
    "Predator": 15,
}
ATTACK_RATE = {
    "Grass": 0,
    "Rock": 0,
    "Tree": 0,
    "Herbivore": 0,
    "Predator": 15,
}
TRANSPARENSY = {
    "Grass": False,
    "Rock": False,
    "Tree": False,
    "Herbivore": False,
    "Predator": False,
}
LAYERS = {
    0: "Grass",
    1: "Rock",
    2: "Tree",
    3: "Herbivore",
    4: "Predator",
}
IMAGE = {
    "Grass": "G",
    "Rock": "R",
    "Tree": "T",
    "Herbivore": "H",
    "Predator": "P",
}
TARGET = {
    "Herbivore": "Grass",
    "Predator": "Herbivore",
}

# Directions
DIR_LIST = [
    "up_left",
    "up",
    "up_right",
    "left",
    "right",
    "down_left",
    "down",
    "down_right",
]

# Game settings
WIDTH = 640
HEIGHT = 480
