from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        print(f"Context: transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class concreteStateA(State):
    def handle1(self) -> None:
        print("StateA: handles request1.")
        print("StateA: wants to change the state of the context.")
        self.context.transition_to(concreteStateB())

    def handle2(self) -> None:
        print("StateA: handle request2")


class concreteStateB(State):
    def handle1(self) -> None:
        print("StateB: handles request1")

    def handle2(self) -> None:
        print("StateB: handles request2.")
        print("StateB: wants to change the state of the context.")
        self.context.transition_to(concreteStateA())


if __name__ == "__main__":
    context = Context(concreteStateA())
    context.request1()
    context.request2()

    context = Context(concreteStateB())
    context.request1()
    context.request2()
