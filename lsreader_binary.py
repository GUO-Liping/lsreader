# BinoutReader
from lsreader import BinoutReader, BINOUT_DataType as bdt

binary_path = "E:\\ls_dyna\\paper6_bridge_rock_avalanche\\bridge_failure_DEM16000\\binout"
br = BinoutReader(binary_path)

branches = br.get_data(bdt.BINOUT_BRANCHES)
print(branches)

ids = br.get_data(bdt.BINOUT_NODOUT_IDS)
print(ids)