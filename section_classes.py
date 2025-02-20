import logging
import random

LOGGER = logging.getLogger(__name__)

class Animal:
    def __init__(self, name: str):
        self.name = name
        LOGGER.info("Initialized Animal")

    def make_sound(self) -> str:
        LOGGER.info("Making Animal sound")
        return "Any sound!"

    def make_move(self):
        raise NotImplementedError()

class Dog(Animal):
    def bark(self) -> str:
        LOGGER.info("Making Dog sound")
        return "A dog sound!"

    def run(self) -> str:
        LOGGER.info("Dog running")
        return "Running!"
    
    def make_move(self):  # EXPLAIN: Implementing make_move() to match test expectations.
        return self.run()  # EXPLAIN: Now returns "Running!" instead of raising an error.

    def make_sound(self) -> str:  # EXPLAIN: Override make_sound() to match the test.
        LOGGER.info("Dog making sound")
        return self.bark()  # EXPLAIN: it returns "A dog sound!" instead of "Any sound!"
        
class Cat(Animal):
    _hungry = None

    @property
    def hungry(self) -> bool:
        if self._hungry is None:
            self._hungry = random.choice([True, False])
            LOGGER.debug("Cat is hunge=%s", self._hungry)
        return self._hungry

class Horse(Animal):
    """horse class"""
    # TASK: add implementation here
    def __init__(self, name: str, height: int):
        super().__init__(name)  # Call Animal's constructor.
        self.height = height  # Only added height here as asked in the Task.
