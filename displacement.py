# formula for displacement of object

# constants

# variables
v = float(input('input velocity:'))
a = float(input('input acceleration:'))
t = float(input('input time:'))
# function


def displace(v, a, t):
    disp = v*t + (1/2)*a*(t**2)
    return disp


d1 = displace(v, a, t)
print('the displacement will be', d1, 'meters')
