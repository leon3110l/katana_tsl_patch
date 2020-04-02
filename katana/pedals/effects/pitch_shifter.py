from enum import IntEnum

from ..pedal import FXPedal, FXType

class PitchShifterType(IntEnum):
    DEFAULT = 0
    ONE_VOICE = 0
    TWO_VOICES = 1

class PitchShifter(FXPedal):

    FX_TYPE = FXType.PITCH_SHIFTER

    def __init__(self,
                _type : PitchShifterType = PitchShifterType.DEFAULT,
                direct_mix: int = 100,
                ps1f_back: int = 0,
                ps1fine: int = 60,
                ps1level: int = 70,
                ps1mode: int = 1,
                ps1pitch: int = 24,
                ps1pre_dly_h: int = 0,
                ps1pre_dly_l: int = 0,
                ps1pre_dly: int = 0,
                ps2fine: int = 40,
                ps2level: int = 70,
                ps2mode: int = 1,
                ps2pitch: int = 24,
                ps2pre_dly_h: int = 0,
                ps2pre_dly_l: int = 0,
                ps2pre_dly: int = 0,
    ):
        super().__init__('pitch_shifter')
        self.voice = _type
        self.direct_mix = direct_mix
        self.ps1f_back = ps1f_back
        self.ps1fine = ps1fine
        self.ps1level = ps1level
        self.ps1mode = ps1mode
        self.ps1pitch = ps1pitch
        self.ps1pre_dly_h = ps1pre_dly_h
        self.ps1pre_dly_l = ps1pre_dly_l
        self.ps1pre_dly = ps1pre_dly
        self.ps2fine = ps2fine
        self.ps2level = ps2level
        self.ps2mode = ps2mode
        self.ps2pitch = ps2pitch
        self.ps2pre_dly_h = ps2pre_dly_h
        self.ps2pre_dly_l = ps2pre_dly_l
        self.ps2pre_dly = ps2pre_dly