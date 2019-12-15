class Control:
    """ Class for maintaining shared variables """
    
    def __init__(self):
        self.output_frame = None
        self.lock = None
        self.vs = None

        # filters
        self.filters = []
