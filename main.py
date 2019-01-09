"Calculates the statistical evidence of emotions based on voice recordings"

import csv
import argparse
import os.path
from pyds import MassFunction
from enum import Enum
from pathlib import Path
class Emotion(Enum):
     FEAR =0
     SURPRISE= 1
     ANGER = 2
     JOY = 3
     DISGUST = 4
     SADNESS = 5

def emotionToString( s ):
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

                if float(el_tact["speaking_rate"].replace(",",".")) < 4:
                    m1 = MassFunction([({'d', 'sa'}, 0.8), (omega, 0.2)])
                elif(float(el_tact["speaking_rate"].replace(",","."))>= 4 and float(el_tact["speaking_rate"].replace(",",".")) < 5):
                    m1= MassFunction([(omega, 1)])
                elif float(el_tact["speaking_rate"].replace(",",".")) >= 5:
                    m1= MassFunction([({'j', 'f', 's', 'a'}, 0.8), (omega, 0.2)])
                else:
                    m1 = None

                if el_tact["avg_pitch"] == "niedrig" or el_tact["avg_pitch"] == "sehr niedrig" :
                    m2 = MassFunction([({'d','sa'},0.8),(omega,0.2)])
                elif el_tact["avg_pitch"] == "normal":
                    m2 = MassFunction([(omega,1)])
                elif el_tact["avg_pitch"] == "hoch" or el_tact["avg_pitch"] == "sehr hoch":
                    m2 = MassFunction([({'j','f','su','a'}, 0.8), (omega, 0.2)])
                else:
                    m2 = None

                if el_tact["sound_intensity"] == "niedrig" or el_tact["sound_intensity"] == "sehr niedrig" :
                    m3 = MassFunction([({'d','sa'},0.8),(omega,0.2)])
                elif el_tact["sound_intensity"] == "normal":
                    m3 = MassFunction([({'f'}, 0.6), (omega, 0.4)])
                elif el_tact["sound_intensity"] == "hoch" or el_tact["sound_intensity"] == "sehr hoch":
                    m3 = MassFunction([({'j','su','a'}, 0.8), (omega, 0.2)])
                else:
                    m3 = None

                m4 = m1.combine_conjunctive([m2, m3], normalization=True)
                print("Die plausibelste Emotion ist " + emotionToString(str(m4.max_pl())[12:-3]))
    else:
        print("Given path is invalid")



if __name__ == "__main__":
    main()
