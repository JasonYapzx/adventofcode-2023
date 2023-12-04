import os
import collections

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_dir, 'inputs.txt')

    print("Attempting to open:", input_file_path)

    with open(input_file_path, 'r') as file:
        scratch_cards = file.read().splitlines()

    res = [1] * len(scratch_cards)

    for line in scratch_cards:
        split_colon = line.split(':')
        card_id = split_colon[0].split()[1].strip()
        winning_numbers = [int(num) for num in split_colon[1].split('|')[0].split()]
        guesses = [int(num) for num in split_colon[1].split('|')[1].split()]

        amount = count_points(winning_numbers, guesses)
        for i in range(int(card_id), int(card_id) + amount):
            res[i] += (res[int(card_id) - 1] * 1)
    
    print(sum(res))


def count_points(winning_numbers, guesses):
    count = 0
    for i in guesses:
        if i in winning_numbers:
            count += 1
    return count


if __name__ == "__main__":
     main()