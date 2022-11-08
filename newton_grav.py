#import scipy as sp
#import numpy as np


G = 6.67  # Gravitational_constant
# r = float(input('distance(m):'))
# m1 = float(input('mass1(kg):'))
# m2 = float(input('mass2(kg):'))

# Force = float()


def newt_grav(m1, m2, r):
    Force = G*(m1*m2)/(r**2)
    return Force


# F1 = newt_grav(m1, m2, r)
# print("the force will be", F1, "newton-meters.")
