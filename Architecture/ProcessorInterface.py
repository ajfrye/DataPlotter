
class ProcessorInterface:
    def __init__(self):
        self.is_valid       = None
        self.environment    = None
        self.system         = None
        self.propagator     = None
        self.event          = {}

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