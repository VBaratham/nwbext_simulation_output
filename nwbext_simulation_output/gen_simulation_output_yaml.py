from pynwb.spec import NWBDatasetSpec, NWBNamespaceBuilder, NWBGroupSpec


name = 'simulation_output'
ns_path = name + '.namespace.yaml'
ext_source = name + '.extensions.yaml'


# Continuous data for cell compartments
datasets = [
    NWBDatasetSpec(doc='list of unit ids',
                   dtype='int',
                   shape=(None,),
                   name='unit_id',
                   quantity='?',
                   dims=('cells',)),
    NWBDatasetSpec(neurodata_type_inc='VectorIndex',
                   doc='maps cell to compartments',
                   shape=(None,),
                   name='compartments_index',
                   dims=('cells',)),
    NWBDatasetSpec(neurodata_type_inc='VectorData',
                   doc='cell compartment ids corresponding to a each column in the data',
                   dtype='int',
                   shape=(None,),
                   name='compartments',
                   dims=('compartments',)),
    NWBDatasetSpec(doc='position of recording within a compartment. 0 is close to soma, 1 is other end',
                   dtype='float',
                   shape=(None,),
                   name='compartment_position',
                   dims=('compartments',),
                   quantity='?')]

cont_data = NWBGroupSpec(doc='Stores continuous data in cell compartments',
                         datasets=datasets,
                         neurodata_type_inc='TimeSeries',
                         neurodata_type_def='CompartmentSeries')

# Export
ns_builder = NWBNamespaceBuilder(name + ' extensions', name)
for spec in [cont_data]:
    ns_builder.add_spec(ext_source, spec)
ns_builder.export(ns_path)