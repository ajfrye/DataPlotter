
from abc import ABC, abstractmethod

class SubsystemBase:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def finalize(self):
        pass