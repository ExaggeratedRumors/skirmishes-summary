import math
import re
import pandas
import skrplt.utils as utils


def cleanup_data(data):
    new_data = []
    for sample in data:
        # remove fights with too small group
        if sample[6].count('/PID') < utils.min_group:
            continue
        # remove incorrect samples fights against players
        if sample[7].count('PID') > 0:
            continue
        # remove lvl from NPC name
        sample[7] = re.sub(r' \(.*?\)', '', sample[7])
        # clean server-name
        sample[0] = re.sub(r'mgame_pl_', '', sample[0])
        # change players data to group amount
        group_amount = sample[6].count('/PID')
        sample[6] = str(group_amount)
        new_data.append(sample)
    return new_data


def create_labeled_dataset(data):
    return pandas.DataFrame({
        'server': [row[0] for row in data],
        'result': [row[5] for row in data],
        'group_amount': [row[6] for row in data],
        'NPC_name': [row[7] for row in data]
    })
    # dataset = dataset.drop_duplicates()


def filter_servers(data):
    if utils.server == '0':
        return data
    if utils.server == '1':
        return data[utils.public_servers.__contains__(data.server)]
    if utils.server == '2':
        return data[utils.private_servers.__contains__(data.server)]
    else:
        return data[data.server == utils.server]


def create_npcs_score_label(data, npc_name_array):
    # array: wins, losses, draws
    result = {key: [0, 0, 0] for key in npc_name_array}

    # sum scores
    for sample in data.values:
        if not sample[3] in result:
            continue
        if sample[1] == '1':
            result[sample[3]][0] += 1
        elif sample[1] == '2':
            result[sample[3]][1] += 1
        else:
            result[sample[3]][2] += 1
    return result


def create_group_amount_label(data, npc_name_array):
    # array: wins, losses, draws
    result = {key: [0] * (10 - utils.min_group + 1) for key in npc_name_array}
    # sum scores
    for sample in data.values:
        if not sample[3] in result:
            continue
        result[sample[3]][int(sample[2]) - utils.min_group] += 1
    return result
