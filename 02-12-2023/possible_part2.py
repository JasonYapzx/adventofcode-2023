import os


def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_dir, 'inputs.txt')

    print("Attempting to open:", input_file_path)

    with open(input_file_path, 'r') as file:
        games_data = file.read().splitlines()


    games_dict = {}

    for line in games_data:
        game_id, game_data = line.split(':')
        game_id = game_id.split()[1]

        game_data_list = [item.strip() for item in game_data.split(';')]
        game_data_list = [[element.strip() for element in item.split(',')] for item in game_data_list]

        games_dict[game_id.strip()] = game_data_list

    res = 0

    for game_id, cubes_combinations in games_dict.items():
        res += minimum_cubes(cubes_combinations)

    print(res)

def minimum_cubes(cubes_combinations):
    bag = {'red': 0, 'green': 0, 'blue': 0}

    for games in cubes_combinations:
        for cubes in games:
            amount, color = cubes.split()
            amount = int(amount)

            bag[color] = max(bag[color], amount)

    res = 1
    for amount in bag.values():
        res *= amount
    
    return res


if __name__ == "__main__":
     main()