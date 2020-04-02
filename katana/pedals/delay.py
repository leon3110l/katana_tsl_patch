from .pedal import BasePedal
from enum import IntEnum

class DelayType(IntEnum):
    DEFAULT = 0
    DIGITAL = 0
    SINGLE = 0
    PAN = 1
    STEREO = 2
    DUAL_SERIES = 3
    DUAL_PARALLEL = 4
    DUAL_LR = 5
    REVERSE = 6
    ANALOG = 7
    TAPE_ECHO = 8
    MODULATE = 9
    SDE_3000 = 10

class Delay(BasePedal):

    CHAIN_POS = [7, 8, 8]

    def __init__(self,
                _type: DelayType = DelayType.DEFAULT,
                on: bool = True,
                d1_f_back: int = 20,
                d1_hi_cut: int = 14,
                d1_level: int = 50,
                d1_time_h: int = 0,
                d1_time_l: int = 100,
                d1_time: int = 100,
                d2_f_back: int = 20,
                d2_hi_cut: int = 14,
                d2_level: int = 50,
                d2_time_h: int = 3,
                d2_time_l: int = 16,
                d2_time: int = 400,
                delay_time_h: int = 1,
                delay_time_l: int = 48,
                delay_time: int = 176,
                direct_mix: int = 100,
                effect_level: int = 0,
                f_back: int = 35,
                high_cut: int = 12,
                mod_depth: int = 50,
                mod_rate: int = 40,
                tap_time: int = 50,
                vtg_effect_phase: int = 0,
                vtg_feedback_phase: int = 0,
                vtg_filter: int = 0,
                vtg_lpf: int = 0,
                vtg_mod_sw: int = 0
    ):
        super().__init__('delay', on)
        self.type = _type
        self.d1_f_back = d1_f_back
        self.d1_hi_cut = d1_hi_cut
        self.d1_level = d1_level
        self.d1_time_h = d1_time_h
        self.d1_time_l = d1_time_l
        self.d1_time = d1_time
        self.d2_f_back = d2_f_back
        self.d2_hi_cut = d2_hi_cut
        self.d2_level = d2_level
        self.d2_time_h = d2_time_h
        self.d2_time_l = d2_time_l
        self.d2_time = d2_time
        self.delay_time_h = delay_time_h
        self.delay_time_l = delay_time_l
        self.delay_time = delay_time
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.f_back = f_back
        self.high_cut = high_cut
        self.mod_depth = mod_depth
        self.mod_rate = mod_rate
        self.tap_time = tap_time
        self.vtg_effect_phase = vtg_effect_phase
        self.vtg_feedback_phase = vtg_feedback_phase
        self.vtg_filter = vtg_filter
        self.vtg_lpf = vtg_lpf
        self.vtg_mod_sw = vtg_mod_sw