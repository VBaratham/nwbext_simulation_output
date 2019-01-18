import os

from collections import Iterable

import numpy as np
from pynwb import load_namespaces, register_class, docval, NWBHDF5IO, NWBFile
from pynwb.core import VectorIndex, VectorData
from pynwb.form.utils import popargs
from pynwb import load_namespaces
from pynwb.base import TimeSeries, _default_resolution, _default_conversion

from datetime import datetime

namespace_path = os.path.join(os.path.split(__file__)[0], 'simulation_output.namespace.yaml')

load_namespaces(namespace_path)

# not working yet
# CompartmentSeries = get_class('CompartmentSeries', 'simulation_output')


@register_class('CompartmentSeries', 'simulation_output')
class CompartmentSeries(TimeSeries):
    __nwbfields__ = ('unit_id', 
                     {'name': 'compartments_index', 'child': True},
                     {'name': 'compartments', 'child': True},
                     'compartment_position')

    @docval({'name': 'name', 'type': str, 'doc': 'name'},
            {'name': 'data', 'type': ('array_data', 'data', TimeSeries), 'shape': (None, None),
             'doc': 'The data this TimeSeries dataset stores. Can also store binary data e.g. image frames'},
            {'name': 'unit_id', 'type': ('array_data', 'data'), 'shape': (None,),
             'doc': 'list of unit ids'},
            {'name': 'compartments', 'type': list, 'doc': 'list of list of compartments'},
            {'name': 'unit', 'type': str, 'doc': 'SI unit of measurement'},
            {'name': 'compartment_position', 'type': ('array_data', 'data'), 'shape': (None,),
             'doc': 'position of recording within a compartment. 0 is close to soma, 1 is other end',
             'default': None},
            {'name': 'resolution', 'type': float,
             'doc': 'The smallest meaningful difference (in specified unit) between values in data',
             'default': _default_resolution},
            {'name': 'conversion', 'type': float,
             'doc': 'Scalar to multiply each element by to conver to volts', 'default': _default_conversion},

            {'name': 'timestamps', 'type': ('array_data', 'data', TimeSeries),
             'doc': 'Timestamps for samples stored in data', 'default': None},
            {'name': 'starting_time', 'type': float, 'doc': 'The timestamp of the first sample', 'default': None},
            {'name': 'rate', 'type': float, 'doc': 'Sampling rate in Hz', 'default': None},

            {'name': 'comments', 'type': str,
             'doc': 'Human-readable comments about this TimeSeries dataset', 'default': 'no comments'},
            {'name': 'description', 'type': str,
             'doc': 'Description of this TimeSeries dataset', 'default': 'no description'},
            {'name': 'control', 'type': Iterable,
             'doc': 'Numerical labels that apply to each element in data', 'default': None},
            {'name': 'control_description', 'type': Iterable,
             'doc': 'Description of each control value', 'default': None},
            {'name': 'parent', 'type': 'NWBContainer',
             'doc': 'The parent NWBContainer for this NWBContainer', 'default': None}
            )
    def __init__(self, **kwargs):
        unit_id, compartments = popargs('unit_id', 'compartments', kwargs)
        if 'compartment_position' in kwargs:
            self.compartment_position = popargs('compartment_position', kwargs)

        super(CompartmentSeries, self).__init__(**kwargs)

        # flatten_list
        self.compartments = VectorData(
            'compartments', 'indicates which compartments the data refers to',
            [item for sublist in compartments for item in sublist])
        self.compartments_index = VectorIndex(
            'compartments_index', np.cumsum([len(x) for x in compartments]), target=self.compartments)
        self.unit_id = unit_id

