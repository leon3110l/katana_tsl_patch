from enum import IntEnum

from ..pedal import FXPedal, FXType

class HeavyOctaveType(IntEnum):
    DEFAULT = 0

class HeavyOctave(FXPedal):

    FX_TYPE = FXType.HEAVY_OCTIVE

    def __init__(self,
                _type : HeavyOctaveType = HeavyOctaveType.DEFAULT,
                _1oct_level: int = 0,
                _2oct_level: int = 0,
                direct_mix: int = 0,
    ):
        super().__init__('heavy_oct')
        self.type = _type
        self['1oct_level'] = _1oct_level
        self['2oct_level'] = _2oct_level
        self.direct_mix = direct_mix
        