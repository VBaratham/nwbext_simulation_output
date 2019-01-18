import os
from pynwb import load_namespaces, get_class

namespace_path = os.path.join(os.path.split(__file__)[0], 'simulation_output.namespace.yaml')

load_namespaces(namespace_path)
CompartmentSeries = get_class('CompartmentSeries', 'simulation_output')
