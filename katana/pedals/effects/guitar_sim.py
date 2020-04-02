from enum import IntEnum

from ..pedal import FXPedal, FXType

class GuitarSimType(IntEnum):
    DEFAULT = 0
    SINGLE_TO_HUMBUCKER = 0
    HUMBUCKER_TO_SINGLE = 1
    HUMBUCKER_TO_SINGLE_HALF_TONE = 2
    SINGLE_TO_ACOUSTIC_HOLLOW = 3
    HUMBUCKER_TO_ACOUSTIC_HOLLOW = 4
    SINGLE_TO_ACOUSTIC = 5
    HUMBUCKER_TO_ACOUSTIC = 6
    PIEZO_TO_ACOUSTIC = 7

class GuitarSim(FXPedal):

    FX_TYPE = FXType.GUITAR_SIM

    def __init__(self,
                _type : GuitarSimType = GuitarSimType.DEFAULT,
                body: int = 50,
                high: int = 50,
                level: int = 50,
                low: int = 50,
    ):
        super().__init__('guitar_sim')
        self.type = _type
        self.body = body
        self.high = high
        self.level = level
        self.low = low