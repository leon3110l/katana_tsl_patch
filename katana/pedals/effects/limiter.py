from enum import IntEnum

from ..pedal import FXPedal, FXType

class LimiterType(IntEnum):
    DEFAULT = 0
    BOSS_LIMITER = 0
    DBX_160X_RACK = 1
    UREI_1178_VINTAGE_RACK = 2

class Limiter(FXPedal):

    FX_TYPE = FXType.LIMITER

    def __init__(self,
                _type : LimiterType = LimiterType.DEFAULT,
                attack: int = 0,
                level: int = 42,
                ratio: int = 8,
                release: int = 20,
                thresh: int = 24,
                **kwargs
    ):
        super().__init__('limiter')
        self.type = _type
        self.attack = attack
        self.level = level
        self.ratio = ratio
        self.release = release
        self.thresh = thresh