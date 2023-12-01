class EmptyProductListException(Exception):
    def __init__(self, message="Can not calculate average rating of zero products"):
        self.message = message
        super().__init__(self.message)