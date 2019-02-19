from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from nwbext_simulation_output import CompartmentSeries, Compartments


compartments = Compartments()
compartments.add_row(number=[0, 1, 2, 3])
compartments.add_row(number=[0, 1, 2])
cs = CompartmentSeries('membrane_potential', [[1., 2., 3.], [1., 2., 3.], [1., 2., 3.]],
                       compartments=compartments,
                       unit='V', rate=100.)
nwbfile = NWBFile('description', 'id', datetime.now().astimezone())
nwbfile.add_acquisition(compartments)
nwbfile.add_acquisition(cs)

with NWBHDF5IO('test_compartment_series.nwb', 'w') as io:
    io.write(nwbfile)

with NWBHDF5IO('test_compartment_series.nwb', mode='r') as io:
    io.read()
