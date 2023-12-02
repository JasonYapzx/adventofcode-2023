import os
import re

mapping = {
    'one' : 'o1e',    'two' : 't2o',    'three' : 'thr3e',
    'four': 'fo4r',   'five': 'fi5e',   'six': 's6x',
    'seven': 'se7en', 'eight': 'ei8ht', 'nine':'ni9e'}

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(script_dir, 'input.txt')

    print("Attempting to open:", input_file_path)

    with open(input_file_path, 'r') as file:
        input_list = file.read().splitlines()

    sum = 0

    for line in input_list:
        sum = sum + getCalibration(line)

    print(sum)

def getCalibration(line):
    for key, val in mapping.items():
        line = line.replace(key, val)

    digits = re.sub('\D', '', line)
    return int(digits[0] + digits[-1])




if __name__ == "__main__":
     main()