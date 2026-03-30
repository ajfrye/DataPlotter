
from .Interfaces.SystemBase import SystemBase
from Architecture import BufferIterator

class SpaceSystem(SystemBase):
    def __init__(self, name: str):
        self.name       = name
        self.truth      = BufferIterator()
        self.hardware   = BufferIterator()
        self.software   = BufferIterator()

    def initialize(self):
        """
        Initialize all obects in the buffer
        """
        if not self.truth.empty_buffer():
            self.truth.initialize_objects()

        if not self.hardware.empty_buffer():
            self.hardware.initialize_objects()

        if not self.software.empty_buffer():
            self.software.initialize_objects()

    def execute(self):
        """
        Run execute on all obects in the buffer
        """
        if not self.truth.empty_buffer():
            self.truth.execute_objects()

        if not self.hardware.empty_buffer():
            self.hardware.execute_objects()

        if not self.software.empty_buffer():
            self.software.execute_objects()

    def update_derivatives(self, time_step):
        """
        Update derivatives on all obects in the buffer
        """
        if not self.truth.empty_buffer():
            obj = self.truth.get_next_object()
            while obj is not None:
                obj.update_derivatives(time_step)
                obj = self.truth.get_next_object()

        if not self.hardware.empty_buffer():
            obj = self.hardware.get_next_object()
            while obj is not None:
                obj.update_derivatives(time_step)
                obj = self.hardware.get_next_object()

        if not self.software.empty_buffer():
            obj = self.software.get_next_object()
            while obj is not None:
                obj.update_derivatives(time_step)
                obj = self.software.get_next_object()

    def get_event(self):
        event_dict = {}
        if not self.hardware.empty_buffer():
            event = self.hardware.get_events_buffer()
            if event:
                event_dict['Hardware'] = event

        if not self.software.empty_buffer():
            event = self.software.get_events_buffer()
            if event:
                event_dict['Software'] = event

        return event_dict

    def finalize(self):
        pass

    def print_name(self):
        print(self.name)