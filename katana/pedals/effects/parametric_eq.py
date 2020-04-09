from ..pedal import FXType, FXPedal
from enum import IntEnum

class ParametricEQType(IntEnum):
    DEFAULT = 0

class ParametricEQ(FXType):

    FX_TYPE = FXType.PARAMETRIC_EQ

    def __init__(self,
                _type: ParametricEQType = ParametricEQType.DEFAULT,
                high_cut: int = 14,
                high_gain: int = 20,
                high_mid_freq: int = 26,
                high_mid_gain: int = 20,
                high_mid_q: int = 1,
                level: int = 20,
                low_cut: int = 0,
                low_gain: int = 20,
                low_mid_freq: int = 12,
                low_mid_gain: int = 20,
                low_mid_q: int = 0,
                position: int = 0,
                **kwargs
    ):
        super().__init__('parametric_eq')
        self.type = _type
        self.high_cut = high_cut
        self.high_gain = high_gain
        self.high_mid_freq = high_mid_freq
        self.high_mid_gain = high_mid_gain
        self.high_mid_q = high_mid_q
        self.level = level
        self.low_cut = low_cut
        self.low_gain = low_gain
        self.low_mid_freq = low_mid_freq
        self.low_mid_gain = low_mid_gain
        self.low_mid_q = low_mid_q
        self.position = position