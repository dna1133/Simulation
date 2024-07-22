# import pytest
# from faker import Faker

from back.entities.entities import Rock
from back.settings import HEALTH


def test_rock_create_success():
    rock = Rock()
    assert rock.health.as_generic_type() != HEALTH.get("Rock")


def test_example():
    assert 1 + 1 == 2
