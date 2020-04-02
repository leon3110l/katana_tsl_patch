from enum import IntEnum

from ..pedal import FXPedal, FXType

class TouchWahMode(Enum):
    DEFAULT = 0
    LOW_PASS = 0
    BAND_PASS = 1

class TouchWahPolarity(Enum):
    DEFAULT = 0
    DOWN = 0
    UP = 1

class TouchWah(FXPedal):

    FX_TYPE = FXType.TOUCH_WAH

    def __init__(self,
                mode : TouchWahMode = TouchWahMode.DEFAULT,
                polar: TouchWahPolarity = TouchWahPolarity.DEFAULT,
                direct_mix: int = 0,
                effect_level: int = 50,
                freq: int = 35,
                peak: int = 35,
                sens: int = 50,
    ):
        super().__init__('t_wah')
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.freq = freq
        self.mode = mode
        self.peak = peak
        self.polar = polar
        self.sens = sens
