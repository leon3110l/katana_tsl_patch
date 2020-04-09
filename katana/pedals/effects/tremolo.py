from enum import IntEnum

from ..pedal import FXPedal, FXType

class TremoloType(IntEnum):
    DEFAULT = 0

class Tremolo(FXPedal):

    FX_TYPE = FXType.TREMOLO

    def __init__(self,
                _type : TremoloType = TremoloType.DEFAULT,
                depth: int = 65,
                level: int = 50,
                rate: int = 85,
                wave_shape: int = 70,
                **kwargs
    ):
        super().__init__('tremolo')
        self.type = _type
        self.depth = depth
        self.level = level
        self.rate = rate
        self.wave_shape = wave_shape
        