## include a size and T as docopt

import numpy as np
# from numba import jit

def calculate_local_energy(landscape):
    pass

def single_timestep(landscape,T):
   ## generate two random numbers 
   ## call energy function
   ## generate random number for Boltzmann
   ## flip?
   return landscape,T


size = 100
ising_landscape = np.zeros([size,size]) 

for _ in range(size**2):
    landscape,T = single_timestep(landscape,T)
