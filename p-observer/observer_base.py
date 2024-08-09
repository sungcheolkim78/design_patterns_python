class Observer(object):
    def __init__(self):
        pass

    def update(self, theChangedSubject) -> None:
        raise NotImplementedError("Please implement this method")


class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self, o: Observer):
        self._observers.append(o)

    def detach(self, o: Observer):
        self._observers.remove(o)

    def notify(self):
        for i in self._observers:
            i.update(self)

