import math, csv, os, sys, string
#from pylab import *

class central_star:

#--------------------------------------------------------------------------------------------
      def __init__(self,gm_m3ps2):

          self.dtr = math.pi/180.0
          self.rtd = 180.0/math.pi
          self.autkm = 149597870.691
          self.central_star_gm_km3ps2 = gm_m3ps2/(math.pow(1000.0,3))

#--------------------------------------------------------------------------------------------
      def get_central_star_gm(self):
          return self.central_star_gm_km3ps2
