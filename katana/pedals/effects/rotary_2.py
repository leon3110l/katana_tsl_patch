from enum import IntEnum

from ..pedal import FXPedal, FXType

class Rotary2Type(IntEnum):
    DEFAULT = 1
    SLOW = 0
    FAST = 1

class Rotary2(FXPedal):

    FX_TYPE = FXType.ROTARY_2

    def __init__(self,
                _type : Rotary2Type = Rotary2Type.DEFAULT,
                balance: int = 50,
                depth: int = 50,
                direct_mix: int = 0,
                falltime: int = 50,
                level: int = 50,
                rate_fast: int = 50,
                rate_slow: int = 50,
                risetime: int = 50,
    ):
        super().__init__('rotary2')
        self.speed_select = _type
        self.balance = balance
        self.depth = depth
        self.direct_mix = direct_mix
        self.falltime = falltime
        self.level = level
        self.rate_fast = rate_fast
        self.rate_slow = rate_slow
        self.risetime = risetime
        