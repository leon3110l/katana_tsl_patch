from enum import IntEnum

from ..pedal import FXPedal, FXType

class UniVType(IntEnum):
    DEFAULT = 0

class UniV(FXPedal):

    FX_TYPE = FXType.UNI_V

    def __init__(self,
                _type : UniVType = UniVType.DEFAULT,
                depth: int = 60,
                level: int = 100,
                rate: int = 70,
                
    ):
        super().__init__('uni_v')
        self.type = _type
        self.depth = depth
        self.level = level
        self.rate = rate