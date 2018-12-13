from pynwb import load_namespaces, get_class

load_namespaces('simulation_output.namespace.yaml')
CompartmentSeries = get_class('CompartmentSeries', 'simulation_output')
