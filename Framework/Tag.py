class Tag:
    """Base class of all commands"""
    def __init__(self, factory, controller):
        self.controller = controller
        self.factory = factory
        self.framework = controller.framework


    def _aux_make(self):
        self.args = self.factory._command[1:]
        self.local = self.factory._local
        self.make()

    def make(self):
        """Define what the command will do"""
        pass