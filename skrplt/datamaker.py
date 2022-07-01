import re
import pandas

min_advantage = 3
max_advantage = 13
advantage_factor = 0.05  # in common player A can be 5% higher in level than player B


def cleanup_data(data):
    for sample in data[:]:
        # remove group fights
        if sample[6].count('PID') > 2 or sample[7].count('PID') > 2:
            data.remove(sample)
            continue
        # clean server-name
        sample[0] = re.sub(r'mgame_pl_', '', sample[0])
        # split level and profession
        lvl_prof = re.search(r'\(.*?\)', sample[6]).group()
        sample[6] = ''.join(s for s in lvl_prof if s.isdigit())
        sample.append(''.join(s for s in lvl_prof if s.isalpha()))
        lvl_prof = re.search(r'\(.*?\)', sample[7]).group()
        sample[7] = ''.join(s for s in lvl_prof if s.isdigit())
        sample.append(''.join(s for s in lvl_prof if s.isalpha()))
        # remove high advantage
        legal_advantage = min(max_advantage, max(min_advantage, int(int(sample[6]) * advantage_factor)))
        if abs(int(sample[6]) - int(sample[7])) > legal_advantage:
            data.remove(sample)
            continue


def create_filtered_dataset(data):
    return pandas.DataFrame({
        'server': [row[0] for row in data],
        'result': [row[5] for row in data],
        'first_player_lvl': [row[6] for row in data],
        'first_player_prof': [row[8] for row in data],
        'second_player_lvl': [row[7] for row in data],
        'second_player_prof': [row[9] for row in data]
    })
    # dataset = dataset.drop_duplicates()
