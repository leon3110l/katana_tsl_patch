from enum import IntEnum

from ..pedal import FXPedal, FXType

class AcousticProcessorType(IntEnum):
    DEFAULT = 1
    SMALL = 0
    MEDIUM = 1
    BRIGHT = 2
    POWER = 3

class AcousticProcessor(FXPedal):

    FX_TYPE = FXType.ACU_PROCESSOR

    def __init__(self,
                _type : AcousticProcessorType = AcousticProcessorType.DEFAULT,
                bass: int = 50,
                level: int = 50,
                middle_freq: int = 16,
                middle: int = 50,
                presence: int = 50,
                treble: int = 50,
                **kwargs
    ):
        super().__init__('ac_processor')
        self.type = _type
        self.bass = bass
        self.level = level
        self.middle_freq = middle_freq
        self.middle = middle
        self.presence = presence
        self.treble = treble
        