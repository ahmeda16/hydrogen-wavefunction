import numpy as np
import scipy as sp
import matplotlib as mpl
import seaborn as sb
import math

""" Computes the Radial Contribution of the Wavefunction Using Exponential Decay, Laguerre Polynomials, and Power Term

Arguments: (int) n - Principal Quantum Number, the energy level or shell. (r in spherical coordinates)
           (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates)
           (numpy array) r - Radial Coordinate, from a given polar/spherical coordinate. 
           
Output: A numpy array of the radial contribution to the wavefunction
"""
def radial_Contribution(n, l, r):
    
    e = math.e
    a0 = sp.constants.physical_constants["Bohr radius"][0] * 1e+12
    z = 2 / (n * a0)

    squareRootTerm = (-1) * np.sqrt(
                                   (z ** 3) *
                                   ((np.math.factorial(n - l - 1)) / (2 * n * (np.math.factorial(n + l))))
                                   )
    
    powerOfLTerm = (z * r) ** l

    laguerreTerm = sp.special.genlaguerre((n - l - 1), (2 * l + 1))

    decayTerm = e**((-1)*((z * r) / 2))

    return squareRootTerm * powerOfLTerm * laguerreTerm(z * r) * decayTerm



