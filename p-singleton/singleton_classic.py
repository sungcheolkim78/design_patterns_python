class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance


class BorgSingleton(object):
    _shared_borg_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(BorgSingleton, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_borg_state
        return obj


if __name__ == "__main__":
    singleton1 = SingletonClass()
    singleton2 = SingletonClass()

    print(singleton1 is singleton2)

    # add new variable
    singleton1.variable = "Added variable"
    print(singleton2.variable)

    borg = BorgSingleton()
    borg.variable = "Added variable"

    class ChildBorg(BorgSingleton):
        pass

    childBorg = ChildBorg()
    print(borg is childBorg)
    print(childBorg.variable)
