from skrplt.pve import datamaker as dm
from skrplt.pve import plotmaker as pm
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
    pm.create_score_graph(dataset, utils.colossi)
    pm.create_group_amount_graph(dataset, utils.colossi)
    pm.create_score_graph(dataset, utils.titans)
    pm.create_group_amount_graph(dataset, utils.titans)
