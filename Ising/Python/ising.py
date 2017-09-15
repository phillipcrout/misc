## include a size and T as docopt

import numpy as np
# from numba import jit

def calculate_local_energy(landscape,location):
    pass

def single_timestep(landscape,T):
   rand_location =  [np.random.randint(0,high=landscape.shape[0]-1),np.random.randint(0,high=landscape.shape[0]-1)]
   local_energy = calculate_local_energy(landscape,rand_location)
   ## generate random number for Boltzmann
   ## flip?
   return landscape,T

T = 1
size = 100
landscape = np.zeros([size,size]) 

for _ in range(size**2):
    landscape,T = single_timestep(landscape,T)
