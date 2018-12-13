from pynwb import load_namespaces, get_class, NWBHDF5IO, NWBFile
from datetime import datetime

import numpy as np

load_namespaces('simulation_output.namespace.yaml')
CompartmentSeries = get_class('CompartmentSeries', 'simulation_output')
membrane_potential = CompartmentSeries(name='membrane_potential',
                                       gid=[1, 2, 3],
                                       index_pointer=[1, 2, 3],
                                       data=[[1., 2., 4.], [1., 2., 4.]],
                                       timestamps=np.arange(2),
                                       element_id=[0, 0, 0],
                                       compartment_position=[1., 1., 1.],
                                       unit='µV')

nwbfile = NWBFile(session_description='session_description',
                  identifier='identifier', session_start_time=datetime.now().astimezone(),)

module = nwbfile.create_processing_module(name='membrane_potential', description='description')
module.add_container(membrane_potential)

with NWBHDF5IO('mem_potential_test.nwb', mode='w') as io:
    io.write(nwbfile)

with NWBHDF5IO('mem_potential_test.nwb', mode='r') as io:
    io.read()
