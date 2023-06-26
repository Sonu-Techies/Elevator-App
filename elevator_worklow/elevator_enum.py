from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def convertable_list(cls):
        return tuple(map(lambda enum_val: (enum_val.name, enum_val.value), cls))



class DirectionStatusEum(ExtendedEnum):
    """
    Lift Direction Enum
    """

    UP = "UP"
    DOWN = "DOWN"
    STOPPED = "STOPPED"


class DoorStatusEnum(ExtendedEnum):
    """
    Door Status Enum
    """
    OPEN = "OPEN"
    CLOSE = "CLOSE"
    PARTIAL_OPEN = "PARTIAL_OPEN"
