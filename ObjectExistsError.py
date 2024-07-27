class ObjectExistsError(Exception):
    def __init__(self, message="Object already present"):
        self.message = message
        super().__init__(self.message)
