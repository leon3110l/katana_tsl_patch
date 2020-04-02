from enum import IntEnum

from ..pedal import FXPedal, FXType

class OverToneType(IntEnum):
    DEFAULT = 0

# TODO: this starts with prm_ for some reason
# "prm_fx2_overtone_detune": 50,
# "prm_fx2_overtone_direct_level": 100,
# "prm_fx2_overtone_lower_level": 100,
# "prm_fx2_overtone_tone": 50,
# "prm_fx2_overtone_upper_level": 100,

class OverTone(FXPedal):

    FX_TYPE = FXType.OVER_TONE

    def __init__(self,
                _type : OverToneType = OverToneType.DEFAULT,
                detune: int = 50,
                direct_level: int = 100,
                lower_level: int = 100,
                tone: int = 50,
                upper_level: int = 100,
    ):
        super().__init__('overtone')
        self.type = _type
        self.detune = detune
        self.direct_level = direct_level
        self.lower_level = lower_level
        self.tone = tone
        self.upper_level = upper_level