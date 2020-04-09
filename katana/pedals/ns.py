from .pedal import BasePedal
from enum import IntEnum

class NoiseSuppressorType(IntEnum):
    DEFAULT = 0

class NoiseSuppressor(BasePedal):

    CHAIN_POS = [13]

    def __init__(self,
                _type: NoiseSuppressorType = NoiseSuppressorType.DEFAULT,
                on: bool = True,
                detect: int = 0,
                release: int = 30,
                threshold: int = 30,
                **kwargs
    ):
        super().__init__('ns1', on)
        self.type = _type
        self.detect = detect
        self.release = release
        self.threshold = threshold