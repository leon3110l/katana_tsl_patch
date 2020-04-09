from enum import IntEnum

from ..pedal import FXPedal, FXType

class ToneModifyType(IntEnum):
    DEFAULT = 0
    FAT = 0
    PRESENCE = 1
    MILD = 2
    TIGHT = 3
    ENHANCE = 4
    RESONATOR_1 = 5
    RESONATOR_2 = 6
    RESONATOR_3 = 7

class ToneModify(FXPedal):

    FX_TYPE = FXType.TONE_MODIFY

    def __init__(self,
                _type : ToneModifyType = ToneModifyType.DEFAULT,
                high: int = 50,
                level: int = 50,
                low: int = 50,
                reso: int = 50,
                **kwargs
    ):
        super().__init__('tone_modify')
        self.type = _type
        self.high = high
        self.level = level
        self.low = low
        self.reso = reso