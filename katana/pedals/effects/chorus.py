from enum import IntEnum

from ..pedal import FXPedal, FXType

class Chorus_2x2Type(IntEnum):
    DEFAULT = 0

class Chorus_2x2(FXPedal):

    FX_TYPE = FXType.TWO_BY_TWO_CHORUS

    def __init__(self,
                _type : Chorus_2x2Type = Chorus_2x2Type.DEFAULT,
                direct_level: int = 80,
                high_depth: int = 48,
                high_level: int = 65,
                high_pre_delay: int = 3,
                high_rate: int = 33,
                low_depth: int = 46,
                low_level: int = 75,
                low_pre_delay: int = 3,
                low_rate: int = 43,
                xover_freq: int = 4,
                **kwargs
    ):
        super().__init__('ring_mod')
        self.type = _type
        self.direct_level = direct_level
        self.high_depth = high_depth
        self.high_level = high_level
        self.high_pre_delay = high_pre_delay
        self.high_rate = high_rate
        self.low_depth = low_depth
        self.low_level = low_level
        self.low_pre_delay = low_pre_delay
        self.low_rate = low_rate
        self.xover_freq = xover_freq