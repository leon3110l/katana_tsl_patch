from enum import IntEnum

from .. import FXPedal, FXType

class RotaryType(IntEnum):
    DEFAULT = 1
    SLOW = 0
    FAST = 1

class Rotary(FXPedal):

    FX_TYPE = FXType.ROTARY_1

    def __init__(self,
                _type : RotaryType = RotaryType.DEFAULT,
                depth: int = 60,
                fall_time: int = 0,
                level: int = 50,
                rate_fast: int = 85,
                rate_slow: int = 30,
                rise_time: int = 0,
                **kwargs
    ):
        super().__init__('rotary')
        self.speed_select = _type
        self.depth = depth
        self.fall_time = fall_time
        self.level = level
        self.rate_fast = rate_fast
        self.rate_slow = rate_slow
        self.rise_time = rise_time
        