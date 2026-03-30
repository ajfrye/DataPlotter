
from Utilities.Space import *
from .CommonTypes.SpaceTypes import AstroState

class TleLoader:
    def __init__(self, filename):
        self.filename   = filename
        self.satellites = []

    def load_data(self):
        with open(self.filename, 'r') as f:
            line = f.readline()
            while line:
                sat = Satellite()
                sat.name                = line.rstrip()

                line = f.readline()
                sat.satellite_number    = line[2:7]
                sat.classification      = line[7]
                sat.launch_year         = line[9:11]
                sat.launch_number       = line[11:14]
                sat.launch_piece        = line[14:17]
                sat.epoch_year          = line[18:20]
                sat.epoch_day           = line[20:32]
                sat.mean_motion_1st     = line[33:43]
                sat.mean_motion_2nd     = line[44:52]
                sat.bstar_drag          = line[53:61]
                sat.ephemeris_type      = line[62]
                sat.element_number      = line[64:68]
                
                line = f.readline()
                sat.inclination_deg     = line[8:16]
                sat.raan_deg            = line[17:25]
                sat.eccentricity        = '.' + line[26:33]
                sat.arg_perigee_deg     = line[34:42]
                sat.mean_anomaly_deg    = line[43:51]
                sat.mean_motion_revs    = line[52:63]
                sat.rev_number_epoch    = line[63:68]

                self.satellites.append(sat)
                line = f.readline()

    def get_satellite_buffer(self):
        return self.satellites

    def get_astro_state(self):
        state_buffer = []
        for sat in self.satellites:
            r, v = orbital_params_to_r_v(sat)
            astro_state = AstroState(sat.name, r,v)
            state_buffer.append(astro_state)
        return state_buffer

class Satellite:
    def __init__(self):
        self.name               = None
        self.satellite_number   = None
        self.classification     = None
        self.launch_year        = None
        self.launch_number      = None
        self.launch_piece       = None
        self.epoch_year         = None
        self.epoch_day          = None
        self.mean_motion_1st    = None
        self.mean_motion_2nd    = None
        self.bstar_drag         = None
        self.ephemeris_type     = None
        self.element_number     = None

        self.inclination_deg    = None
        self.raan_deg           = None
        self.eccentricity       = None
        self.arg_perigee_deg    = None
        self.mean_anomaly_deg   = None
        self.mean_motion_revs   = None
        self.rev_number_epoch   = None

    def print_info(self):
        print(f'name: {self.name}')
        print(f'satellite number: {self.satellite_number}')
        print(f'calssification: {self.classification}')
        print(f'launch year: {self.launch_year}')
        print(f'launch number: {self.launch_number}')
        print(f'launch piece: {self.launch_piece}')
        print(f'epoch year: {self.epoch_year}')
        print(f'epoch day: {self.epoch_day}')
        print(f'mean motion 1st derivative: {self.mean_motion_1st}')
        print(f'mean motion 2nd derivative: {self.mean_motion_2nd}')
        print(f'BSTAR drag term: {self.bstar_drag}')
        print(f'ephemeris type: {self.ephemeris_type}')
        print(f'element number: {self.element_number}')
        print(f'inclination (deg): {self.inclination_deg}')
        print(f'right ascention of the ascending node (deg): {self.raan_deg}')
        print(f'eccentricity: {self.eccentricity}')
        print(f'argument of perigee (deg): {self.arg_perigee_deg}')
        print(f'mean anomaly (deg): {self.mean_anomaly_deg}')
        print(f'mean motion (revs per day): {self.mean_motion_revs}')
        print(f'revolution number at epoch (revs): {self.rev_number_epoch}')
        print('')