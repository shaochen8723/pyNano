#!/usr/bin/python -tt
# Chen Shao
# Strain energy in PMMA/graphene nanocomposites

import math
import pyNano as nano
import matplotlib as mpl
import matplotlib.pyplot as plt

# set plot configuration
lineweight =  1.5
mpl.rcParams['lines.linewidth'] = lineweight
mpl.rcParams['lines.markeredgewidth'] = lineweight
mpl.rcParams['lines.markersize'] = 12
mpl.rcParams['lines.color'] = 'r'
mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['font.size'] = 24
mpl.rcParams['axes.linewidth'] = lineweight
mpl.rcParams['axes.color_cycle'] = 'r, b, m, k, g, c, y'
mpl.rcParams['axes.labelweight'] = 'bold'
mpl.rcParams['figure.dpi'] = 120
mpl.rcParams['figure.figsize'] = (16, 6)
mpl.rcParams['savefig.dpi'] = 120
mpl.rcParams['savefig.bbox'] = 'tight'
mpl.rcParams['savefig.pad_inches'] = 0.2
mpl.rcParams['legend.numpoints'] = 1

def main():
  n = 2 # number of sheets per layer
  Ly = 50.96 #nm system size in y
  Lx = 10 #nm
  Lz = 20 #nm

  epsi_gp = [0.5+x*0.01 for x in range(200)]  #kcal/mol
  tau = [0.033+x*0.267 for x in epsi_gp]  #GPa shear strength
  
  se = []
  N = range(2,20)
  
  for i in N:
    res, a, b = nano.getStrainEnergy(0.001, tau[0], i, Lx, Ly, n)
    se.append(res)
  
  
  plt.figure(num=1,figsize = (8,6))
  plt.plot(N,se,label='UTS = '+str(10))
  
  plt.figure(num = 1, figsize = (8, 6))
  plt.xlabel('L (nm)')
  plt.ylabel('UTS (GPa)')
  plt.legend(loc = 0, prop={'size':20})
  #plt.xlim(0,0.5)
  #plt.ylim(0,5e-15)
  plt.tight_layout()
  plt.savefig('test.tiff', pad_inches = 0.2)
  return

if __name__ == '__main__':
  main()