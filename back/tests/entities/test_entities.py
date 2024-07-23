# import pytest
# from faker import Faker

from back.domain.creatures.herbivore import Herbivore
from back.domain.creatures.predator import Predator
from back.domain.landscape.grass import Grass
from back.domain.landscape.rock import Rock
from back.domain.landscape.tree import Tree
from back.settings import *


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
    rock = Tree(
        type="Tree",
        is_active=True,
        transparensy=True,
        x_pos=1,
        y_pos=1,
        health=13,
        image="R",
    )
    assert rock.type == "Tree"
    assert rock.health == 13


def test_grass_create_success():
    rock = Grass(
        type="Grass",
        is_active=True,
        transparensy=True,
        x_pos=1,
        y_pos=1,
        health=11,
        image="R",
    )
    assert rock.type == "Grass"
    assert rock.x_pos == 1


def test_herbivore_create_success():
    rock = Herbivore(
        type="Herbivore",
        is_active=True,
        transparensy=True,
        x_pos=1,
        y_pos=1,
        health=11,
        image="R",
        speed=3,
        attack_rate=2,
    )
    assert rock.type == "Herbivore"
    assert rock.attack_rate == 2


def test_predator_create_success():
    rock = Predator(
        type="Predator",
        is_active=True,
        transparensy=False,
        x_pos=1,
        y_pos=1,
        health=11,
        image="R",
        speed=3,
        attack_rate=5,
    )
    assert rock.type == "Predator"
    assert rock.attack_rate == 5
