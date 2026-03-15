
class SystemScheduler:
    def __init__(self):
        self.buffer     = []
        self.iterator   = iter(self.buffer)

    def initialize(self):
        obj = self.getNextObject()
        while obj is not None:
            obj.initialize()
            obj = self.getNextObject()

    def push(self, obj):
        self.buffer.append(obj)

    def remove(self, obj):
        self.buffer.remove(obj)

    def getNextObject(self):
        try:
            obj = next(self.iterator)
        except StopIteration:
            obj = None
            # reset iterator
            self.iterator = iter(self.buffer)
        return obj

    def execute(self):
        obj = self.getNextObject()
        while obj is not None:
            obj.execute()
            obj.update_derivative()
            obj = self.getNextObject()

    def finalize(self):
        obj = self.getNextObject()
        while obj is not None:
            obj.finalize()
            obj = self.getNextObject()
