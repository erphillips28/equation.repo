#calculate the energy of a photon

#constants
plancks = 6.626e-34 #J*s plancks constant
c = 2.998e8 #m/s speed of light
J_to_eV = 1.602e-25
#variables

L_wave = float(input('wavelength(um):'))
E_photon = float()

def Photon(L_wave):
    E_photon = (plancks*c)/(J_to_eV*L_wave)
    return E_photon

E1 = Photon(L_wave)
print('the photon energy is', E1, 'eV')

