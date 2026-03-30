
class BufferIterator:
    def __init__(self):
        self.buffer     = []
        self.iterator   = iter(self.buffer)
        self.events     = {}

    def initialize_objects(self):
        """
        Initialize all obects in the buffer
        """
        obj = self.get_next_object()
        while obj is not None:
            obj.initialize()
            obj = self.get_next_object()

    def execute_objects(self):
        """
        run execute on all objects in the buffer
        and check for events
        """
        obj = self.get_next_object()
        while obj is not None:
            obj.execute()
            event = obj.get_event()
            if event is not None:
                self.events.update(event)
            obj = self.get_next_object()

    def finalize_objects(self):
        """
        finalize all objects in the buffer
        """
        obj = self.get_next_object()
        while obj is not None:
            obj.finalize()
            obj = self.get_next_object()

    def push(self, obj):
        """
        Append a new object into buffer
        """
        self.buffer.append(obj)

    def remove(self, obj):
        """
        Remove desired object from the buffer
        """
        self.buffer.remove(obj)

    def empty_buffer(self):
        """
        Checks the length of the buffer and 
        returns True is the buffer is empty
        """
        if len(self.buffer) == 0:
            return True
        else:
            return False

    def get_next_object(self):
        """
        Return the next object in the iterator.

        Once the iterator has run out of objects,
        restart the iterator back to the first object.
        """
        try:
            obj = next(self.iterator)
        except StopIteration:
            obj = None
            # reset iterator
            self.iterator = iter(self.buffer)
        return obj

    def get_events_buffer(self):
        """
        Return buffer conataining all events that have occured
        for all systems

        A particular event may be used as termination criteria
        """
        return self.events
