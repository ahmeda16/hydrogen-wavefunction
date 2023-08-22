import numpy as np
import scipy as sp
import matplotlib as mpl
import seaborn as sb

""" Computes the Radial Contribution of the Wavefunction Using Exponential Decay, Laguerre Polynomials, and Power Term

Arguments: (int) n - Principal Quantum Number, the energy level or shell. (r in spherical coordinates)
           (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates)
           (numpy array) r - Radial Coordinate, from a given polar/spherical coordinate. 
           
Output: A numpy array of the radial contribution to the wavefunction
"""
def radial_Contribution(n, l, r):
    
    e = np.e
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

""" Computes the Angular Contribution of the Wavefunction Using Exponential Decay, Legendre Polynomials, and Power Term

Arguments: (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates)
           (int) ml - Magnetic Quantum Number, the orientation in space of an orbital (ϕ in spherical coordinates)
           (numpy array) theta - Polar Angle Coordinate, from a given polar/spherical coordinate. 
           (int) phi - Azimuth Angle Coordinate, from a given polar/spherical coordinate. 
           
           *Note, that we only analyize the REAL portion of the complex spherical harmonic equation
           *Note, ml is defined to be a integer in Physics, we may consider the negative here due it its boundary conditions
Output: A numpy array of the angular contribution (spherical harmonics) of the wavefunction
"""
def angular_Contribution(l, ml, theta, phi):


    e = np.e
    pi = np.pi

    negPosTerm = (-1)**ml

    sqaureRootTerm = np.sqrt(
                            (((2 * l) + 1)/(4 * pi)) *
                            ((np.math.factorial(l - ml))/(np.math.factorial(l + ml)))
                            )
    
    legendreTerm = sp.special.lpmv(ml, l, np.cos(theta))

    decayTerm = np.real(np.exp(1j * ml * phi))

    return negPosTerm * sqaureRootTerm * legendreTerm * decayTerm
