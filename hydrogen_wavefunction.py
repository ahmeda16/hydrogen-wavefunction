import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


""" Computes the Radial Contribution of the Wavefunction Using Exponential Decay, Laguerre Polynomials, and Power Term
Arguments: (int) n - Principal Quantum Number, the energy level or shell. (r in spherical coordinates)
           (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates)
           (numpy array) r - Variable Radius Coordinate for seaborn plot 
           (numpy array) r - Variable Radius Coordinate for plot
           
Output: A numpy array of the radial contribution to the wavefunction
"""
def radial_Contribution(n, l, r):
    
    e = np.e
    a0 = sp.constants.physical_constants["Bohr radius"][0] * 1e+12
    z = 2 / (n * a0)

    squareRootTerm = np.sqrt(
                            (z ** 3) *
                            ((np.math.factorial(n - l - 1)) / (2 * n * (np.math.factorial(n + l))))
                            )
    
    powerOfLTerm = (z * r) ** l

    laguerreTerm = sp.special.genlaguerre((n - l - 1), (2 * l + 1))

    decayTerm = e**((-1)*((z * r) / 2))

    return squareRootTerm * powerOfLTerm * laguerreTerm(z * r) * decayTerm

""" Computes the Angular Contribution of the Wavefunction Using Exponential Decay, Legendre Polynomials, and Power Term

Arguments: (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates)
           (int) ml - Magnetic Quantum Number, the orientation in space of an orbital (ϕ in spherical coordinates)
           (numpy array) theta - Variable Polar Angle Coordinate for plot
           (numpy array) phi - Variable Azimuth Angle Coordinate for plot
           
Output: A numpy array of the angular contribution (spherical harmonics) of the wavefunction
"""
def angular_Contribution(l, ml, theta, phi):

    e = np.e
    pi = np.pi

    negPosTerm = (-1)**ml

    #Needed to ensure calculation for -l
    absML = np.abs(ml)
    sqaureRootTerm = np.sqrt(
                            (((2 * l) + 1)/(4 * pi)) *
                            ((np.math.factorial(l - absML))/(np.math.factorial(l + absML)))
                            )
    
    legendreTerm = sp.special.lpmv(ml, l, np.cos(theta))

    decayTerm = np.real(np.exp(1j * ml * phi))

    return negPosTerm * sqaureRootTerm * legendreTerm * decayTerm
    
