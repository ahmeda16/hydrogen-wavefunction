# The Hydrogen Wavefunction & Electron Density Cloud Plot

## 1. Pre-requisites

### 1.1 Language
Python (3.11.2 64-bit) was the main method behind the plot file and makes use of many libraries for ease of code visualization. Libraries and main imports include,

* Math (Internal)
* NumPY (1.24.3)
* SciPY (1.11.2)
* Matplotlib (3.7.2)
* Seaborn (0.12.2)

### 1.2 Basis Knowledge
As the topic of the electron cloud density is complex to calculate, a foundation in Multivariable Calculus, the general idea of Quantum Mechanics, and knowledge of Laugerre Polynomials/Legendre Polynomials would be beneficial. However, I will try my best to explain the process.


## 2. Foundation Explanation
If you already have the basis knowledge down you may skip this section as it is a revision and explanation portion. Only necessary ideas will be conveyed in this section. Resources will be provided as per section explanation.

### 2.1 Multivariable Calculus 



### 2.2 Quantum Mechanics 



### 2.3 Laugerre Polynomials 



## 3. The Wavefunction 



### 3.1 Atomic Shape



#### 3.1.x Atomic Orbitals



#### 3.1.x Quantum Numbers



### 3.2 Schrödinger Equation for the Hydrogen Wavefunction (Time Independant)

### $$\psi_{(n,ℓ,m_ℓ)} = R_{n,ℓ}(r)\times Y_{ℓ,m_ℓ}(\theta,\phi)$$

#### 3.2.x Radial Contribution

#### $$R_{(n,ℓ)}(r) = \sqrt{\left(\frac{2}{na_0}\right)^{3}\frac{(n-ℓ-1)!}{2n(n+1)!}}\left(\frac{2r}{na_0}\right)^{ℓ} L_{n-ℓ-1}^{2ℓ+1}\left(\frac{2r}{na_0}\right)e^{-\frac{r}{na_0}}$$

#### 3.2.x Angular Contribution 

#### $$Y_{ℓ}^{m_ℓ}(θ,ϕ) = (-1)^{m_ℓ} \sqrt{\left(\frac{2ℓ+1}{4π}\right)\frac{(ℓ-m_ℓ)!}{(ℓ+m_ℓ)!}}P_{ℓ}^{m_ℓ}(cos(θ))e^{im_ℓϕ}$$

#### 3.2.x Probability Density

#### $$P(r,\theta,\phi) = |\psi_{(n,ℓ,m_ℓ)}(r,\theta,\phi)|^2$$

## 4. References
#### [1] Martin Fränzl, Universität Leipzig, Molecular Nanophotonics Group, "The Hydrogen Atom" https://home.uni-leipzig.de/~physik/sites/mona/wp-content/uploads/sites/3/2017/12/Hydrogen_Atom.pdf
#### [2] The University of Washington, Physics 441, "Radial Wave Functions from the Solution of the Radial Equation" https://faculty.washington.edu/seattle/physics441/ch10b.pdf