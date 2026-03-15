
class ProcessorInterface:
    def __init__(self):
        self.environment    = None
        self.system         = None
        self.event          = {}

    def setEnvironment(self, obj):
        self.environment = obj

    def setSystem(self, obj):
        self.system = obj