from enum import IntEnum

from ..pedal import FXPedal, FXType

class HarmonistType(IntEnum):
    DEFAULT = 0
    ONE_VOICE = 0
    TWO_VOICES = 1

class Harmonist(FXPedal):

    FX_TYPE = FXType.HARMONIST

    def __init__(self,
                _type : HarmonistType = HarmonistType.DEFAULT,
                direct_mix: int = 100,
                hr1a: int = 24,
                hr1ab: int = 24,
                hr1b: int = 24,
                hr1bb: int = 24,
                hr1c: int = 24,
                hr1d: int = 24,
                hr1db: int = 24,
                hr1e: int = 24,
                hr1eb: int = 24,
                hr1f_back: int = 0,
                hr1f_s: int = 24,
                hr1f: int = 24,
                hr1g: int = 24,
                hr1harm: int = 12,
                hr1level: int = 70,
                hr1pre_dly_h: int = 0,
                hr1pre_dly_l: int = 0,
                hr1pre_dly: int = 0,
                hr2a: int = 24,
                hr2ab: int = 24,
                hr2b: int = 24,
                hr2bb: int = 24,
                hr2c: int = 24,
                hr2d: int = 24,
                hr2db: int = 24,
                hr2e: int = 24,
                hr2eb: int = 24,
                hr2f_s: int = 24,
                hr2f: int = 24,
                hr2g: int = 24,
                hr2harm: int = 7,
                hr2level: int = 80,
                hr2pre_dly_h: int = 0,
                hr2pre_dly_l: int = 0,
                hr2pre_dly: int = 0,
    ):
        super().__init__('harmonist')
        self.voice = _type
        self.direct_mix = direct_mix
        self.hr1a = hr1a
        self.hr1ab = hr1ab
        self.hr1b = hr1b
        self.hr1bb = hr1bb
        self.hr1c = hr1c
        self.hr1d = hr1d
        self.hr1db = hr1db
        self.hr1e = hr1e
        self.hr1eb = hr1eb
        self.hr1f_back = hr1f_back
        self.hr1f_s = hr1f_s
        self.hr1f = hr1f
        self.hr1g = hr1g
        self.hr1harm = hr1harm
        self.hr1level = hr1level
        self.hr1pre_dly_h = hr1pre_dly_h
        self.hr1pre_dly_l = hr1pre_dly_l
        self.hr1pre_dly = hr1pre_dly
        self.hr2a = hr2a
        self.hr2ab = hr2ab
        self.hr2b = hr2b
        self.hr2bb = hr2bb
        self.hr2c = hr2c
        self.hr2d = hr2d
        self.hr2db = hr2db
        self.hr2e = hr2e
        self.hr2eb = hr2eb
        self.hr2f_s = hr2f_s
        self.hr2f = hr2f
        self.hr2g = hr2g
        self.hr2harm = hr2harm
        self.hr2level = hr2level
        self.hr2pre_dly_h = hr2pre_dly_h
        self.hr2pre_dly_l = hr2pre_dly_l
        self.hr2pre_dly = hr2pre_dly
        