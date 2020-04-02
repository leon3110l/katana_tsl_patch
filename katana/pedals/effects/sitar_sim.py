from enum import IntEnum

from ..pedal import FXPedal, FXType

class SitarSimType(IntEnum):
    DEFAULT = 0
    FIRST_AT_24 = 0
    FIRST_AT_12 = 1
    FIRST_AT_OPEN = 2
    FOURTH_AT_2 = 3


class SitarSim(FXPedal):

    FX_TYPE = FXType.SITAR_SIM

    def __init__(self,
                _type : SitarSimType = SitarSimType.DEFAULT,
                direct_mix: int = 100,
                level: int = 62,
    ):
        super().__init__('octave')
        self.range = _type
        self.direct_mix = direct_mix
        self.level = level