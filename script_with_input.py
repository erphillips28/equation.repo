import argparse

from Nernst_Ecell import Potential
from newton_grav import newt_grav


def run_Ecell():
    TempK = float(input('temperature(K):'))  # around 270
    # need to be drop down for element reactions
    E_s = float(input('standard cell potential:'))
    # electron transfer *will be auto input from previous answer*
    z = float(input('electron exchange number:'))
    # reaction quotient 0<x<1 *element dependent*
    Q = float(input('reaction quotient:'))

    e_Cell = Potential(
        TempK, E_s, z, Q)
    print(e_Cell)


def run_grav():
    # collect inputs
    # run run_ecell
    print("result from newt grav=")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("eq")
    args = p.parse_args()

    if args.eq == "ecell":
        run_Ecell()
    elif args.eq == "grav":
        run_grav()

    #continue adding args
    else:
        print("invalid eq", args.eq)
