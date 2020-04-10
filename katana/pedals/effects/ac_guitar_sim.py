from enum import IntEnum

from .. import FXPedal, FXType

class ACGuitarSimType(IntEnum):
    DEFAULT = 0

class ACGuitarSim(FXPedal):

    FX_TYPE = FXType.AC_GUITAR_SIM

    def __init__(self,
                _type : ACGuitarSimType = ACGuitarSimType.DEFAULT,
                body: int = 50,
                high: int = 50,
                level: int = 50,
                low: int = 50,
                **kwargs
    ):
        super().__init__('acsim')
        self.type = _type
        self.body = body
        self.high = high
        self.level = level
        self.low = low