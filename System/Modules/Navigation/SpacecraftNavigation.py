
import numpy as np

class SpacecraftNavigation:
    def __init__(self):
        """
        Declare system state variables required
        for navigation
        """
        self.posEcef = None
        self.velEcef = None
        self.accEcef = None

    def initialize(self):
        """
        Initialize system state variables with
        initial state at startup
        """
        self.posEcef = np.zeros(3)
        self.velEcef = np.zeros(3)
        self.accEcef = np.zeros(3)

    def execute(self):
        pass

    def finalize(self):
        pass
