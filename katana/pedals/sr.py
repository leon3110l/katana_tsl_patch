from .pedal import BasePedal
from enum import IntEnum

class SendReturnType(IntEnum):
    DEFAULT = 0

class SendReturn(BasePedal):

    CHAIN_POS = [1]

    def __init__(self,
                _type: SendReturnType = SendReturnType.DEFAULT,
                on: bool = True,
                adjust: int = 0,
                mode: int = 0,
                position: int = 0,
                return_level: int = 50,
                send_level: int = 50
    ):
        super().__init__('send_return', on)
        self.type = _type
        self.adjust = adjust
        self.mode = mode
        self.position = position
        self.return_level = return_level
        self.send_level = send_level