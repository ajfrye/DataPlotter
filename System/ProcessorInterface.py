
class ProcessorInterface:
    def __init__(self):
        self.is_valid       = None
        self.environment    = None
        self.propagator     = None
        self.system         = None
        self.event          = {}

    def initialize(self):
        self.environment.initialize()
        self.propagator.initialize()
        self.system.initialize()

    def execute(self):
        self.system.execute()
        self.system.update_derivatives()

    def finalize(self):
        self.environment.finalize()
        self.propagator.finalize()
        self.system.finalize()
        self.is_valid   = False
        self.event      = {}

    def set_valid(self):
        self.is_valid = True
        
    def set_environment(self, obj):
        self.environment = obj

    def set_system(self, obj):
        self.system = obj
    
    def set_propagator(self, obj):
        self.propagator = obj
    
    def set_event(self, event):
        self.event.update(event)