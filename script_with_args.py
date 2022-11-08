import argparse
 #continue importing functions
from Nernst_Ecell import Potential


def Main():
    p = argparse.ArgumentParser()
    p.add_argument("TempK", type=float)
    p.add_argument("E_s", type=float)
    p.add_argument("z", type=float)
    p.add_argument("Q", type=float)
    #continue adding variables here
    args = p.parse_args()

    potential_energy = Potential(
        args.TempK, args.E_s, args.z, args.Q)
    print(potential_energy)
    #continue calling formulas here


if __name__ == "__main__":
    Main()
