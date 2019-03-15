import math, csv, os, sys, string
from pylab import *

class planet:

#--------------------------------------------------------------------------------------------------------
      def __init__(self, name):

          self.dtr = math.pi/180.0
          self.rtd = 180.0/math.pi
          self.autkm = 149597870.691
          self.pos_km = [0.0e0, 0.0e0, 0.0e0]
          self.vel_kmps = [0.0e0, 0.0e0, 0.0e0]
          self.name = name
           
          if   name == 'mercury':
               self.name = name
               self.gm_km3ps2 = 2.2032e13/(math.pow(1000.0,3))
               self.semi_major_axis0_au = 0.38709843
               self.semi_major_axis_rate_aupcty = 0.00000000
               self.ecc0 = 0.20563661
               self.ecc_rate_pcty = 0.00002123
               self.incl0_dg = 7.00559432
               self.incl0_rd = self.incl0_dg*(math.pi/180.0)
               self.incl_rate_dgpcty = -0.00590158
               self.incl_rate_rdpcty = self.incl_rate_dgpcty*(math.pi/180.0)
               self.mean_long0_dg = 252.25166724
               self.mean_long0_rd = self.mean_long0_dg*(math.pi/180.0)
               self.mean_long_rate_dgpcty = 149472.67486623
               self.mean_long_rate_rdpcty = self.mean_long_rate_dgpcty*(math.pi/180.0)
               self.long_perh0_dg = 77.45771895
               self.long_perh0_rd = self.long_perh0_dg*(math.pi/180.0)
               self.long_perh_rate_dgpcty = 0.15940013
               self.long_perh_rate_rdpcty = self.long_perh_rate_dgpcty*(math.pi/180.0)
               self.long_asc_node0_dg = 48.33961819
               self.long_asc_node0_rd = self.long_asc_node0_dg*(math.pi/180.0)
               self.long_asc_node_rate_dgpcty = -0.12214182
               self.long_asc_node_rate_rdpcty = self.long_asc_node_rate_dgpcty*(math.pi/180.0)
               self.b = 0.0e0
               self.c = 0.0e0
               self.s = 0.0e0
               self.f = 0.0e0
          elif name == 'venus':
               self.name = name
               self.gm_km3ps2 = 3.24859e14/(math.pow(1000.0,3))
               self.semi_major_axis0_au = 0.72332102
               self.semi_major_axis_rate_aupcty = -0.00000026
               self.ecc0 = 0.00676399
               self.ecc_rate_pcty = -0.00005107
               self.incl0_dg = 3.39777545
               self.incl0_rd = self.incl0_dg*(math.pi/180.0)
               self.incl_rate_dgpcty =  0.00043494
               self.incl_rate_rdpcty = self.incl_rate_dgpcty*(math.pi/180.0)
               self.mean_long0_dg = 181.97970850
               self.mean_long0_rd = self.mean_long0_dg*(math.pi/180.0)
               self.mean_long_rate_dgpcty =  58517.81560260
               self.mean_long_rate_rdpcty = self.mean_long_rate_dgpcty*(math.pi/180.0)
               self.long_perh0_dg = 131.76755713
               self.long_perh0_rd = self.long_perh0_dg*(math.pi/180.0)
               self.long_perh_rate_dgpcty = 0.05679648
               self.long_perh_rate_rdpcty = self.long_perh_rate_dgpcty*(math.pi/180.0)
               self.long_asc_node0_dg = 76.67261496
               self.long_asc_node0_rd = self.long_asc_node0_dg*(math.pi/180.0)
               self.long_asc_node_rate_dgpcty = -0.27274174
               self.long_asc_node_rate_rdpcty = self.long_asc_node_rate_dgpcty*(math.pi/180.0)
               self.b = 0.0e0
               self.c = 0.0e0
               self.s = 0.0e0
               self.f = 0.0e0
          elif name == 'earth':
               self.name = name
               self.gm_km3ps2 = 3.986004418e14/(math.pow(1000.0,3))
               self.semi_major_axis0_au = 1.00000018
               self.semi_major_axis_rate_aupcty = -0.00000003
               self.ecc0 = 0.01673163
               self.ecc_rate_pcty = -0.00003661
               self.incl0_dg = -0.00054346
               self.incl0_rd = self.incl0_dg*(math.pi/180.0)
               self.incl_rate_dgpcty = -0.01337178
               self.incl_rate_rdpcty = self.incl_rate_dgpcty*(math.pi/180.0)
               self.mean_long0_dg = 100.46691572
               self.mean_long0_rd = self.mean_long0_dg*(math.pi/180.0)
               self.mean_long_rate_dgpcty =  35999.37306329
               self.mean_long_rate_rdpcty = self.mean_long_rate_dgpcty*(math.pi/180.0)
               self.long_perh0_dg = 102.93005885
               self.long_perh0_rd = self.long_perh0_dg*(math.pi/180.0)
               self.long_perh_rate_dgpcty = 0.31795260
               self.long_perh_rate_rdpcty = self.long_perh_rate_dgpcty*(math.pi/180.0)
               self.long_asc_node0_dg = -5.11260389
               self.long_asc_node0_rd = self.long_asc_node0_dg*(math.pi/180.0)
               self.long_asc_node_rate_dgpcty = -0.24123856
               self.long_asc_node_rate_rdpcty = self.long_asc_node_rate_dgpcty*(math.pi/180.0)
               self.b = 0.0e0
               self.c = 0.0e0
               self.s = 0.0e0
               self.f = 0.0e0
          elif name == 'mars':
               self.name = name
               self.gm_km3ps2 = 4.2828e13/(math.pow(1000.0,3))
               self.semi_major_axis0_au = 1.52371243
               self.semi_major_axis_rate_aupcty =  0.00000097
               self.ecc0 = 0.09336511
               self.ecc_rate_pcty =  0.00009149
               self.incl0_dg =  1.85181869
               self.incl0_rd = self.incl0_dg*(math.pi/180.0)
               self.incl_rate_dgpcty = -0.00724757
               self.incl_rate_rdpcty = self.incl_rate_dgpcty*(math.pi/180.0)
               self.mean_long0_dg =  -4.56813164
               self.mean_long0_rd = self.mean_long0_dg*(math.pi/180.0)
               self.mean_long_rate_dgpcty =  19140.29934243
               self.mean_long_rate_rdpcty = self.mean_long_rate_dgpcty*(math.pi/180.0)
               self.long_perh0_dg = -23.91744784
               self.long_perh0_rd = self.long_perh0_dg*(math.pi/180.0)
               self.long_perh_rate_dgpcty = 0.45223625
               self.long_perh_rate_rdpcty = self.long_perh_rate_dgpcty*(math.pi/180.0)
               self.long_asc_node0_dg = 49.71320984
               self.long_asc_node0_rd = self.long_asc_node0_dg*(math.pi/180.0)
               self.long_asc_node_rate_dgpcty = -0.26852431
               self.long_asc_node_rate_rdpcty = self.long_asc_node_rate_dgpcty*(math.pi/180.0)
               self.b = 0.0e0
               self.c = 0.0e0
               self.s = 0.0e0
               self.f = 0.0e0
          elif name == 'jupiter':
               self.name = name
               self.gm_km3ps2 = 1.26686534e17/(math.pow(1000.0,3))
               self.semi_major_axis0_au = 5.20248019
               self.semi_major_axis_rate_aupcty = -0.00002864
               self.ecc0 = 0.04853590
               self.ecc_rate_pcty =  0.00018026
               self.incl0_dg =  1.29861416
               self.incl0_rd = self.incl0_dg*(math.pi/180.0)
               self.incl_rate_dgpcty = -0.00322699
               self.incl_rate_rdpcty = self.incl_rate_dgpcty*(math.pi/180.0)
               self.mean_long0_dg =  34.33479152
               self.mean_long0_rd = self.mean_long0_dg*(math.pi/180.0)
               self.mean_long_rate_dgpcty =   3034.90371757
               self.mean_long_rate_rdpcty = self.mean_long_rate_dgpcty*(math.pi/180.0)
               self.long_perh0_dg =  14.27495244
               self.long_perh0_rd = self.long_perh0_dg*(math.pi/180.0)
               self.long_perh_rate_dgpcty = 0.18199196
               self.long_perh_rate_rdpcty = self.long_perh_rate_dgpcty*(math.pi/180.0)
               self.long_asc_node0_dg = 100.29282654
               self.long_asc_node0_rd = self.long_asc_node0_dg*(math.pi/180.0)
               self.long_asc_node_rate_dgpcty =  0.13024619
               self.long_asc_node_rate_rdpcty = self.long_asc_node_rate_dgpcty*(math.pi/180.0)
               self.b =  -0.00012452
               self.c =   0.06064060
               self.s =  -0.35635438
               self.f =  38.35125000
          elif name == 'saturn':
               self.name = name
               self.gm_km3ps2 = 3.7931187e16/(math.pow(1000.0,3))
               self.semi_major_axis0_au = 9.54149883
               self.semi_major_axis_rate_aupcty = -0.00003065
               self.ecc0 = 0.05550825
               self.ecc_rate_pcty = -0.00032044
               self.incl0_dg =  2.49424102
               self.incl0_rd = self.incl0_dg*(math.pi/180.0)
               self.incl_rate_dgpcty =  0.00451969
               self.incl_rate_rdpcty = self.incl_rate_dgpcty*(math.pi/180.0)
               self.mean_long0_dg =  50.07571329
               self.mean_long0_rd = self.mean_long0_dg*(math.pi/180.0)
               self.mean_long_rate_dgpcty =   1222.11494724
               self.mean_long_rate_rdpcty = self.mean_long_rate_dgpcty*(math.pi/180.0)
               self.long_perh0_dg =  92.86136063
               self.long_perh0_rd = self.long_perh0_dg*(math.pi/180.0)
               self.long_perh_rate_dgpcty = 0.54179478
               self.long_perh_rate_rdpcty = self.long_perh_rate_dgpcty*(math.pi/180.0)
               self.long_asc_node0_dg = 113.63998702
               self.long_asc_node0_rd = self.long_asc_node0_dg*(math.pi/180.0)
               self.long_asc_node_rate_dgpcty = -0.25015002
               self.long_asc_node_rate_rdpcty = self.long_asc_node_rate_dgpcty*(math.pi/180.0)
               self.b =   0.00025899
               self.c =  -0.13434469
               self.s =   0.87320147
               self.f =  38.35125000
          elif name == 'uranus':
               self.name = name
               self.gm_km3ps2 = 5.793939e15/(math.pow(1000.0,3))
               self.semi_major_axis0_au = 19.18797948
               self.semi_major_axis_rate_aupcty = -0.00020455
               self.ecc0 = 0.04685740
               self.ecc_rate_pcty = -0.00001550
               self.incl0_dg =  0.77298127
               self.incl0_rd = self.incl0_dg*(math.pi/180.0)
               self.incl_rate_dgpcty = -0.00180155
               self.incl_rate_rdpcty = self.incl_rate_dgpcty*(math.pi/180.0)
               self.mean_long0_dg = 314.20276625
               self.mean_long0_rd = self.mean_long0_dg*(math.pi/180.0)
               self.mean_long_rate_dgpcty =    428.49512595
               self.mean_long_rate_rdpcty = self.mean_long_rate_dgpcty*(math.pi/180.0)
               self.long_perh0_dg = 172.43404441
               self.long_perh0_rd = self.long_perh0_dg*(math.pi/180.0)
               self.long_perh_rate_dgpcty = 0.09266985
               self.long_perh_rate_rdpcty = self.long_perh_rate_dgpcty*(math.pi/180.0)
               self.long_asc_node0_dg =  73.96250215
               self.long_asc_node0_rd = self.long_asc_node0_dg*(math.pi/180.0)
               self.long_asc_node_rate_dgpcty =  0.05739699
               self.long_asc_node_rate_rdpcty = self.long_asc_node_rate_dgpcty*(math.pi/180.0)
               self.b =   0.00058331
               self.c =  -0.97731848
               self.s =   0.17689245
               self.f =   7.67025000
          elif name == 'neptune':
               self.name = name
               self.gm_km3ps2 = 6.836529e15/(math.pow(1000.0,3))
               self.semi_major_axis0_au = 30.06952752
               self.semi_major_axis_rate_aupcty =  0.00006447
               self.ecc0 = 0.00895439
               self.ecc_rate_pcty =  0.00000818
               self.incl0_dg =  1.77005520
               self.incl0_rd = self.incl0_dg*(math.pi/180.0)
               self.incl_rate_dgpcty =  0.00022400
               self.incl_rate_rdpcty = self.incl_rate_dgpcty*(math.pi/180.0)
               self.mean_long0_dg = 304.22289287
               self.mean_long0_rd = self.mean_long0_dg*(math.pi/180.0)
               self.mean_long_rate_dgpcty =    218.46515314
               self.mean_long_rate_rdpcty = self.mean_long_rate_dgpcty*(math.pi/180.0)
               self.long_perh0_dg =  46.68158724
               self.long_perh0_rd = self.long_perh0_dg*(math.pi/180.0)
               self.long_perh_rate_dgpcty = 0.01009938
               self.long_perh_rate_rdpcty = self.long_perh_rate_dgpcty*(math.pi/180.0)
               self.long_asc_node0_dg = 131.78635853
               self.long_asc_node0_rd = self.long_asc_node0_dg*(math.pi/180.0)
               self.long_asc_node_rate_dgpcty = -0.00606302
               self.long_asc_node_rate_rdpcty = self.long_asc_node_rate_dgpcty*(math.pi/180.0)
               self.b =  -0.00041348
               self.c =   0.68346318
               self.s =  -0.10162547
               self.f =   7.67025000
          elif name == 'pluto':
               self.name = name
               self.gm_km3ps2 = 1.108e12/(math.pow(1000.0,3))
               self.semi_major_axis0_au = 39.48686035
               self.semi_major_axis_rate_aupcty =  0.00449751
               self.ecc0 = 0.24885238
               self.ecc_rate_pcty =  0.00006016
               self.incl0_dg = 17.14104260
               self.incl0_rd = self.incl0_dg*(math.pi/180.0)
               self.incl_rate_dgpcty =  0.00000501
               self.incl_rate_rdpcty = self.incl_rate_dgpcty*(math.pi/180.0)
               self.mean_long0_dg = 238.96535011
               self.mean_long0_rd = self.mean_long0_dg*(math.pi/180.0)
               self.mean_long_rate_dgpcty =    145.18042903
               self.mean_long_rate_rdpcty = self.mean_long_rate_dgpcty*(math.pi/180.0)
               self.long_perh0_dg = 224.09702598
               self.long_perh0_rd = self.long_perh0_dg*(math.pi/180.0)
               self.long_perh_rate_dgpcty = -0.00968827
               self.long_perh_rate_rdpcty = self.long_perh_rate_dgpcty*(math.pi/180.0)
               self.long_asc_node0_dg = 110.30167986
               self.long_asc_node0_rd = self.long_asc_node0_dg*(math.pi/180.0)
               self.long_asc_node_rate_dgpcty = -0.00809981
               self.long_asc_node_rate_rdpcty = self.long_asc_node_rate_dgpcty*(math.pi/180.0)
               self.b =  -0.01262724
               self.c =   0.0e0
               self.s =   0.0e0
               self.f =   0.0e0
          else:
            print('Incorrect planet name')

#--------------------------------------------------------------------------------------------------------
      def prnt_planet_name(self):
          print('Planet =',self.name,'------------------------------------------------------')

#--------------------------------------------------------------------------------------------------------
      def prnt_planet_data(self):
          print ("{0} semi_major_axis0_au         = {1:.8f}".format(self.name,self.semi_major_axis0_au))
          print ("{0} semi_major_axis_rate_aupcty = {1:.8f}".format(self.name,self.semi_major_axis_rate_aupcty))
          print ("{0} ecc0                        = {1:.8f}".format(self.name,self.ecc0))
          print ("{0} ecc_rate_pcty               = {1:.8f}".format(self.name,self.ecc_rate_pcty))
          print ("{0} incl0_dg                    = {1:.8f}".format(self.name,self.incl0_dg))
          print ("{0} incl_rate_dgpcty            = {1:.8f}".format(self.name,self.incl_rate_dgpcty))
          print ("{0} mean_long0_dg               = {1:.8f}".format(self.name,self.mean_long0_dg))
          print ("{0} mean_long_rate_dgpcty       = {1:.8f}".format(self.name,self.mean_long_rate_dgpcty))
          print ("{0} long_perh0_dg               = {1:.8f}".format(self.name,self.long_perh0_dg))
          print ("{0} long_perh_rate_dgpcty       = {1:.8f}".format(self.name,self.long_perh_rate_dgpcty))
          print ("{0} long_asc_node0_dg           = {1:.8f}".format(self.name,self.long_asc_node0_dg))
          print ("{0} long_asc_node_rate_dgpcty   = {1:.8f}".format(self.name,self.long_asc_node_rate_dgpcty))
          print ("{0} b                           = {1:.8f}".format(self.name,self.b))
          print ("{0} c                           = {1:.8f}".format(self.name,self.c))
          print ("{0} s                           = {1:.8f}".format(self.name,self.s))
          print ("{0} f                           = {1:.8f}".format(self.name,self.f))

#--------------------------------------------------------------------------------------------------------
      def prnt_planet_pos(self, jd, mo, d, y, h, mi, s):
          #print jd, y, mo, d, h, mi, s, self.x_ecl_au, self.y_ecl_au, self.z_ecl_au
          print ("%20.9f, %i-%i-%i %i:%i:%15.12f, %20.14f, %20.14f, %20.14f, %20.14f, %20.14f, %20.14f" % \
                 (jd, y, mo, d, h, mi, s, self.pos_km[0], self.pos_km[1], self.pos_km[2], \
                  self.vel_kmps[0], self.vel_kmps[1], self.vel_kmps[2]))

#--------------------------------------------------------------------------------------------------------
      def update_planet_pos(self, jd):
    #     calculate number of centuries past j2000
          self.no_cty_past_j2000 = (jd - 2451545.0)/36525.0
    #     calculate the curve fit orbital parameters
          self.semi_major_axis_au = self.semi_major_axis0_au + \
                                    self.semi_major_axis_rate_aupcty *self.no_cty_past_j2000
          self.ecc = self.ecc0 + self.ecc_rate_pcty*self.no_cty_past_j2000
          self.incl_dg = self.incl0_dg + self.incl_rate_dgpcty*self.no_cty_past_j2000
          self.mean_long_dg = self.mean_long0_dg + self.mean_long_rate_dgpcty*self.no_cty_past_j2000
          self.long_perh_dg = self.long_perh0_dg + self.long_perh_rate_dgpcty*self.no_cty_past_j2000
          self.long_asc_node_dg = self.long_asc_node0_dg + self.long_asc_node_rate_dgpcty*self.no_cty_past_j2000
    #     modulus mean longitude 
          self.mean_long_dg = math.fmod(self.mean_long_dg,360)
    #     convert semi major axis from au to km
          self.semi_major_axis_km = self.semi_major_axis_au*self.autkm
    #     convert angles from deg to radians
          self.incl_rd          = self.incl_dg*self.dtr
          self.mean_long_rd     = self.mean_long_dg*self.dtr
          self.long_perh_rd     = self.long_perh_dg*self.dtr
          self.long_asc_node_rd = self.long_asc_node_dg*self.dtr
    # Comput the argument of perihelion and the mean anomaly
          self.arg_perh_dg = self.long_perh_dg - self.long_asc_node_dg
          self.arg_perh_rd = self.arg_perh_dg*self.dtr
          self.mean_anomaly_dg = self.mean_long_dg - self.long_perh_dg + \
                                 self.b*self.no_cty_past_j2000*self.no_cty_past_j2000 + \
                                 self.c*math.cos(self.f*self.no_cty_past_j2000) + \
                                 self.s*math.sin(self.f*self.no_cty_past_j2000)
          self.mean_anomaly_dg = math.fmod(self.mean_anomaly_dg,360.0)
    
          if (self.mean_anomaly_dg < -180.0):
                self.mean_anomaly_dg = self.mean_anomaly_dg + 360.0
          elif (self.mean_anomaly_dg > 180.0):
                self.mean_anomaly_dg = self.mean_anomaly_dg - 360.0
    
          self.mean_anomaly_rd = self.mean_anomaly_dg*self.dtr

    # Solve Kepler's Equation
          self.ecc_anomaly_dg =self.mean_anomaly_dg + self.rtd*self.ecc*math.sin(self.mean_anomaly_dg*self.dtr)
          self.delta_ecc_anomaly_dg = 1.0
          self.ecc_error_tol = 1.0e-09
          self.n = 0
    
    #  loop until error is small
          while math.fabs(self.delta_ecc_anomaly_dg) > self.ecc_error_tol:
            self.n = self.n + 1
            self.delta_mean_anomaly_dg = self.mean_anomaly_dg - (self.ecc_anomaly_dg - \
                                         self.rtd*self.ecc*math.sin(self.ecc_anomaly_dg*self.dtr))
            self.tmp_var_1 = (self.ecc_anomaly_dg - self.rtd*self.ecc*math.sin(self.mean_anomaly_dg*self.dtr))
            self.delta_ecc_anomaly_dg = self.delta_mean_anomaly_dg/ \
                                        (1.0 - self.ecc*math.cos(self.ecc_anomaly_dg*self.dtr))
            self.ecc_anomaly_dg = self.ecc_anomaly_dg + self.delta_ecc_anomaly_dg
            self.ecc_anomaly_rd = self.ecc_anomaly_dg*self.dtr

    #   Compute the planets heliocentric coordinates in its orbital plane, r', 
    #    with the x'-axis aligned from the focus to the perihelion
    
          self.x_prime = self.semi_major_axis_au*(math.cos(self.ecc_anomaly_dg*self.dtr) - self.ecc)
          self.y_prime = self.semi_major_axis_au*math.sqrt(1.0 - \
                               self.ecc*self.ecc)*math.sin(self.ecc_anomaly_dg*self.dtr)
          self.z_prime = 0.0e0
    
    #   Compute the coordinates, recl, in the J2000 ecliptic plane, with the x-axis aligned towrard the equinox:
    
          self.x_ecl_au = (math.cos(self.arg_perh_rd)*math.cos(self.long_asc_node_rd) - \
                  math.sin(self.arg_perh_rd)*math.sin(self.long_asc_node_rd)* \
                  math.cos(self.incl_rd))*self.x_prime + \
                  (-1.0*math.sin(self.arg_perh_rd)*math.cos(self.long_asc_node_rd) - \
                  math.cos(self.arg_perh_rd)*math.sin(self.long_asc_node_rd)* \
                  math.cos(self.incl_rd))*self.y_prime
    
          self.y_ecl_au = (math.cos(self.arg_perh_rd)*math.sin(self.long_asc_node_rd) + \
                  math.sin(self.arg_perh_rd)*math.cos(self.long_asc_node_rd)* \
                  math.cos(self.incl_rd))*self.x_prime + \
                  (-1.0*math.sin(self.arg_perh_rd)*math.sin(self.long_asc_node_rd) + \
                  math.cos(self.arg_perh_rd)*math.cos(self.long_asc_node_rd)* \
                  math.cos(self.incl_rd))*self.y_prime
    
          self.z_ecl_au = math.sin(self.arg_perh_rd)*math.sin(self.incl_rd)*self.x_prime +  \
                     math.cos(self.arg_perh_rd)*math.sin(self.incl_rd)*self.y_prime
    
          self.pos_km[0] = self.x_ecl_au*self.autkm
          self.pos_km[1] = self.y_ecl_au*self.autkm
          self.pos_km[2] = self.z_ecl_au*self.autkm

#--------------------------------------------------------------------------------------------------------
      def update_planet_vel(self, jd, central_star):
    #   Compute the heliocentric velocity components:

    #    compute true anomaly
          self.slr_km = self.semi_major_axis_km*(1.0 - math.pow(self.ecc,2.0))
          self.true_anomaly_term1 = math.sqrt(1.0 + self.ecc)*math.sin(self.ecc_anomaly_rd/2.0)
          self.true_anomaly_term2 = math.sqrt(1.0 - self.ecc)*math.cos(self.ecc_anomaly_rd/2.0)
          self.true_anomaly_rd = 2.0*math.atan2(self.true_anomaly_term1, self.true_anomaly_term2)
          self.true_anomaly_dg = self.true_anomaly_rd*180.0/math.pi

    #    compute the orbital plane velocity components
          cs_gm_km3ps2 = central_star.get_central_star_gm_km3ps2()
          self.xd_op_kmps = -1.0*math.sqrt(cs_gm_km3ps2/self.slr_km)*math.sin(self.true_anomaly_rd) 
          self.yd_op_kmps = math.sqrt(cs_gm_km3ps2/self.slr_km)*(self.ecc + math.cos(self.true_anomaly_rd))
          self.zd_op_kmps = 0.0e0


    #    compute the transformation matrix from orbital plane to heliocentric ecliptic plane
          self.T11 = (     math.cos(self.long_asc_node_rd)*math.cos(self.arg_perh_rd)) - \
                     (     math.sin(self.long_asc_node_rd)*math.sin(self.arg_perh_rd)*math.cos(self.incl_rd))
          self.T12 = (-1.0*math.cos(self.long_asc_node_rd)*math.sin(self.arg_perh_rd)) - \
                     (     math.sin(self.long_asc_node_rd)*math.cos(self.arg_perh_rd)*math.cos(self.incl_rd))
          self.T13 =       math.sin(self.long_asc_node_rd)*math.sin(self.incl_rd)
          self.T21 = (     math.sin(self.long_asc_node_rd)*math.cos(self.arg_perh_rd)) + \
                     (     math.cos(self.long_asc_node_rd)*math.sin(self.arg_perh_rd)*math.cos(self.incl_rd))
          self.T22 = (-1.0*math.sin(self.long_asc_node_rd)*math.sin(self.arg_perh_rd)) + \
                     (     math.cos(self.long_asc_node_rd)*math.cos(self.arg_perh_rd)*math.cos(self.incl_rd))
          self.T23 =  -1.0*math.cos(self.long_asc_node_rd)*math.sin(self.incl_rd)
          self.T31 = math.sin(self.arg_perh_rd)*math.sin(self.incl_rd)
          self.T32 = math.cos(self.arg_perh_rd)*math.sin(self.incl_rd)
          self.T33 = math.cos(self.incl_rd)

    #    transform velocity componets from oribital plane coordinates to heliocentric ecliptic coordinates
          self.vel_kmps[0] = (self.T11*self.xd_op_kmps) + (self.T12*self.yd_op_kmps) + (self.T13*self.zd_op_kmps)
          self.vel_kmps[1] = (self.T21*self.xd_op_kmps) + (self.T22*self.yd_op_kmps) + (self.T23*self.zd_op_kmps)
          self.vel_kmps[2] = (self.T31*self.xd_op_kmps) + (self.T32*self.yd_op_kmps) + (self.T33*self.zd_op_kmps)
          self.tot_vel_kmps = math.sqrt(self.vel_kmps[0]*self.vel_kmps[0] + \
                                        self.vel_kmps[1]*self.vel_kmps[1] + \
                                        self.vel_kmps[2]*self.vel_kmps[2])

#--------------------------------------------------------------------------------------------------------
      def get_planet_pos(self):
          return self.pos_km
#--------------------------------------------------------------------------------------------------------
      def get_planet_vel(self):
          return self.vel_kmps
#--------------------------------------------------------------------------------------------------------
      def get_planet_totvel(self):
          return self.tot_vel_kmps
#--------------------------------------------------------------------------------------------------------
      def get_planet_gm(self):
          return self.gm_km3ps2
