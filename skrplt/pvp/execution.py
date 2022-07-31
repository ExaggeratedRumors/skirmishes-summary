from skrplt.pvp import datamaker as dm
from skrplt.pvp import plotmaker as pm
from skrplt import utils


def execute(raw_data):
    size = len(raw_data)
    print(f"#### Read {size} samples ####")
    print("#### Cleanup data ####")
    dataset = dm.cleanup_data(raw_data)

    print(f"#### Removed {size - len(dataset)} samples ####")
    dataset = dm.create_labeled_dataset(dataset)

    print("#### Filter servers ####")
    size = len(dataset)
    dataset = dm.filter_servers(dataset)
    print(f"#### Removed {size - len(dataset)} samples ####")

    for prof in utils.target_profession:
        print(f"#### Create output for {prof} ####")
        pm.create_result_graph(dataset, prof)
