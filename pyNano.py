#!/usr/bin/env python -tt
# Chen Shao
# Module to predict strain energy in PMMA/graphene nanocomposites

import math

# global parameters
UTS = 10 #GPa UTS for multilayer graphene
dg = 0.34 #nm interlayer distance between graphene sheets
Eg = 900 #GPa
Gg = 2  #GPa
D = 236 #GPa nm
L0 = math.sqrt(D*dg/4/Gg)

def getMLGStrength(Loverlap):
  '''
  compute UTS given Loverlap
  '''
  return UTS*math.sinh(Loverlap/L0)/(1+math.cosh(Loverlap/L0))

def getLoverlap(Loverlap, dL, n):
  '''
  compute new overlap length once dL and n is given
  50% overlapping percentage is assumed
  '''
  return Loverlap-dL/n/2
  
def getForce(sigma, tau, N, Lx, Ly, Lsheet, delL):
  '''
  compute force needed to pull graphene layer given
  sigma, thickness of graphene layer N, interfacial shear
  strength tau, Lx, Ly assuming pulling in y direction
  '''
  Lc = sigma/tau*N/2*dg
  nc = math.floor((Lc+delL)/Lsheet)
  #print Lc, nc
  if Ly >= Lc and Lc > nc*Lsheet-delL:
    # yielding in graphene layer
    return sigma*Lx*N*dg, Ly-delL
  elif Ly >= Lc and Lc <= nc*Lsheet-delL:
    return 2*tau*Lx*(nc*Lsheet-delL), nc*Lsheet-delL
  else:
    return 2*tau*Lx*(Ly-delL), Ly-delL

def getStrainEnergy(dL, tau, N, Lx, Ly, n):
  '''
  compute deformation strain energy given input
  of dL, tau, N, Lx, Ly, n
  '''
  res = 0
  delL = 0  #nm total displacement
  Loverlap = Ly/n/2 #nm initial overlapping length
  Lsheet = Ly/n #nm graphene sheet length
  Lgp = Ly  #nm initial overlapping between graphene and polymer
  a = b = []
  while Lgp > 0:
    sigma = getMLGStrength(Loverlap)
    force, Lgp = getForce(sigma, tau, N, Lx, Ly, Lsheet, delL)
    #print force, Lgp
    #raw_input('------------')
    res += force*dL
    
    #update values
    delL += dL
    Loverlap -= dL/n/2
    a.append(force)
    b.append(Lgp)
  return res, a, b
