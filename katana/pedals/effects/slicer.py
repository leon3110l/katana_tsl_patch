from enum import IntEnum

from ..pedal import FXPedal, FXType

class SlicerType(IntEnum):
    DEFAULT = 0


class Slicer(FXPedal):

    FX_TYPE = FXType.SLICER

    def __init__(self,
                _type : SlicerType = SlicerType.DEFAULT,
                direct_mix: int = 0,
                effect_level: int = 50,
                pattern: int = 0,
                rate: int = 50,
                trigger_sens: int = 50,
                **kwargs
    ):
        super().__init__('slicer')
        self.type = _type
        self.direct_mix = direct_mix
        self.effect_level = effect_level
        self.pattern = pattern
        self.rate = rate
        self.trigger_sens = trigger_sens