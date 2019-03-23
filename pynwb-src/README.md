# nwbext_simulation_output: An extension for output data of large-scale simulations
 Developed in collaboration between the Soltesz lab and the Allen Institute during [NWB Hackathon #4](https://github.com/NeurodataWithoutBorders/nwb_hackathons/tree/master/HCK04_2018_Seattle/Projects/NetworkOutput) by Ben Dichter*, Kael Dai*, Aaron Milstein, Yazan Billeh, Andrew Tritt, Jean-Christophe Fillion-Robin, Anton Akhipov, Oliver Ruebel, Nicholas Cain, Kristofer Bouchard, and Ivan Soltesz

This extension defines a single NWB data type, `CompartmentSeries`, that allows you to store continuous data (e.g. membrane potential) from many compartments of many cells in a scalable way. 

![Image of CompartmentSeries](../docs/source/_static/multicompartment_schema_1.png)

This structure stores an arbitrarily large number of cells and cellular compartments with 5 datasets. It can scale to a million or more neurons, and enables efficient parallel read and write. It is designed to handle NEURON output data and to easily interface with the SONATA format.

## Guide
#### installation
```
pip install git+https://github.com/bendichter/simulation_output.git
```

#### usage
```python
from pynwb import NWBHDF5IO, NWBFile
from datetime import datetime
from nwbext_simulation_output import CompartmentSeries, Compartments
import numpy as np


compartments = Compartments()
compartments.add_row(number=[0, 1, 2, 3, 4], position=[0.1, 0.2, 0.3, 0.4, 0.5])
compartments.add_row(number=[0], position=[np.nan])
cs = CompartmentSeries('membrane_potential', np.random.randn(10, 6),
                       compartments=compartments,
                       unit='V', rate=100.)
nwbfile = NWBFile('description', 'id', datetime.now().astimezone())
nwbfile.add_acquisition(compartments)
nwbfile.add_acquisition(cs)

with NWBHDF5IO('test_compartment_series.nwb', 'w') as io:
    io.write(nwbfile)
```


## Talks
Ben Dichter*, Kael Dai*, Aaron Milstein, Yazan Billeh, Andrew Tritt, Jean-Christophe Fillion-Robin, Anton Akhipov, Oliver Ruebel, Nicholas Cain, Kristofer Bouchard, Ivan Soltesz. NWB extension for storing results of large-scale neural network simulations. NeuroInformatics. Montreal, Canada (2018). [video](https://www.youtube.com/watch?v=uuYQW0EE2GY).
