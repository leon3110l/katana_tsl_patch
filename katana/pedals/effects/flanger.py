from enum import IntEnum

from ..pedal import FXPedal, FXType

class FlangerType(IntEnum):
    DEFAULT = 0

class Flanger(FXPedal):

    FX_TYPE = FXType.FLANGER

    def __init__(self,
                _type : FlangerType = FlangerType.DEFAULT,
                depth: int = 40,
                direct_mix: int = 0,
                effect_level: int = 60,
                low_cut: int = 0,
                manual: int = 82,
                rate: int = 31,
                reso: int = 50,
                separation: int = 0,
    ):
        super().__init__('flanger')
        self.type = _type
        self.depth = depth
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.low_cut = low_cut
        self.manual = manual
        self.rate = rate
        self.reso = reso
        self.separation = separation
        