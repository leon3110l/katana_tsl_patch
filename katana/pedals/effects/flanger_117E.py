from enum import IntEnum

from ..pedal import FXPedal, FXType

class Flanger117EType(IntEnum):
    DEFAULT = 0

class Flanger117E(FXPedal):

    FX_TYPE = FXType.FLANGER_117E

    def __init__(self,
                _type : Flanger117EType = Flanger117EType.DEFAULT,
                manual: int = 0,
                regen: int = 0,
                speed: int = 0,
                width: int = 0,
                **kwargs
    ):
        super().__init__('flanger117e')
        self.type = _type
        self.manual = manual
        self.regen = regen
        self.speed = speed
        self.width = width
        