import csv
import sys
import itertools

import skrplt.utils as utils
import skrplt.pvp.datamaker as dm
import skrplt.pvp.plotmaker as pm

# Read data from first argue
filename = sys.argv[1]
print("#### Open csv file ####")
if not filename.__contains__(".csv"):
    filename += ".csv"
file = open(filename, encoding='UTF-8')
csv_reader = csv.reader(file)
raw_data = []
for row in itertools.islice(csv_reader, utils.sample_size):
    raw_data.append(row)
size = len(raw_data)

print(f"#### Read {size} samples ####")
print("#### Cleanup data ####")
dataset = dm.cleanup_data(raw_data)

print(f"#### Removed {size - len(dataset)} samples ####")
dataset = dm.create_labeled_dataset(dataset)
file.close()

print("#### Filter servers ####")
size = len(dataset)
dataset = dm.filter_servers(dataset)
print(f"#### Removed {size - len(dataset)} samples ####")

for prof in utils.target_profession:
    print(f"#### Create output for {prof} ####")
    pm.create_bar_graph(dataset, prof)

# TODO:
#   - read hiperparameters from Utils file (range, prof, server)
#   - create windows visualization for plots
#   - create pdf conversion for plots
#   - create filters for hiperparameters
