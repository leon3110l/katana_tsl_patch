from .pedal import BasePedal
from enum import IntEnum


class EQType(IntEnum):
    DEFAULT = 0
    PARAMETRIC = 0
    GRAPIC = 1

class EQ(BasePedal):

    CHAIN_POS = [4]

    def __init__(self,
                _type: EQType = EQType.DEFAULT,
                on: bool = True,
                geq_125hz: int = 0,
                geq_16khz: int = 0,
                geq_1khz: int = 0,
                geq_250hz: int = 0,
                geq_2khz: int = 0,
                geq_31hz: int = 24,
                geq_4khz: int = 0,
                geq_500hz: int = 0,
                geq_62hz: int = 0,
                geq_8khz: int = 0,
                geq_level: int = 0,
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
    ):
        super().__init__('eq', on)
        self.type = _type
        self.geq_125hz = geq_125hz
        self.geq_16khz = geq_16khz
        self.geq_1khz = geq_1khz
        self.geq_250hz = geq_250hz
        self.geq_2khz = geq_2khz
        self.geq_31hz = geq_31hz
        self.geq_4khz = geq_4khz
        self.geq_500hz = geq_500hz
        self.geq_62hz = geq_62hz
        self.geq_8khz = geq_8khz
        self.geq_level = geq_level
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
        