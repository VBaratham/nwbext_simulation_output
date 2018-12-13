# nwbext_simulation_output: An extension the output data of large-scale simulations
 Developed in collaboration between the Soltesz lab and the Allen Institute.

This extension defines a single NWB data type, `CompartmentSeries`, that allows you to store continuous data (e.g. membrane potential) from many compartments of many cells in a scalable way. 

![Image of CompartmentSeries](multicompartment_schema_1.png)

This structure stores an arbitrarily large number of cells and cellular compartments with 5 datasets. It can scale to a million or more neurons, and enables efficient parallel read and write. It is designed to handle NEURON output data and to easily interface with the SONATA format.

## Usage
### python
to install:
```
pip install git+https://github.com/bendichter/simulation_output.git
```

to use:
```python
import pynwb
from nwbext_simulation_output.simulation_output import CompartmentSeries

nwbfile = pynwb.NWBFile(...)

...

membrane_potential = CompartmentSeries(name='membrane_potential',
                                       id=[1, 2, 3],
                                       index_pointer=[1, 2, 3],
                                       data=[[1., 2., 4.], [1., 2., 4.]],
                                       element_id=[0, 0, 0],
                                       compartment_position=[1., 1., 1.],
                                       unit='µV',
                                       rate=100.)
```

### MATLAB
to install:
```matlab
generateExtension('/path/to/nwbext_simulation_output/nwbext_simulation_output/nwbext_simulation_output.namespace.yaml');
```

to use:

```matlab
membrane_potential = types.simulation_output.CompartmentSeries('name', membrane_potential',...
    'id', [1, 2, 3], ...
    'index_pointer', [1, 2, 3], ...
    'data', [[1., 2., 4.], [1., 2., 4.]]', ...
    'element_id, [0, 0, 0], ...
    'compartment_position', [1., 1., 1.], ...
    'unit, 'µV', ...
    'rate', 100.)
```
