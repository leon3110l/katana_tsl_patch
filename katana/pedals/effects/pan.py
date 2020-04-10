from enum import IntEnum

from .. import FXPedal, FXType

class PanType(IntEnum):
    DEFAULT = 0
    AUTO = 0
    MANUAL = 1

class Pan(FXPedal):

    FX_TYPE = FXType.PAN

    def __init__(self,
                _type : PanType = PanType.DEFAULT,
                depth: int = 100,
                level: int = 50,
                pos: int = 50,
                rate: int = 40,
                wave_shape: int = 0,
                **kwargs
    ):
        super().__init__('pan')
        self.type = _type
        self.depth = depth
        self.level = level
        self.pos = pos
        self.rate = rate
        self.wave_shape = wave_shape