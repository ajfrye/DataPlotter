
from Architecture import BufferIterator

class SystemScheduler(BufferIterator):
    def __init__(self):
        self.buffer     = []
        self.iterator   = iter(self.buffer)

    def initialize(self):
        """
        Initialize all obects in the buffer
        """
        self.initialize_objects()

    def execute(self):
        obj = self.getNextObject()
        while obj is not None:
            obj.execute()
            obj.update_derivative()
            obj = self.getNextObject()

    def finalize(self):
        """
        finalize all objects in the buffer
        """
        self.finalize_objects()
