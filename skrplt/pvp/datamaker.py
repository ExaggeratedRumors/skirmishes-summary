import math
import re
import pandas
import skrplt.utils as utils


def cleanup_data(data):
    new_data = []
    for sample in data:
        # remove group fights
        if sample[6].count('PID') > 2 or sample[7].count('PID') > 2:
            continue
        # clean server-name
        sample[0] = re.sub(r'mgame_pl_', '', sample[0])
        # split level and profession
        lvl_prof = re.search(r'\(.*?\)', sample[6]).group()
        sample[6] = int(''.join(s for s in lvl_prof if s.isdigit()))
        sample.append(''.join(s for s in lvl_prof if s.isalpha()))
        lvl_prof = re.search(r'\(.*?\)', sample[7]).group()
        sample[7] = int(''.join(s for s in lvl_prof if s.isdigit()))
        sample.append(''.join(s for s in lvl_prof if s.isalpha()))
        # remove mirror fights
        if sample[8] == sample[9]:
            continue
        # remove high advantage and low level
        legal_advantage = min(utils.max_advantage,
                              max(utils.min_advantage, int(int(sample[6]) * utils.advantage_factor)))
        if abs(sample[6] - sample[7]) > legal_advantage or sample[6] < utils.min_level or sample[7] < utils.min_level:
            continue
        sample[6] = int(10 * math.floor(sample[6] / 10)) if sample[6] < utils.max_level else utils.max_level
        sample[7] = int(10 * math.floor(sample[7] / 10)) if sample[7] < utils.max_level else utils.max_level
        new_data.append(sample)
    return new_data


def create_labeled_dataset(data):
    return pandas.DataFrame({
        'server': [row[0] for row in data],
        'result': [row[5] for row in data],
        'first_player_lvl': [row[6] for row in data],
        'first_player_prof': [row[8] for row in data],
        'second_player_lvl': [row[7] for row in data],
        'second_player_prof': [row[9] for row in data]
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


def filter_profession(data, profession):
    dataset = data[data.first_player_prof == profession].append(data[data.second_player_prof == profession])
    result = {
        "w": {x: [0, 0] for x in range(utils.min_level, utils.max_level + 1, 10)},
        "b": {x: [0, 0] for x in range(utils.min_level, utils.max_level + 1, 10)},
        "p": {x: [0, 0] for x in range(utils.min_level, utils.max_level + 1, 10)},
        "m": {x: [0, 0] for x in range(utils.min_level, utils.max_level + 1, 10)},
        "t": {x: [0, 0] for x in range(utils.min_level, utils.max_level + 1, 10)},
        "h": {x: [0, 0] for x in range(utils.min_level, utils.max_level + 1, 10)}
    }
    result.pop(profession)
    for sample in dataset.values:
        if sample[3] == profession:
            if not sample[2] in result[sample[5]]:
                result[sample[5]][sample[2]] = [0, 0]
            result[sample[5]][sample[2]][0] += (2 - int(sample[1]))
            result[sample[5]][sample[2]][1] += 1
        elif sample[5] == profession:
            if not sample[4] in result[sample[3]]:
                result[sample[3]][sample[4]] = [0, 0]
            result[sample[3]][sample[4]][0] += (int(sample[1]) - 1)
            result[sample[3]][sample[4]][1] += 1
    return result
