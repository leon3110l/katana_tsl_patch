from enum import IntEnum
from .pedal import BasePedal

# all amp types
class AmpType(IntEnum):
    DEFAULT = 11
    NATURAL_CLEAN = 0
    ACOUSTIC = 1
    FULL_RANGE = 1
    COMBO_CRUNCH = 2
    STACK_CRUNCH = 3
    HI_GAIN_STACK = 4
    POWER_DRIVE = 5
    EXTREME_LEAD = 6
    CORE_METAL = 7
    CLEAN = 8
    JC_120 = 8
    CLEAN_TWIN = 9
    PRO_CRUNCH = 10
    CRUNCH = 11
    TWEED = 11
    DELUXE_CRUNCH = 12
    VO_DRIVE = 13
    VO_LEAD = 14
    MATCH_DRIVE = 15
    BG_LEAD = 16
    BG_DRIVE = 17
    MS_1959_1 = 18
    MS_1959_1_2 = 19
    R_FIER_VINTAGE = 20
    R_FIER_MODERN = 21
    BROWN = 22
    SLDN = 22
    LEAD = 23
    DRIVE_5150 = 23
    CUSTOM = 24


class Amp(BasePedal):

    CHAIN_POS = [2]

    def __init__(self,
                _type: AmpType = AmpType.DEFAULT,
                on: bool = True,
                bass: int = 50,
                bright: int = 0,
                custom_bottom: int = 50,
                custom_char: int = 50,
                custom_edge: int = 50,
                custom_preamp_high: int = 50,
                custom_preamp_low: int = 50,
                custom_sp_cabinet: int = 0,
                custom_sp_color_high: int = 10,
                custom_sp_color_low: int = 10,
                custom_sp_num: int = 2,
                custom_sp_size: int = 7,
                custom_type: AmpType = AmpType.DEFAULT,
                direct_mix: int = 0,
                gain_sw: int = 1,
                gain: int = 30,
                level: int = 20,
                mic_dis: int = 1,
                mic_level: int = 100,
                mic_pos: int = 5,
                mic_type: int = 1,
                middle: int = 50,
                presence: int = 10,
                solo_level: int = 50,
                solo_sw: int = 0,
                sp_type: int = 0,
                t_comp: int = 10,
                treble: int = 50
    ):

        super().__init__('preamp_a', on)
        self.type = _type
        self.bass = bass
        self.bright = bright
        self.custom_bottom = custom_bottom
        self.custom_char = custom_char
        self.custom_edge = custom_edge
        self.custom_preamp_high = custom_preamp_high
        self.custom_preamp_low = custom_preamp_low
        self.custom_sp_cabinet = custom_sp_cabinet
        self.custom_sp_color_high = custom_sp_color_high
        self.custom_sp_color_low = custom_sp_color_low
        self.custom_sp_num = custom_sp_num
        self.custom_sp_size = custom_sp_size
        self.custom_type = custom_type
        self.direct_mix = direct_mix
        self.gain_sw = gain_sw
        self.gain = gain
        self.level = level
        self.mic_dis = mic_dis
        self.mic_level = mic_level
        self.mic_pos = mic_pos
        self.mic_type = mic_type
        self.middle = middle
        self.presence = presence
        self.solo_level = solo_level
        self.solo_sw = solo_sw
        self.sp_type = sp_type
        self.t_comp = t_comp
        self.treble = treble