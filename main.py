"""Calculates the statistical evidence of emotions based on voice recordings"""

import csv
import argparse
from pathlib import Path
from pyds import MassFunction


def emotionToString(s):
    """(String) -> String
    Translates shortened string into the right emotion"""

    if s == "d":
        return "Ekel"
    elif s == "f":
        return "Angst"
    elif s == "sa":
        return "Traurigkeit"
    elif s == "su":
        return "Ueberraschung"
    elif s == "a":
        return "Wut"
    elif s == "j":
        return "Freude"
    else:
        return "ND"


def main():
    """() -> 
    main function"""

    print("Main")

    # parses given arguments
    parser = argparse.ArgumentParser(description="Do something lol")
    parser.add_argument("input", help="input file")
    args = parser.parse_args()
    print("Given argument:", args.input)
    input_file = Path(args.input)

    # checks if given parameter is a valid path
    if input_file.is_file():
        print("Given path is valid")
        tacts = []

        # opens given file
        with open(input_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader, None)
            # for each row of the file add a tact to the tacts array
            for row in reader:
                tacts.append({
                    "id" : row[0],
                    "speaking_rate" : row[1],
                    "avg_pitch" : row[2],
                    "sound_intensity" : row[3]
                    })
            # iterates over each tact
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
                emotion = str(m_4.max_pl())[12:-3]
                print(m_4)
                print("Die plausibelste Emotion ist " + emotionToString(emotion) + ": " + str(m_4.pl({emotion})))

    else:
        print("Given path is invalid")


if __name__ == "__main__":
    main()
