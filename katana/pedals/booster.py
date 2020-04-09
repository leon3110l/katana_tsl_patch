from .pedal import BasePedal
from enum import IntEnum

class BoosterType(IntEnum):
    DEFAULT = 10
    MID_BOOST = 0
    CLEAN_BOOST = 1
    TREBLE_BOOST = 2
    CRUNCH = 3
    NATURAL_OD = 4
    WARM_OD = 5
    FAT_DS = 6
    LEAD_DS = 7
    METAL_DS = 8
    OCT_FUZZ = 9
    BLUES_OD = 10
    OD_1 = 11
    TUBESCREAMER = 12
    TURBO_OD = 13
    DIST = 14
    RAT = 15
    GUV_DS = 16
    DST_PLUS = 17
    METAL_ZONE = 18
    SIXTIES_FUZZ = 19
    MUFF_FUZZ = 20
    CUSTOM = 21

class Booster(BasePedal):

    CHAIN_POS = [15]

    def __init__(self,
                _type: BoosterType = BoosterType.DEFAULT,
                on: bool = True,
                bottom: int = 50,
                custom_bottom: int = 50,
                custom_character: int = 50,
                custom_high: int = 50,
                custom_low: int = 50,
                custom_top: int = 50,
                custom_type: int = 0,
                direct_mix: int = 0,
                drive: int = 20,
                effect_level: int = 56,
                solo_level: int = 50,
                solo_sw: int = 0,
                tone: int = 46,
                **kwargs
    ):
        super().__init__('od_ds', on)
        self.type = _type
        self.bottom = bottom
        self.custom_bottom = custom_bottom
        self.custom_character = custom_character
        self.custom_high = custom_high
        self.custom_low = custom_low
        self.custom_top = custom_top
        self.custom_type = custom_type
        self.direct_mix = direct_mix
        self.drive = drive
        self.effect_level = effect_level
        self.solo_level = solo_level
        self.solo_sw = solo_sw
        self.tone = tone