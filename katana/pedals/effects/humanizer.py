from enum import IntEnum

from ..pedal import FXPedal, FXType

class RingModulateType(IntEnum):
    DEFAULT = 1
    PICKING = 0
    AUTO = 1

class RingModulate(FXPedal):

    FX_TYPE = FXType.HUMANIZER

    def __init__(self,
                _type : RingModulateType = RingModulateType.DEFAULT,
                depth: int = 100,
                level: int = 100,
                manual: int = 50,
                rate: int = 80,
                sens: int = 50,
                vowel1: int = 0,
                vowel2: int = 2,
                **kwargs
    ):
        super().__init__('humanizer')
        self.mode = _type
        self.depth = depth
        self.level = level
        self.manual = manual
        self.rate = rate
        self.sens = sens
        self.vowel1 = vowel1
        self.vowel2 = vowel2