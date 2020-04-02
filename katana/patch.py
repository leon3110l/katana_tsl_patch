from typing import List
from .pedals.pedal import BasePedal, FXPedal
from .pedals.delay import Delay
from .pedals.fx import FX
from importlib import import_module

import json

class Patch():
    def __init__(self, name: str, pedals: List[BasePedal] = []):
        self.name = name
        self.pedals = pedals
        self._fix_pedals()

    def _fix_pedals(self):

        new_pedals = []
        for pedal in self.pedals:
            if(isinstance(pedal, FXPedal)):
                new_pedals.append(FX(pedal))
            elif(not isinstance(pedal, BasePedal)):
                raise TypeError(pedal)
            else:
                new_pedals.append(pedal)
        self.pedals = new_pedals


        if(len(self.pedals) > 12):
            raise Exception('too many pedals given')
        if(len(self.pedals) < 12):
            # fix the amount by adding pedals that are turned off
            pedal_amount = {
                "katana.pedals.wah.Wah": 0,
                "katana.pedals.booster.Booster": 0,
                "katana.pedals.fx.FX": 0,
                "katana.pedals.ns.NoiseSuppressor": 0,
                "katana.pedals.volume.Volume": 0,
                "katana.pedals.amp.Amp": 0,
                "katana.pedals.eq.EQ": 0,
                "katana.pedals.sr.SendReturn": 0,
                "katana.pedals.delay.Delay": 0,
                "katana.pedals.reverb.Reverb": 0
            }
            for pedal in self.pedals:
                pedal_type = type(pedal).__module__ + '.' + type(pedal).__name__

                pedal_amount[pedal_type] += 1
            for cp_name, amount in pedal_amount.items():
                if(amount == 0):
                    if(cp_name == 'katana.pedals.amp.Amp'):
                        self._add_missing_pedal(cp_name, on=True)
                    else:
                        self._add_missing_pedal(cp_name)
                if((cp_name == 'katana.pedals.delay.Delay' or cp_name == 'katana.pedals.fx.FX') and amount < 2):
                    self._add_missing_pedal(cp_name)
            
        self._fix_num_pedals()

    def _add_missing_pedal(self, cp_name: str, on: bool=False):
        cp_split = cp_name.split('.')
        c_name = cp_split.pop()
        p_name = '.'.join(cp_split)
        module = import_module(p_name)
        target_class = getattr(module, c_name)
        self.pedals.append(target_class(on=on))

    def _fix_num_pedals(self):
        delay_count = 0
        fx_count = 1
        for pedal in self.pedals:
            
            # there can be two of these pedals
            if(isinstance(pedal, Delay)):
                pedal._num = delay_count
                delay_count += 2
            if(isinstance(pedal, FX)):
                pedal._num = fx_count
                fx_count += 1

    def _get_chain_positions(self):
        out = {}
        for pos in range(2, 14):
            out['fx_chain_position' + str(pos)] = self.pedals[pos-2].get_chain_index()

        return out

    def get_pedal_params(self):
        out = {}

        for value in self.pedals:
            out = {**out, **value.to_dict()}
        
        return out

    def to_tsl(self):

        with open('katana/clean_patch.tsl') as tsl_raw:
            tsl = json.load(tsl_raw)
            tsl['patchList']['params'] = self.get_pedal_params()

            tsl['patchList']['params'] = { **tsl['patchList']['params_always_include'], **tsl['patchList']['params'], **self._get_chain_positions() }
            del tsl['patchList']['params_always_include']

        return tsl

    def save(self, file: str):
        with open(file, 'w') as file:
            file.write(json.dumps(self.to_tsl(), indent=4))
            file.close()