import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

""" Computes the Radial Contribution of the Wavefunction Using Exponential Decay, Laguerre Polynomials, and Power Term

Arguments: (int) n - Principal Quantum Number, the energy level or shell. (r in spherical coordinates)
           (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates)
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

    decayTerm = np.exp(1.j * ml * phi)

    return negPosTerm * sqaureRootTerm * legendreTerm * decayTerm
    
""" Computes the total complex wavefunction from the calculated angular_Contribution and radial_Contribution

Arguments: (int) n - Principal Quantum Number, the energy level or shell. (r in spherical coordinates)
           (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates) 
           (int) ml - Magnetic Quantum Number, the orientation in space of an orbital (ϕ in spherical coordinates)

Output: A COMPLEX numpy array of the total wavefunction
"""

def complex_Wave_Function(n, l, ml):     

    pi = np.pi

    num_points = 680
    r = np.linspace(0, 2, num_points)
    theta = np.linspace(0, 2 * pi, num_points)
    phi = np.linspace(0, pi, num_points)
    
    theta, phi = np.meshgrid(theta, phi)

    radial = radial_Contribution(n, l, r)
    angular = angular_Contribution(l, ml, theta, phi)

    psi = radial * angular

    return psi
    
def probability_Density(psi):

    return (np.abs(psi) ** 2)

def main_Plot(P):
    
    plt.imshow(P, interpolation='none')
    plt.show()

main_Plot(probability_Density(complex_Wave_Function(3,1,1)))

    
