# D3plotReader
from lsreader import D3plotReader, DataType as dt

d3plot_path = "E:\\ls_dyna\\paper6_bridge_rock_avalanche\\bridge_failure_DEM16000\\d3plot"
dr = D3plotReader(d3plot_path)

shell_stress = dr.get_data(dt.D3P_SHELL_STRESS, ist=0, ipt=1)
print(shell_stress[0].x())

shell_eps = dr.get_data(dt.D3P_SHELL_EFFECTIVE_PLASTIC_STRAIN, ist=0, ipt=1)
print(shell_eps[0])

thickness = dr.get_data(dt.D3P_SHELL_THICKNESS, ist=11)
print(thickness[0])

num_solid_element = dr.get_data(dt.D3P_NUM_SOLID)
print(num_solid_element)

# Get d3plot data by part
num_solid_pid_4 = dr.get_data(dt.D3P_NUM_SOLID, ipart_user=4)


solid_stress_pid_4 = dr.get_data(dt.D3P_SOLID_STRESS, ist=4, ipt=0, ipart_user=4)

# Get data by part set
#num_beams = dr.get_data(dt.D3P_NUM_BEAM, ipartset_user=[1])

# Get numpy array(numpy is required to be installed, using "pip install numpy")
shell_stress = dr.get_data(dt.D3P_SHELL_STRESS, ist=0, ipt=1, ask_for_numpy_array=True)
print(shell_stress)
