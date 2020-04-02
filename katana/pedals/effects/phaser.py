from enum import IntEnum

from ..pedal import FXPedal, FXType

class PhaserType(IntEnum):
    DEFAULT = 0
    FOUR_STAGE = 0
    EIGHT_STAGE = 1
    TWELVE_STAGE = 2
    BI_PHASE = 3

class Phaser(FXPedal):

    FX_TYPE = FXType.PHASER

    def __init__(self,
                _type : PhaserType = PhaserType.DEFAULT,
                depth: int = 40,
                direct_mix: int = 0,
                effect_level: int = 100,
                manual: int = 55,
                rate: int = 70,
                reso: int = 0,
                step_rate: int = 0,
    ):
        super().__init__('phaser')
        self.type = _type
        self.depth = depth
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.manual = manual
        self.rate = rate
        self.reso = reso
        self.step_rate = step_rate
        