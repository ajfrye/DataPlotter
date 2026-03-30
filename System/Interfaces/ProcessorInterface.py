
class ProcessorInterface:
    def __init__(self):
        self.is_valid       = None
        self.time_step      = None
        self.environment    = None
        self.propagator     = None
        self.system         = None

    def initialize(self):
        #self.environment.initialize()
        #self.propagator.initialize()
        self.system.initialize()

    def execute(self):
        self.system.execute()
        #self.time_step = self.propagator.get_time_step(self.time_step)
        self.system.update_derivatives(self.time_step)

    def finalize(self):
        #self.environment.finalize()
        #self.propagator.finalize()
        self.system.finalize()
        self.is_valid   = False

    def set_valid(self):
        self.is_valid = True
        
    def set_time_step(self, time_step):
        self.time_step = time_step

    def set_environment(self, obj):
        self.environment = obj

    def set_system(self, obj):
        self.system = obj
    
    def set_propagator(self, obj):
        self.propagator = obj

    def get_event(self):
        return self.system.get_event()