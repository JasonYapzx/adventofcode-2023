import os
import collections

directions = [-1, 0, 1]

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_dir, 'inputs.txt')

    print("Attempting to open:", input_file_path)

    with open(input_file_path, 'r') as file:
        schema_data = file.read().splitlines()

    print(schema_data)

    part1 = 0

    for x, line in enumerate(schema_data):
        n = 0
        counts = False

        for y, char in enumerate(line):
            if char.isdigit():
                n = n*10 + int(char)
                for i in directions:
                    for j in directions:
                        try:
                            symbol = schema_data[x+i][y+j]
                            if symbol != '.' and not symbol.isdigit():
                                counts = True
                        except IndexError:
                            continue # ignore oob
            if not char.isdigit() or y == len(line) - 1:
                if counts:
                    part1 += n
                    counts = False
                n = 0

    print(part1)



if __name__ == "__main__":
     main()