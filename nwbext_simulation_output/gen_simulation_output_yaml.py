from pynwb.spec import NWBDatasetSpec, NWBNamespaceBuilder, NWBGroupSpec


name = 'simulation_output'
ns_path = name + '.namespace.yaml'
ext_source = name + '.extensions.yaml'


# Continuous data for cell compartments
datasets = [
    NWBDatasetSpec(doc='list of cell ids',
                   dtype='uint32',
                   shape=(None,),
                   name='id',
                   quantity='?',
                   dims=('cells',)),
    NWBDatasetSpec(doc='index pointer',
                   dtype='uint64',
                   shape=(None,),
                   name='index_pointer',
                   dims=('cells',)),
    NWBDatasetSpec(doc='cell compartment ids corresponding to a given '
                       'column in the data',
                   dtype='uint32',
                   shape=(None,),
                   name='element_id',
                   dims=('compartments',)),
    NWBDatasetSpec(doc='relative position of recording within a given '
                       'cell',
                   dtype='float',
                   shape=(None, None),
                   name='compartment_position',
                   dims=('compartments', 'position'))]

cont_data = NWBGroupSpec(doc='Stores continuous data in cell compartments',
                         datasets=datasets,
                         neurodata_type_inc='TimeSeries',
                         neurodata_type_def='CompartmentSeries')

# Export
ns_builder = NWBNamespaceBuilder(name + ' extensions', name)
for spec in [cont_data]:
    ns_builder.add_spec(ext_source, spec)
ns_builder.export(ns_path)