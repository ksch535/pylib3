# v 1.0

# for "making" static methods, example inside of class declarations: method = StaticMethod(method)
class StaticMethod:
    def __init__(self, anycallable):
        self.__call__ = anycallable
