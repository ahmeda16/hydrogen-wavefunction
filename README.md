# The Hydrogen Wavefunction & Electron Density Cloud Plot

### Execution of File
To execute the Python file, you must first follow these items, (1.1 Language). Execution is done through the Python terminal by entering your Quantum Numbers with set restrictions stated below.
| Quantum Number | Limitations             |
| -------------- | ----------------------- |
| $$n$$          | $$n \geq  1$$           |
| $$ℓ$$          | $$0 \leq  l \lt  n$$    |
| $$m_ℓ$$        | $$-ℓ \leq m_ℓ \leq ℓ$$   |

After execution, a 3D interactable figure will pop up via Matplotlib and will save a .png file within the respective Python file directory where ever that may be on your device. If the Wavefunction Plot is not within the bounds, try adjusting the Global Constants to a larger value by an addition of 500 for both. This portion is not automated, but will be in the future.

Figure examples are shown below for: $n = 2, l = 1, m_ℓ = 1$

<div align="center">
  <h3> Real Hydrogen Wavefunction </h3>
  <img src="Example_211_Real.png" />
  
  <h3> Complex Hydrogen Wavefunction </h3>
  <img src="Example_211_Complex.png" />
</div>

## 1. Pre-requisites

### 1.1 Language
Python (3.11.2 64-bit) was the main method behind the plot file and makes use of many libraries for ease of code visualization. Libraries and main imports include,

* Math (Internal)
* NumPY (1.24.3)
* SciPY (1.11.2)
* Matplotlib (3.7.2)

### 1.2 Basis Knowledge
As the topic of the electron cloud density is complex to calculate, a foundation in Multivariable Calculus, the general idea of Quantum Mechanics, and knowledge of Laugerre Polynomials/Legendre Polynomials would be beneficial. However, I will try my best to explain the process.


## 2. Foundation Explanation
If you already have the basis knowledge down you may skip this section as it is a revision and explanation portion. Only necessary ideas will be conveyed in this section. Resources will be provided as per section explanation.

### 2.1 Multivariable Calculus 

#### 2.1.1 Spherical Coordinates 
Spherical Coordinates is formally defined to be a coordinate system for an n-dimension Euclidean space where $(n = 3)$ with the following parameters:

1) The Radial Distance (radius, or radial coordinate), being the distance from the origin to the point as a straight line (magnitude). $$r,ρ \left \( 0 \leq r,ρ \right \)$$ 

2) The Polar Angle, being the angle (typically in radians) from the x - axis, counter clockwise stopping at the xy projection of r. $$\theta \left \( 0 \leq \theta \lt 2\pi \right \)$$ 

3) The Azimuth Angle, being the angle (typically in radians) from the z - axis, being the direct angle stopping at r. $$\phi \left \( 0 \leq \phi  \leq \pi \right \)$$

<div align="center">
  <h3> Spherical Coordinate Definition </h3>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Sphericalcoordinates.svg/280px-Sphericalcoordinates.svg.png" />
</div>

Note: that theta ($\theta$) and phi ($\phi$) could be defined in either order (theta being phi and vice versa). This is up to the discretion of whoever is applying it. For this case, it will be hard defined as stated above.

The direct translation from Cartesian to Spherical is as follows:
$$r,ρ = \sqrt{x^2 + y^2 + z^2}$$
$$\theta = \arctan{\frac{y}{x}}$$
$$\phi = \arccos{\frac{z}{\sqrt{x^2 + y^2 + z^2}}}$$

All in all, the Spherical Coordinate System is another way of plotting any particular point in 3D space rather than using the Cartesian Coordinate System $(x, y, z)$. Spherical coordinates has many advantages over the Cartesian Coordinate System as it applies for the wavefunction which will be discussed further. 

An excellent resource on Spherical Coordinates is linked here from Paul's Online Notes: https://tutorial.math.lamar.edu/classes/calciii/SphericalCoords.aspx
### 2.2 Quantum Mechanics 



### 2.3 Laugerre Polynomials 



### 2.4 Legendre Polynomials 



## 3. The Wavefunction 



### 3.1 Atomic Shape



#### 3.1.1 Atomic Orbitals



#### 3.1.2 Quantum Numbers



### 3.2 Schrödinger Equation for the Hydrogen Wavefunction (Time Independant)

### $$\psi_{(n,ℓ,m_ℓ)} = R_{n,ℓ}(r)\times Y_{ℓ,m_ℓ}(\theta,\phi)$$

#### 3.2.1 Radial Contribution

#### $$R_{(n,ℓ)}(r) = \sqrt{\left(\frac{2}{na_0}\right)^{3}\frac{(n-ℓ-1)!}{2n(n+1)!}}\left(\frac{2r}{na_0}\right)^{ℓ} L_{n-ℓ-1}^{2ℓ+1}\left(\frac{2r}{na_0}\right)e^{-\frac{r}{na_0}}$$

#### 3.2.2 Angular Contribution 

#### $$Y_{ℓ}^{m_ℓ}(θ,ϕ) = (-1)^{m_ℓ} \sqrt{\left(\frac{2ℓ+1}{4π}\right)\frac{(ℓ-m_ℓ)!}{(ℓ+m_ℓ)!}}P_{ℓ}^{m_ℓ}(cos(θ))e^{im_ℓϕ}$$

#### 3.2.3 Probability Density

#### $$P(r,\theta,\phi) = |\psi_{(n,ℓ,m_ℓ)}(r,\theta,\phi)|^2$$

## 4. References
#### [1] Martin Fränzl, Universität Leipzig, Molecular Nanophotonics Group, "The Hydrogen Atom" https://home.uni-leipzig.de/~physik/sites/mona/wp-content/uploads/sites/3/2017/12/Hydrogen_Atom.pdf
#### [2] The University of Washington, Physics 441, "Radial Wave Functions from the Solution of the Radial Equation" https://faculty.washington.edu/seattle/physics441/ch10b.pdf
#### [3] Wikipedia, "Vector Fields in Cylindrical Coordinates" https://en.wikipedia.org/wiki/Vector_fields_in_cylindrical_and_spherical_coordinates
