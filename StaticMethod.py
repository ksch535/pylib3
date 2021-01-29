# v 1.0

# for "making" static methods
class StaticMethod:
    def __init__(self, anycallable):
        self.__call__ = anycallable
