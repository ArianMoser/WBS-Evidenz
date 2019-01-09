"Calculates the statistical evidence of emotions based on voice recordings"

import csv
import argparse
from enum import Enum
from pathlib import Path
from pyds import MassFunction

class Emotion(Enum):
    FEAR = 0
    SURPRISE = 1
    ANGER = 2
    JOY = 3
    DISGUST = 4
    SADNESS = 5

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
                omega = {"su", 'f', 'j', 'a', 'sa', 'd'}
                print(el_tact)

                if float(el_tact["speaking_rate"].replace(",", ".")) < 4:
                    m_1 = MassFunction([({'d', 'sa'}, 0.8), (omega, 0.2)])
                elif(float(el_tact["speaking_rate"].replace(",", ".")) >= 4 and
                     float(el_tact["speaking_rate"].replace(",", ".")) < 5):
                    m_1 = MassFunction([(omega, 1)])
                elif float(el_tact["speaking_rate"].replace(",", ".")) >= 5:
                    m_1 = MassFunction([({'j', 'f', 's', 'a'}, 0.8), (omega, 0.2)])
                else:
                    m_1 = None

                if el_tact["avg_pitch"] == "niedrig" or el_tact["avg_pitch"] == "sehr niedrig":
                    m_2 = MassFunction([({'d', 'sa'}, 0.8), (omega, 0.2)])
                elif el_tact["avg_pitch"] == "normal":
                    m_2 = MassFunction([(omega, 1)])
                elif el_tact["avg_pitch"] == "hoch" or el_tact["avg_pitch"] == "sehr hoch":
                    m_2 = MassFunction([({'j', 'f', 'su', 'a'}, 0.8), (omega, 0.2)])
                else:
                    m_2 = None

                if el_tact["sound_intensity"] == "niedrig" or el_tact["sound_intensity"] == "sehr niedrig":
                    m_3 = MassFunction([({'d', 'sa'}, 0.8), (omega, 0.2)])
                elif el_tact["sound_intensity"] == "normal":
                    m_3 = MassFunction([({'f'}, 0.6), (omega, 0.4)])
                elif el_tact["sound_intensity"] == "hoch" or el_tact["sound_intensity"] == "sehr hoch":
                    m_3 = MassFunction([({'j', 'su', 'a'}, 0.8), (omega, 0.2)])
                else:
                    m_3 = None

                m_4 = m_1.combine_conjunctive([m_2, m_3], normalization=True)
                print(m_4.max_pl())
    else:
        print("Given path is invalid")


if __name__ == "__main__":
    main()
