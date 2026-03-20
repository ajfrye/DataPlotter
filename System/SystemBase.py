
from Architecture import BufferIterator

class SystemBase():
    def __init__(self, name: str):
        self.name       = name
        self.hardware   = BufferIterator()
        self.software   = BufferIterator()

    def initialize(self):
        """
        Initialize all obects in the buffer
        """
        if not self.hardware.empty_buffer():
            self.hardware.initialize_objects()

        if not self.software.empty_buffer():
            self.software.initialize_objects()

    def execute(self):
        pass

    def update_derivative():
        pass

    def finalize(self):
        pass

    def print_name(self):
        print(self.name)