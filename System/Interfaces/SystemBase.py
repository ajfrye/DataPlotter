
from .SubsystemBase import SubsystemBase
from abc import ABC, abstractmethod

class SystemBase(SubsystemBase):
    @abstractmethod
    def update_derivatives(self):
        pass