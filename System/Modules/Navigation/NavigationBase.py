
import numpy as np

class NavigationBase:
    def __init__(self):
        """
        Declare system state variables required
        for navigation
        """
        self.pos_ecef = None
        self.vel_ecef = None
        self.acc_ecef = None

    def initialize(self):
        """
        Initialize system state variables with
        initial state at startup
        """
        self.pos_ecef = np.zeros(3)
        self.vel_ecef = np.zeros(3)
        self.acc_ecef = np.zeros(3)

    def execute(self):
        pass

    def finalize(self):
        pass

    def update_derivatives(self, dt):
        pass

    def set_state(self, posEcef, velEcef, accEcef):
        self.posEcef = posEcef
        self.velEcef = velEcef
        self.accEcef = accEcef

    def get_pos(self):
        return self.pos_ecef

    def get_vel(self):
        return self.vel_ecef