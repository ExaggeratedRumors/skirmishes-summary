import csv
import sys
import itertools

import skrplt.datamaker as dm
import skrplt.plotmaker as pm

sample_size = 1000000

# Read data from first argue
filename = sys.argv[1]
print("#### Read file ####")
if not filename.__contains__(".csv"):
    filename += ".csv"
file = open(filename, encoding='UTF-8')
csv_reader = csv.reader(file)
raw_data = []
for row in itertools.islice(csv_reader, sample_size):
    raw_data.append(row)

print("#### Cleanup data ####")
dataset = dm.cleanup_data(raw_data)
print(f"#### Read {len(dataset)} samples ####")
dataset = dm.create_labeled_dataset(dataset)
file.close()

print("#### Create output ####")
pm.create_bar_graph(dataset, "t")

# TODO:
#   - read hiperparameters from Utils file (range, prof, server)
#   - create windows visualization for plots
#   - create pdf conversion for plots
#   - create filters for hiperparameters
