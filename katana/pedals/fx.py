from .pedal import BasePedal, FXPedal, FXType
from .effects.tremolo import Tremolo

class FX(BasePedal):

    CHAIN_POS = [5, 5, 6] # index starts at 1

    def __init__(self,
                pedal: FXPedal = Tremolo(),
                _type: FXType = FXType.DEFAULT,
                on: bool = True,
                **kwargs
    ):
        super().__init__('fx', on)
        self.fx_type = _type
        self.set_pedal(pedal)

    def set_pedal(self, pedal: FXPedal):
        if(not pedal.FX_TYPE or not isinstance(pedal, FXPedal)):
            raise TypeError(pedal)
        
        self._pedal = pedal
        self.fx_type = pedal.FX_TYPE

    def to_dict(self):
        out = {}

        for key, value in self._pedal.to_dict().items():
            out[self._get_tsl_string() + '_' + key] = value
        
        out = {**out, **super().to_dict()}

        return out