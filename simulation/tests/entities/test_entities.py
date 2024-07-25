# import pytest
# from faker import Faker

from simulation.back.domain.creatures.herbivore import Herbivore
from simulation.back.domain.creatures.predator import Predator
from simulation.back.domain.landscape.grass import Grass
from simulation.back.domain.landscape.rock import Rock
from simulation.back.domain.landscape.tree import Tree
from simulation.back.settings import *


def test_rock_create_success():
    rock = Rock(
        type="Rock",
        is_active=True,
        transparensy=True,
        x_pos=1,
        y_pos=1,
        health=11,
        image="R",
    )
    assert rock.type == "Rock"
    assert rock.health == 11


def test_tree_create_success():
    tree = Tree(
        type="Tree",
        is_active=True,
        transparensy=True,
        x_pos=1,
        y_pos=1,
        health=13,
        image="R",
    )
    assert tree.image == "R"
    assert tree.transparensy == True


def test_grass_create_success():
    grass = Grass(
        type="Grass",
        is_active=True,
        transparensy=True,
        x_pos=1,
        y_pos=1,
        health=11,
        image="R",
    )
    assert grass.y_pos == 1
    assert grass.x_pos == 1


def test_herbivore_create_success():
    herbivore = Herbivore(
        type="Herbivore",
        is_active=True,
        transparensy=True,
        x_pos=1,
        y_pos=1,
        health=11,
        image="R",
        speed=3,
        attack_rate=2,
        target="Grass",
        direction="up",
    )
    assert herbivore.type == "Herbivore"
    assert herbivore.speed == 3


def test_predator_create_success():
    predator = Predator(
        type="Predator",
        is_active=True,
        transparensy=False,
        x_pos=1,
        y_pos=1,
        health=11,
        image="R",
        speed=3,
        attack_rate=5,
        target="Herbivore",
        direction="up",
    )
    assert predator.type == "Predator"
    assert predator.attack_rate == 5
