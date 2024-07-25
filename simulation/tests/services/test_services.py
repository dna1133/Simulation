import pytest
from simulation.back.services.domain.entity_builder import EntityBuilder
from simulation.back.settings import DIR_LIST


def test_entity_builder_success():
    position = (1, 1)
    entity_grass = EntityBuilder.get("Grass", position)
    entity_tree = EntityBuilder.get("Tree", position)
    entity_rock = EntityBuilder.get("Rock", position)
    entity_predator = EntityBuilder.get("Predator", position)
    entity_herbivore = EntityBuilder.get("Herbivore", position)
    assert entity_grass.type == "Grass"
    assert entity_rock.is_active == True
    assert entity_tree.transparensy == False
    assert entity_predator.attack_rate == 15
    assert entity_herbivore.health == 10


def test_direction_builder_success():
    position = (2, 2)
    entity_predator = EntityBuilder.get("Predator", position)
    assert entity_predator.direction in DIR_LIST
