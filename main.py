"Calculates the statistical evidence of emotions based on voice recordings"

import csv
import argparse
import os.path
from pyds import MassFunction
from enum import Enum
from pathlib import Path

def main():
    "main function"

    print("Main")

    parser = argparse.ArgumentParser(description="Do something lol")
    parser.add_argument("input", help="input file")
    args = parser.parse_args()
    print("Given argument:", args.input)
    input_file = Path(args.input)

    if input_file.is_file():
        print("Given path is valid")
        tacts = []


        with open(input_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader, None)
            for row in reader:
                tacts.append({
                    "id" : row[0],
                    "speaking_rate" : row[1],
                    "avg_pitch" : row[2],
                    "sound_intensity" : row[3]
                    })
            for el_tact in tacts:
                print(el_tact)
            omega = {"su", 'f', 'j', 'a', 'sa', 'd'}
            m1 = MassFunction([({"sa", 'd'}, 0.8), (omega, 0.2)])
            print(m1.bel("sa"))
    else:
        print("Given path is invalid")


if __name__ == "__main__":
    main()
