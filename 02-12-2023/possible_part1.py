import os

script_dir = os.path.dirname(os.path.realpath(__file__))
input_file_path = os.path.join(script_dir, 'inputs.txt')

print("Attempting to open:", input_file_path)

with open(input_file_path, 'r') as file:
    games_data = file.read().splitlines()


games_dict = {}
bag = {'red': 12, 'green': 13, 'blue': 14}

for line in games_data:
    game_id, game_data = line.split(':')
    game_id = game_id.split()[1]

    game_data_list = [item.strip() for item in game_data.split(';')]
    game_data_list = [[element.strip() for element in item.split(',')] for item in game_data_list]

    games_dict[game_id.strip()] = game_data_list

res = 0

for game_id, cubes_combinations in games_dict.items():
    possible = True
    for games in cubes_combinations:
        for cubes in games:
            amount, color = cubes.split()
            
            if int(amount) > bag[color]:
                possible = False
                break
        if not possible:
            break
    if possible:
        res += int(game_id)

print(res)