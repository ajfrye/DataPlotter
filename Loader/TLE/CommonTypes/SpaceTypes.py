
class Satellite:
    def __init__(self):
        self.name = None
        self.satellite_number = None
        self.classification = None
        self.launch_year = None
        self.launch_number = None
        self.launch_piece = None
        self.epoch_year = None
        self.epoch_day = None
        self.mean_motion_1st = None
        self.mean_motion_2nd = None
        self.bstar_drag = None
        self.ephemeris_type = None
        self.element_number = None

        self.inclination_deg = None
        self.raan_deg = None
        self.eccentricity = None
        self.arg_perigee_deg = None
        self.mean_anomaly_deg = None
        self.mean_motion_revs = None
        self.rev_number_epoch = None

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

class AstroState:
    def __init__(self, name, r, v):
        self.name   = name
        self.r      = r
        self.v      = v
