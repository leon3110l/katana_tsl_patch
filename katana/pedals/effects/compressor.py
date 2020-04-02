from enum import IntEnum

from ..pedal import FXPedal, FXType

class CompressorType(IntEnum):
    DEFAULT = 0
    BOSS_CS_3 = 0
    HI_BAND = 1
    LIGHT = 2
    MXR_DYNACOMP = 3
    ORANGE_SQUEEZER = 4
    FAT = 5
    MILD = 6

class Compressor(FXPedal):

    FX_TYPE = FXType.COMPRESSOR

    def __init__(self,
                _type : CompressorType = CompressorType.DEFAULT,
                attack: int = 50,
                level: int = 50,
                sustain: int = 50,
                tone: int = 50,
    ):
        super().__init__('comp')
        self.type = _type
        self.attack = attack
        self.level = level
        self.sustain = sustain
        self.tone = tone