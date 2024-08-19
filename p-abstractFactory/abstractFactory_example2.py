from Enum import Enum

Enum

class Room:
    def __init__(self, n: int):
        self._id = n

    def SetSide(self, direction, obj):



class Wall:
    pass


class Door:
    def __init__(self, r1: Room, r2: Room):
        self._r1 = r1
        self._r2 = r2


class Maze:
    def AddRoom(self, r1: Room):
        pass


class MazeFactory(object):
    def __init__(self):
        pass

    def MakeMaze(self) -> Maze:
        return Maze()

    def MakeWall(self) -> Wall:
        return Wall()

    def MakeRoom(self, n: int) -> Room:
        return Room(n)

    def MakeDoor(self, r1: Room, r2: Room) -> Door:
        return Door(r1, r2)


def CreateMaze(factory: MazeFactory):
    aMaze = factory.MakeMaze()
    r1 = factory.MakeRoom(1)
    r2 = factory.MakeRoom(2)
    aDoor = factory.MakeDoor(r1, r2)

    aMaze.AddRoom(r1)
    aMaze.AddRoom(r2)

    r1.SetSide(North, factory.MakeWall())