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


    part2 = 0

    gears = collections.defaultdict(list)
    for x, line in enumerate(schema_data):
        n = 0
        counts, gear = False, False

        for y, char in enumerate(line):
            if char.isdigit():
                n = n*10 + int(char)
                for i in directions:
                    for j in directions:
                        try:
                            symbol = schema_data[x+i][y+j]
                            if symbol != '.' and not symbol.isdigit():
                                counts = True
                                if symbol == "*":
                                    gear = (x+i, y+j)
                        except IndexError:
                            continue # ignore oob
            if not char.isdigit() or y == len(line) - 1:
                if counts:
                    counts = False
                if gear:
                    gears[gear].append(n)
                    if len(gears[gear]) == 2:
                        part2 += n * gears[gear][0]
                    gear = False
                n = 0

    print(part2)



if __name__ == "__main__":
     main()