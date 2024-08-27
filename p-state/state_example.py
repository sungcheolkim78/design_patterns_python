from abc import ABC, abstractmethod
from typing import Optional


class TCPOctetStream:
    pass


class TCPConnection:
    def __init__(self):
        self._state = TCPState()

    def ActiveOpen(self):
        self._state.ActiveOpen(self)

    def PassiveOpen(self):
        self._state.PassiveOpen(self)

    def Close(self):
        self._state.Close(self)

    def Send(self):
        self._state.Send(self)

    def Acknowledge(self):
        self._state.Acknowledge(self)

    def Synchronize(self):
        self._state.Synchronize(self)

    def ProcessOctet(self, TCPOctetStream):
        pass

    def _ChangeState(self, newState):
        self._state = newState


class TCPState(object):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super(TCPState, cls).__new__(cls)
        return cls._instance

    def Transmit(self, tcpConnection: TCPConnection, tcpOctetStream: TCPOctetStream):
        pass

    def ActiveOpen(self, tcpConnection: TCPConnection) -> None:
        pass

    def PassiveOpen(self, tcpConnection: TCPConnection) -> None:
        pass

    def Close(self, tcpConnection: TCPConnection) -> None:
        pass

    def Synchronize(self, tcpConnection: TCPConnection) -> None:
        pass

    def Acknowledge(self, tcpConnection: TCPConnection) -> None:
        pass

    def Send(self, tcpConnection: TCPConnection) -> None:
        pass


class TCPEstablished(TCPState):
    def Transmit(self, tcpConnection: TCPConnection, tcpOctetStream: TCPOctetStream):
        print("TCPState: TCPEstablished")
        tcpConnection.ProcessOctet(tcpOctetStream)

    def Close(self, tcpConnection: TCPConnection) -> None:
        print("TCPState: TCPEstablished")
        tcpConnection._ChangeState(TCPListen())


class TCPListen(TCPState):
    def Send(self, tcpConnection: TCPConnection) -> None:
        print("TCPState: TCPListen")
        tcpConnection._ChangeState(TCPEstablished())


class TCPClosed(TCPState):
    def ActiveOpen(self, tcpConnection: TCPConnection) -> None:
        print("TCPState: TCPClosed")
        tcpConnection._ChangeState(TCPEstablished())

    def PassiveOpen(self, tcpConnection: TCPConnection) -> None:
        print("TCPState: TCPClosed")
        tcpConnection._ChangeState(TCPListen())


if __name__ == "__main__":
    tcp = TCPConnection()
    tcp.Send()
    tcp.Acknowledge()
    tcp.Synchronize()
