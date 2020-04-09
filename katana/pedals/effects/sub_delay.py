from enum import IntEnum

from ..pedal import FXPedal, FXType

class SubDelayType(IntEnum):
    DEFAULT = 0
    MONO = 0
    PAN = 1

class SubDelay(FXPedal):

    FX_TYPE = FXType.SUB_DELAY

    def __init__(self,
                _type : SubDelayType = SubDelayType.DEFAULT,
                direct_mix: int = 100,
                effect_level: int = 50,
                f_back: int = 20,
                high_cut: int = 14,
                tap_time: int = 50,
                time_h: int = 3,
                time_l: int = 16,
                time: int = 400,
                **kwargs
    ):
        super().__init__('sub_delay')
        self.type = _type
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.f_back = f_back
        self.high_cut = high_cut
        self.tap_time = tap_time
        self.time_h = time_h
        self.time_l = time_l
        self.time = time