
from Architecture import BufferIterator

class SystemScheduler(BufferIterator):
    def __init__(self):
        super().__init__()
        self.initialized    = False
        self.complete       = False
        self.max_time       = None
        self.time_step      = None

    def run(self):
        """
        Run scheduler until max_time is reached or when a
        termination event is received
        """
        self.validate_scheduler_inputs()

        while not self.complete:
            if not self.initialized:
                self.initialize_objects()
                self.set_initial_object_time_step()
                self.initialized = True
            else:
                self.execute_objects()
                buffer = self.get_events_buffer()
                if buffer:
                    self.complete = True

    def set_max_time(self, max_time):
        """ Setter for max_time for execution """
        self.max_time = max_time

    def set_time_step(self, time_step):
        """ Setter for time_step """
        self.time_step = time_step

    def validate_scheduler_inputs(self):
        """
        Validate variables to make sure scheduler data
        has been properly populated
        """
        if self.max_time is None:
            print('-- WARNING  WARNING  WARNING  WARNING --')
            print('SystemScheduler - max_time not defined')
        if self.time_step is None:
            print('-- WARNING  WARNING  WARNING  WARNING --')
            print('SystemScheduler - time_step not defined')

    def set_initial_object_time_step(self):
        """
        Set the initial time-step on all objects in the buffer
        """
        obj = self.get_next_object()
        while obj is not None:
            obj.set_time_step(self.time_step)
            obj = self.get_next_object()

    def finalize(self):
        """
        finalize all objects in the buffer
        """
        self.finalize_objects()
