from enum import IntEnum

from .. import FXPedal, FXType

class RingModulateType(IntEnum):
    DEFAULT = 0
    NORMAL = 0
    INTELLIGENT = 1

class RingModulate(FXPedal):

    FX_TYPE = FXType.RING_MODULATE

    def __init__(self,
                _type : RingModulateType = RingModulateType.DEFAULT,
                direct_mix: int = 100,
                effect_level: int = 100,
                freq: int = 50,
                **kwargs
    ):
        super().__init__('ring_mod')
        self.mode = _type
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.freq = freq