import csv
import argparse
import os.path
from pyds import MassFunction
from enum import Enum
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
            next(reader, None)
            for row in reader:
                speaking_rate_data = []
                pitch_data = []
                sound_intensity_data= []
                speaking_rate.append(row[1])
                avg_pitch.append(row[2])
                sound_intensity.append(row[3])

            for el in speaking_rate:
                val = el.replace(",",".")
                if float(val) < 4 and float(val) >= 0:
                    speaking_rate_data.append("l")
                elif float(val) >= 4 and float(val) < 5:
                    speaking_rate_data.append("m")
                else:
                    speaking_rate_data.append("h")

                print(val)
            for el in avg_pitch:
                if el == "sehr niedrig" or el=="niedrig":
                    pitch_data.append("l")
                elif el == "normal":
                    pitch_data.append("m")
                elif el == "hoch" or el== "sehr hoch":
                    pitch_data.append("h")
                print(el)
            for el in sound_intensity:
                if el == "sehr niedrig" or el =="niedrig":
                    sound_intensity_data.append("l")
                elif el == "normal":
                    sound_intensity_data.append("m")
                elif el == "hoch" or el == "sehr hoch":
                    sound_intensity_data.append("h")
                print(el)
                # für speaking_rate = l
            omega = {"su",'f','j','a','sa','d'}
            m1=MassFunction([({"sa",'d'},0.8),(omega,0.2)])
            print(m1.bel("sa"))


    else:
        print("Given path is invalid")
    
    


if __name__ == "__main__":
    main()
