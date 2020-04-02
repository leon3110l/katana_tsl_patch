from enum import IntEnum

from ..pedal import FXPedal, FXType

class Phaser90EType(IntEnum):
    DEFAULT = 0

class Phaser90E(FXPedal):

    FX_TYPE = FXType.PHASER_90E

    def __init__(self,
                _type : Phaser90EType = Phaser90EType.DEFAULT,
                script: int = 0,
                speed: int = 0,
    ):
        super().__init__('phaser90e')
        self.type = _type
        self.script = script
        self.speed = speed
        