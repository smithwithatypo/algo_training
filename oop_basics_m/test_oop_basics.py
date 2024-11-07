import pytest
from oop_basics import Dog

def test_dog_initialization():
    mydog = Dog("buddy", 5)
    assert mydog.name == "buddy"
    assert mydog.age == 5

def test_dog_bark():
    mydog = Dog("buddy", 5)
    assert mydog.bark() == "buddy says woof!"

def test_dog_color_attribute():
    mydog = Dog("buddy", 5)
    mydog.color = "brown"
    assert mydog.color == "brown"