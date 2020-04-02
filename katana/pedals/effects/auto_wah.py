from enum import IntEnum

from ..pedal import FXPedal, FXType

class AutoWahMode(Enum):
    DEFAULT = 0
    LOW_PASS = 0
    BAND_PASS = 1

class AutoWah(FXPedal):

    FX_TYPE = FXType.AUTO_WAH

    def __init__(self,
                mode : AutoWahMode = AutoWahMode.DEFAULT,
                depth: int = 60,
                direct_mix: int = 0,
                effect_level: int = 50,
                freq: int = 35,
                peak: int = 50,
                rate: int = 50,
    ):
        super().__init__('auto_wah')
        self.mode = mode
        self.depth = depth
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.freq = freq
        self.peak = peak
        self.rate = rate
