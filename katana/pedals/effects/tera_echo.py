from enum import IntEnum

from ..pedal import FXPedal, FXType

class TeraEchoType(IntEnum):
    DEFAULT = 1
    MONO = 0
    STEREO_1 = 1
    STEREO_2 = 2

# TODO: this starts with prm_ for some reason
# "prm_fx2_teraecho_direct_mix": 100,
# "prm_fx2_teraecho_effect_level": 50,
# "prm_fx2_teraecho_feedback": 50,
# "prm_fx2_teraecho_hold": 0,
# "prm_fx2_teraecho_time": 50,
# "prm_fx2_teraecho_tone": 50,

class TeraEcho(FXPedal):

    FX_TYPE = FXType.TERA_ECHO

    def __init__(self,
                _type : TeraEchoType = TeraEchoType.DEFAULT,
                direct_mix: int = 100,
                effect_level: int = 50,
                feedback: int = 50,
                hold: int = 0,
                time: int = 50,
                tone: int = 50,
    ):
        super().__init__('teraecho')
        self.mode = _type
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.feedback = feedback
        self.hold = hold
        self.time = time
        self.tone = tone