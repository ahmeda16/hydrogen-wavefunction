import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n =  int(input('Enter an n Quantum Number: '))
l = int(input('Enter an l Quantum Number: '))
ml = int(input('Enter an ml Quantum Number: '))

#GLOBAL CONSTANTS (ADJUST IF NECESSARY)
num_points = 680
extent = 480

# Computes the Radial Contribution of the Wavefunction Using Exponential Decay, Laguerre Polynomials, and Power Term
#
# Arguments: (int) n - Principal Quantum Number, the energy level or shell. (r in spherical coordinates)
#            (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates)
#            (numpy array) r - Variable Radius Coordinate for plot
#            
# Output: (numpy array) of the radial contribution to the wavefunction
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

# Computes the Angular Contribution of the Wavefunction Using Exponential Decay, Legendre Polynomials, and Power Term

# Arguments: (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates)
#            (int) ml - Magnetic Quantum Number, the orientation in space of an orbital (ϕ in spherical coordinates)
#            (numpy array) theta - Variable Polar Angle Coordinate for plot
#            (numpy array) phi - Variable Azimuth Angle Coordinate for plot
#           
# Output: (numpy array) of the angular contribution (spherical harmonics) of the wavefunction
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
    
# Computes the total complex wavefunction from the calculated angular_Contribution and radial_Contribution
#
# Arguments: (int) n - Principal Quantum Number, the energy level or shell. (r in spherical coordinates)
#            (int) l - Angular Momentum Quantum Number, the subshell or angular dependence of the orbital. (Θ in spherical coordinates) 
#            (int) ml - Magnetic Quantum Number, the orientation in space of an orbital (ϕ in spherical coordinates)
#            **IMPORTANT, with converting r, theta, phi to their respective cartesian coordinates. We must consider all possible values of r, Θ, ϕ.
#            *Note, x,y,z linspaces are set from the global constants
#          
# Output: COMPLEX (numpy array) of the total wavefunction
def complex_Wave_Function(n, l, ml):     

    if (not isinstance(n, int)) or (n < 1):
        raise ValueError('Quantum Number Error: n shall be part of the Natural Set (n >= 1)')

    if (not isinstance(l, int)) or not (0 <= l < n):
        raise ValueError('Quantum Number Error: l shall be part of the Positive Integer Set and Satisfy (0 <= l < n)')
    
    if (not isinstance(ml, int)) or not (-l <= ml <= l):
        raise ValueError('Quantum Number Error: ml shall be part of the Integer Set and Satisfy (-l <= ml <= l)')

    pi = np.pi

    x = y = z = np.linspace(-extent, extent, num_points)
    x, y = np.meshgrid(x, y)

    magnitude = np.sqrt((x ** 2) + (y ** 2) + (z ** 2))
    r = magnitude
    theta = np.arctan(y / x)
    phi = np.arccos(z / magnitude)

    radial = radial_Contribution(n, l, r)
    angular = angular_Contribution(l, ml, theta, phi)

    psi = radial * angular
    
    return psi
    
# Computes the probability density of any given wavefunction set as z for future plot
#
# Arguments: (numpy array) psi - A COMPLEX numpy array describing the total wavefunction  
# 
# Output: REAL (numpy array) of the probability density
def probability_Density(psi):

    return (np.abs(psi) ** 2)

# Plots any given REAL function including probability density P on a 3D contour graph
#
# Arguments: (numpy array) P - A REAL numpy array describing the total function  
#            (string) text - A title formatter for Real, Complex, or Probability Density Plot
# 
# Output: A final plot of the given function
def main_Plot_Wavefunction(P, text):

    x = y = np.linspace(-extent, extent, num_points)
    x, y = np.meshgrid(x, y)
    z = P

    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    plt.title("Hydrogen Wavefunction " + text + "$ \psi_{(n,ℓ,m_ℓ)}$")
    ax.set_xlabel('$x$', fontsize=20, rotation=150)
    ax.set_ylabel('$y$', fontsize=20, rotation=0)
    ax.set_zlabel('$\psi_{(n,ℓ,m_ℓ)}$', fontsize=20, rotation=150)
    
    ax.contour(x, y, z, 50, cmap='magma')

    plt.savefig(f'({n},{l},{ml})[{text}].png')
    plt.show()


#Real Plot
main_Plot_Wavefunction(np.real(complex_Wave_Function(n, l, ml)), 'Real')

#Complex Plot
main_Plot_Wavefunction(np.imag(complex_Wave_Function(n, l, ml)), 'Complex')

#Probability Density Plot
main_Plot_Wavefunction(np.imag(complex_Wave_Function(n, l, ml)), 'Probability Density')