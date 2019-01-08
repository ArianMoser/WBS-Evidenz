import csv
import argparse
import os.path
from pathlib import Path

def main():
    print("Main")

    parser = argparse.ArgumentParser(description="Do something lol")
    parser.add_argument("input", help="input file")
    args = parser.parse_args()
    print("Given argument:", args.input)
    input_file = Path(args.input)

    if input_file.is_file():
        print("Given path is valid")
        #tact = []
        speaking_rate = []
        avg_pitch = []
        sound_intensity = []


        with open(input_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                speaking_rate.append(row[1])
                avg_pitch.append(row[2])
                sound_intensity.append(row[3])
            for el in speaking_rate:
                print(el)
    else:
        print("Given path is invalid")
    
    


if __name__ == "__main__":
    main()
