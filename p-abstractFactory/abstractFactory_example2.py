from enum import Enum
from typing import List, Dict, Optional


class Direction(Enum):
    North = 1
    South = 2
    East = 3
    West = 4


class MapSite:
    def Enter(self):
        pass


class Room(MapSite):
    def __init__(self, roomNo: int):
        self._roomNumber = roomNo
        self._sides: Dict[Direction, Optional[MapSite]] = {
            Direction.North: None,
            Direction.South: None,
            Direction.East: None,
            Direction.West: None
        }

    def SetSide(self, direction: Direction, obj: MapSite):
        self._sides[direction] = obj

    def GetSide(self, direction: Direction) -> Optional[MapSite]:
        return self._sides[direction]


class Wall(MapSite):
    pass


class Door(MapSite):
    def __init__(self, r1: Room, r2: Room):
        self._room1 = r1
        self._room2 = r2
        self._isOpen = False

    def OtherSideFrom(self, room: Room) -> Room:
        if room == self._room1:
            return self._room2
        else:
            return self._room1


class Maze:
    def AddRoom(self, r1: Room):
        pass

    def RoomNo(self, roomNo: int) -> Room:
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


class MazeGame:
    def CreateMaze(self, factory: MazeFactory) -> Maze:
        aMaze = factory.MakeMaze()
        r1 = factory.MakeRoom(1)
        r2 = factory.MakeRoom(2)
        aDoor = factory.MakeDoor(r1, r2)

        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)

        r1.SetSide(Direction.North, factory.MakeWall())
        r1.SetSide(Direction.East, aDoor)
        r1.SetSide(Direction.South, factory.MakeWall())
        r1.SetSide(Direction.West, factory.MakeWall())

        r2.SetSide(Direction.North, factory.MakeWall())
        r2.SetSide(Direction.East, factory.MakeWall())
        r2.SetSide(Direction.South, factory.MakeWall())
        r2.SetSide(Direction.West, aDoor)

        return aMaze


class EnchantedMazeFactory(MazeFactory):
    def CastSpell(self):
        return 1

    def MakeRoom(self, n: int) -> Room:
        return EnchantedRoom(n, CastSpell())

    def MakeDoor(self, r1: Room, r2: Room) -> Door:
        return DoorNeedingSpell(r1, r2)


class BombedMazeFactory(MazeFactory):
    def MakeRoom(self, n: int) -> Room:
        return RoomWithABomb(n)

    def MakeWall(self) -> Wall:
        return BombedWall()


if __name__ == '__main__':
    game = MazeGame()
    factory = MazeFactory()
    game.CreateMaze(factory)
