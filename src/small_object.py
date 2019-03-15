import math, csv, os, sys, string
from pylab import *

import planet
import central_star
import dandtclass

#---------------------------------------------------------------------------------------------------------------
class small_object:
      def __init__(self,name,x_km,y_km,z_km,xd_kmps,yd_kmps,zd_kmps,mass_kg):

          self.name = name
          self.dtr = math.pi/180.0
          self.rtd = 180.0/math.pi
          self.autkm = 149597870.691

          self.pos_km             = [x_km, y_km, z_km]
          self.vel_kmps           = [xd_kmps, yd_kmps, zd_kmps]
          self.acl_grav_kmps2     = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_sun_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_mer_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_ven_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_ear_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_mar_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_jup_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_sat_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_urn_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_nep_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.acl_grav_plu_kmps2 = [0.0e0, 0.0e0, 0.0e0]
          self.mass_kg            = mass_kg


          extension = '.output'
          filename = self.name + extension
          self.f = open(filename, 'w')

#--------------------------------------------------------------------------------------------------------------
      def calc_grav_from_bodies(self, jd, sun, mer, ven, ear, mar, jup, sat, urn, nep, plu, pos):
    #    calculate grav acceleration from each planet and sun on the small_oject
          mer.update_planet_pos(jd)
          ven.update_planet_pos(jd)
          ear.update_planet_pos(jd)
          mar.update_planet_pos(jd)
          jup.update_planet_pos(jd)
          sat.update_planet_pos(jd)
          urn.update_planet_pos(jd)
          nep.update_planet_pos(jd)
          plu.update_planet_pos(jd)

          #  Sun Accel Grav on Small Object
          self.rx_sun_so = -1.0*pos[0]
          self.ry_sun_so = -1.0*pos[1]
          self.rz_sun_so = -1.0*pos[2]
          self.rmag_sun_so = math.sqrt(self.rx_sun_so*self.rx_sun_so + self.ry_sun_so*self.ry_sun_so + \
                                       self.rz_sun_so*self.rz_sun_so)
          self.ux_sun_so = self.rx_sun_so/self.rmag_sun_so
          self.uy_sun_so = self.ry_sun_so/self.rmag_sun_so
          self.uz_sun_so = self.rz_sun_so/self.rmag_sun_so
          self.acl_grav_sun_kmps2[0] = -1.0*sun.get_central_star_gm()*self.ux_sun_so/ \
                                           (self.rmag_sun_so*self.rmag_sun_so)
          self.acl_grav_sun_kmps2[1] = -1.0*sun.get_central_star_gm()*self.uy_sun_so/ \
                                           (self.rmag_sun_so*self.rmag_sun_so)
          self.acl_grav_sun_kmps2[2] = -1.0*sun.get_central_star_gm()*self.uz_sun_so/ \
                                           (self.rmag_sun_so*self.rmag_sun_so)

          #  Mercury Accel Grav on Small Object
          planet_pos = mer.get_planet_pos()
          self.rx_mer_so = pos[0] - planet_pos[0]
          self.ry_mer_so = pos[1] - planet_pos[1]
          self.rz_mer_so = pos[2] - planet_pos[2]
          self.rmag_mer_so = math.sqrt(self.rx_mer_so*self.rx_mer_so + self.ry_mer_so*self.ry_mer_so + \
                                       self.rz_mer_so*self.rz_mer_so)
          self.ux_mer_so = self.rx_mer_so/self.rmag_mer_so
          self.uy_mer_so = self.ry_mer_so/self.rmag_mer_so
          self.uz_mer_so = self.rz_mer_so/self.rmag_mer_so
          self.acl_grav_mer_kmps2[0] = -1.0*mer.get_planet_gm()*self.ux_mer_so/ \
                                           (self.rmag_mer_so*self.rmag_mer_so)
          self.acl_grav_mer_kmps2[1] = -1.0*mer.get_planet_gm()*self.uy_mer_so/ \
                                           (self.rmag_mer_so*self.rmag_mer_so)
          self.acl_grav_mer_kmps2[2] = -1.0*mer.get_planet_gm()*self.uz_mer_so/ \
                                           (self.rmag_mer_so*self.rmag_mer_so)

          #  Venus Accel Grav on Small Object
          planet_pos = ven.get_planet_pos()
          self.rx_ven_so = pos[0] -planet_pos[0]
          self.ry_ven_so = pos[1] -planet_pos[1]
          self.rz_ven_so = pos[2] -planet_pos[2]
          self.rmag_ven_so = math.sqrt(self.rx_ven_so*self.rx_ven_so + self.ry_ven_so*self.ry_ven_so + \
                                       self.rz_ven_so*self.rz_ven_so)
          self.ux_ven_so = self.rx_ven_so/self.rmag_ven_so
          self.uy_ven_so = self.ry_ven_so/self.rmag_ven_so
          self.uz_ven_so = self.rz_ven_so/self.rmag_ven_so
          self.acl_grav_ven_kmps2[0] = -1.0*ven.get_planet_gm()*self.ux_ven_so/ \
                                           (self.rmag_ven_so*self.rmag_ven_so)
          self.acl_grav_ven_kmps2[1] = -1.0*ven.get_planet_gm()*self.uy_ven_so/ \
                                           (self.rmag_ven_so*self.rmag_ven_so)
          self.acl_grav_ven_kmps2[2] = -1.0*ven.get_planet_gm()*self.uz_ven_so/ \
                                           (self.rmag_ven_so*self.rmag_ven_so)

          #  Earth Accel Grav on Small Object
          planet_pos = ear.get_planet_pos()
          self.rx_ear_so = pos[0] - planet_pos[0]
          self.ry_ear_so = pos[1] - planet_pos[1]
          self.rz_ear_so = pos[2] - planet_pos[2]
          self.rmag_ear_so = math.sqrt(self.rx_ear_so*self.rx_ear_so + self.ry_ear_so*self.ry_ear_so + \
                                       self.rz_ear_so*self.rz_ear_so)
          self.ux_ear_so = self.rx_ear_so/self.rmag_ear_so
          self.uy_ear_so = self.ry_ear_so/self.rmag_ear_so
          self.uz_ear_so = self.rz_ear_so/self.rmag_ear_so
          self.acl_grav_ear_kmps2[0] = -1.0*ear.get_planet_gm()*self.ux_ear_so/ \
                                           (self.rmag_ear_so*self.rmag_ear_so)
          self.acl_grav_ear_kmps2[1] = -1.0*ear.get_planet_gm()*self.uy_ear_so/ \
                                           (self.rmag_ear_so*self.rmag_ear_so)
          self.acl_grav_ear_kmps2[2] = -1.0*ear.get_planet_gm()*self.uz_ear_so/ \
                                           (self.rmag_ear_so*self.rmag_ear_so)

          #  Mars Accel Grav on Small Object
          planet_pos = mar.get_planet_pos()
          self.rx_mar_so = pos[0] - planet_pos[0]
          self.ry_mar_so = pos[1] - planet_pos[1]
          self.rz_mar_so = pos[2] - planet_pos[2]
          self.rmag_mar_so = math.sqrt(self.rx_mar_so*self.rx_mar_so + self.ry_mar_so*self.ry_mar_so + \
                                       self.rz_mar_so*self.rz_mar_so)
          self.ux_mar_so = self.rx_mar_so/self.rmag_mar_so
          self.uy_mar_so = self.ry_mar_so/self.rmag_mar_so
          self.uz_mar_so = self.rz_mar_so/self.rmag_mar_so
          self.acl_grav_mar_kmps2[0] = -1.0*mar.get_planet_gm()*self.ux_mar_so/ \
                                           (self.rmag_mar_so*self.rmag_mar_so)
          self.acl_grav_mar_kmps2[1] = -1.0*mar.get_planet_gm()*self.uy_mar_so/ \
                                           (self.rmag_mar_so*self.rmag_mar_so)
          self.acl_grav_mar_kmps2[2] = -1.0*mar.get_planet_gm()*self.uz_mar_so/ \
                                           (self.rmag_mar_so*self.rmag_mar_so)

          #  Jupiter Accel Grav on Small Object
          planet_pos = jup.get_planet_pos()
          self.rx_jup_so = pos[0] - planet_pos[0]
          self.ry_jup_so = pos[1] - planet_pos[1]
          self.rz_jup_so = pos[2] - planet_pos[2]
          self.rmag_jup_so = math.sqrt(self.rx_jup_so*self.rx_jup_so + self.ry_jup_so*self.ry_jup_so + \
                                       self.rz_jup_so*self.rz_jup_so)
          self.ux_jup_so = self.rx_jup_so/self.rmag_jup_so
          self.uy_jup_so = self.ry_jup_so/self.rmag_jup_so
          self.uz_jup_so = self.rz_jup_so/self.rmag_jup_so
          self.acl_grav_jup_kmps2[0] = -1.0*jup.get_planet_gm()*self.ux_jup_so/ \
                                           (self.rmag_jup_so*self.rmag_jup_so)
          self.acl_grav_jup_kmps2[1] = -1.0*jup.get_planet_gm()*self.uy_jup_so/ \
                                           (self.rmag_jup_so*self.rmag_jup_so)
          self.acl_grav_jup_kmps2[2] = -1.0*jup.get_planet_gm()*self.uz_jup_so/ \
                                           (self.rmag_jup_so*self.rmag_jup_so)

          #  Saturn Accel Grav on Small Object
          planet_pos = sat.get_planet_pos()
          self.rx_sat_so = pos[0] - planet_pos[0]
          self.ry_sat_so = pos[1] - planet_pos[1]
          self.rz_sat_so = pos[2] - planet_pos[2]
          self.rmag_sat_so = math.sqrt(self.rx_sat_so*self.rx_sat_so + self.ry_sat_so*self.ry_sat_so + \
                                       self.rz_sat_so*self.rz_sat_so)
          self.ux_sat_so = self.rx_sat_so/self.rmag_sat_so
          self.uy_sat_so = self.ry_sat_so/self.rmag_sat_so
          self.uz_sat_so = self.rz_sat_so/self.rmag_sat_so
          self.acl_grav_sat_kmps2[0] = -1.0*sat.get_planet_gm()*self.ux_sat_so/ \
                                           (self.rmag_sat_so*self.rmag_sat_so)
          self.acl_grav_sat_kmps2[1] = -1.0*sat.get_planet_gm()*self.uy_sat_so/ \
                                           (self.rmag_sat_so*self.rmag_sat_so)
          self.acl_grav_sat_kmps2[2] = -1.0*sat.get_planet_gm()*self.uz_sat_so/ \
                                           (self.rmag_sat_so*self.rmag_sat_so)

          #  Uranus Accel Grav on Small Object
          planet_pos = urn.get_planet_pos()
          self.rx_urn_so = pos[0] - planet_pos[0]
          self.ry_urn_so = pos[1] - planet_pos[1]
          self.rz_urn_so = pos[2] - planet_pos[2]
          self.rmag_urn_so = math.sqrt(self.rx_urn_so*self.rx_urn_so + self.ry_urn_so*self.ry_urn_so + \
                                       self.rz_urn_so*self.rz_urn_so)
          self.ux_urn_so = self.rx_urn_so/self.rmag_urn_so
          self.uy_urn_so = self.ry_urn_so/self.rmag_urn_so
          self.uz_urn_so = self.rz_urn_so/self.rmag_urn_so
          self.acl_grav_urn_kmps2[0] = -1.0*urn.get_planet_gm()*self.ux_urn_so/ \
                                           (self.rmag_urn_so*self.rmag_urn_so)
          self.acl_grav_urn_kmps2[0] = -1.0*urn.get_planet_gm()*self.uy_urn_so/ \
                                           (self.rmag_urn_so*self.rmag_urn_so)
          self.acl_grav_urn_kmps2[0] = -1.0*urn.get_planet_gm()*self.uz_urn_so/ \
                                           (self.rmag_urn_so*self.rmag_urn_so)

          #  Neptune Accel Grav on Small Object
          planet_pos = nep.get_planet_pos()
          self.rx_nep_so = pos[0] - planet_pos[0]
          self.ry_nep_so = pos[1] - planet_pos[1]
          self.rz_nep_so = pos[2] - planet_pos[2]
          self.rmag_nep_so = math.sqrt(self.rx_nep_so*self.rx_nep_so + self.ry_nep_so*self.ry_nep_so + \
                                       self.rz_nep_so*self.rz_nep_so)
          self.ux_nep_so = self.rx_nep_so/self.rmag_nep_so
          self.uy_nep_so = self.ry_nep_so/self.rmag_nep_so
          self.uz_nep_so = self.rz_nep_so/self.rmag_nep_so
          self.acl_grav_nep_kmps2[0] = -1.0*nep.get_planet_gm()*self.ux_nep_so/ \
                                           (self.rmag_nep_so*self.rmag_nep_so)
          self.acl_grav_nep_kmps2[1] = -1.0*nep.get_planet_gm()*self.uy_nep_so/ \
                                           (self.rmag_nep_so*self.rmag_nep_so)
          self.acl_grav_nep_kmps2[2] = -1.0*nep.get_planet_gm()*self.uz_nep_so/ \
                                           (self.rmag_nep_so*self.rmag_nep_so)

          #  Pluto Accel Grav on Small Object
          planet_pos = plu.get_planet_pos()
          self.rx_plu_so = pos[0] - planet_pos[0]
          self.ry_plu_so = pos[1] - planet_pos[1]
          self.rz_plu_so = pos[2] - planet_pos[2]
          self.rmag_plu_so = math.sqrt(self.rx_plu_so*self.rx_plu_so + self.ry_plu_so*self.ry_plu_so + \
                                       self.rz_plu_so*self.rz_plu_so)
          self.ux_plu_so = self.rx_plu_so/self.rmag_plu_so
          self.uy_plu_so = self.ry_plu_so/self.rmag_plu_so
          self.uz_plu_so = self.rz_plu_so/self.rmag_plu_so
          self.acl_grav_plu_kmps2[0] = -1.0*plu.get_planet_gm()*self.ux_plu_so/ \
                                           (self.rmag_plu_so*self.rmag_plu_so)
          self.acl_grav_plu_kmps2[1] = -1.0*plu.get_planet_gm()*self.uy_plu_so/ \
                                           (self.rmag_plu_so*self.rmag_plu_so)
          self.acl_grav_plu_kmps2[2] = -1.0*plu.get_planet_gm()*self.uz_plu_so/ \
                                           (self.rmag_plu_so*self.rmag_plu_so)

          self.acl_grav_kmps2[0] = self.acl_grav_sun_kmps2[0] + self.acl_grav_mer_kmps2[0] + \
                                   self.acl_grav_ven_kmps2[0] + self.acl_grav_ear_kmps2[0] + \
                                   self.acl_grav_mar_kmps2[0] + self.acl_grav_jup_kmps2[0] + \
                                   self.acl_grav_sat_kmps2[0] + self.acl_grav_urn_kmps2[0] + \
                                   self.acl_grav_nep_kmps2[0] + self.acl_grav_plu_kmps2[0]
          self.acl_grav_kmps2[1] = self.acl_grav_sun_kmps2[1] + self.acl_grav_mer_kmps2[1] + \
                                   self.acl_grav_ven_kmps2[1] + self.acl_grav_ear_kmps2[1] + \
                                   self.acl_grav_mar_kmps2[1] + self.acl_grav_jup_kmps2[1] + \
                                   self.acl_grav_sat_kmps2[1] + self.acl_grav_urn_kmps2[1] + \
                                   self.acl_grav_nep_kmps2[1] + self.acl_grav_plu_kmps2[1]
          self.acl_grav_kmps2[2] = self.acl_grav_sun_kmps2[2] + self.acl_grav_mer_kmps2[2] + \
                                   self.acl_grav_ven_kmps2[2] + self.acl_grav_ear_kmps2[2] + \
                                   self.acl_grav_mar_kmps2[2] + self.acl_grav_jup_kmps2[2] + \
                                   self.acl_grav_sat_kmps2[2] + self.acl_grav_urn_kmps2[2] + \
                                   self.acl_grav_nep_kmps2[2] + self.acl_grav_plu_kmps2[2]

#-------------------------------------------------------------------------------------------------------------
      def update_states(self, cdat, dt_secs, sun, mer, ven, ear, mar, jup, sat, urn, nep, plu):

          self.calc_grav_from_bodies(cdat.jd, sun, mer, ven, ear, mar, jup, sat, urn, nep, plu, self.pos_km)

          self.k1_x = dt_secs*self.vel_kmps[0]
          self.k1_y = dt_secs*self.vel_kmps[1]
          self.k1_z = dt_secs*self.vel_kmps[2]
          self.k1_xd = dt_secs*self.acl_grav_kmps2[0]
          self.k1_yd = dt_secs*self.acl_grav_kmps2[1]
          self.k1_zd = dt_secs*self.acl_grav_kmps2[2]

          jd_mid = cdat.jd + (dt_secs*0.5)/(60.0*60.0*24.0)
          pos_mid_1 = [self.pos_km[0] + 0.5*self.k1_x, \
                       self.pos_km[1] + 0.5*self.k1_y, \
                       self.pos_km[2] + 0.5*self.k1_z]
          self.calc_grav_from_bodies(jd_mid, sun, mer, ven, ear, mar, jup, sat, urn, nep, plu, pos_mid_1)

          self.k2_x = dt_secs*(self.vel_kmps[0] + 0.5*self.k1_xd)
          self.k2_y = dt_secs*(self.vel_kmps[1] + 0.5*self.k1_yd)
          self.k2_z = dt_secs*(self.vel_kmps[2] + 0.5*self.k1_zd)
          self.k2_xd = dt_secs*self.acl_grav_kmps2[0]
          self.k2_yd = dt_secs*self.acl_grav_kmps2[1]
          self.k2_zd = dt_secs*self.acl_grav_kmps2[2]


          pos_mid_2 = [self.pos_km[0] + 0.5*self.k2_x, \
                       self.pos_km[1] + 0.5*self.k2_y, \
                       self.pos_km[2] + 0.5*self.k2_z]
          self.calc_grav_from_bodies(jd_mid, sun, mer, ven, ear, mar, jup, sat, urn, nep, plu, pos_mid_2) 

          self.k3_x = dt_secs*(self.vel_kmps[0] + 0.5*self.k2_xd)
          self.k3_y = dt_secs*(self.vel_kmps[1] + 0.5*self.k2_yd)
          self.k3_z = dt_secs*(self.vel_kmps[2] + 0.5*self.k2_zd)
          self.k3_xd = dt_secs*self.acl_grav_kmps2[0]
          self.k3_yd = dt_secs*self.acl_grav_kmps2[1]
          self.k3_zd = dt_secs*self.acl_grav_kmps2[2]

          jd_end = cdat.jd + (dt_secs)/(60.0*60.0*24.0)
          pos_mid_3 = [self.pos_km[0] + self.k3_x, \
                       self.pos_km[1] + self.k3_y, \
                       self.pos_km[2] + self.k3_z]
          self.calc_grav_from_bodies(jd_end, sun, mer, ven, ear, mar, jup, sat, urn, nep, plu, pos_mid_3)

          self.k4_x = dt_secs*(self.vel_kmps[0] + self.k3_xd)
          self.k4_y = dt_secs*(self.vel_kmps[1] + self.k3_yd)
          self.k4_z = dt_secs*(self.vel_kmps[2] + self.k3_zd)
          self.k4_xd = dt_secs*self.acl_grav_kmps2[0]
          self.k4_yd = dt_secs*self.acl_grav_kmps2[1]
          self.k4_zd = dt_secs*self.acl_grav_kmps2[2]

          self.pos_km[0] = self.pos_km[0] + ((self.k1_x + 2.0*self.k2_x + 2.0*self.k3_x + self.k4_x)/6.0)
          self.pos_km[1] = self.pos_km[1] + ((self.k1_y + 2.0*self.k2_y + 2.0*self.k3_y + self.k4_y)/6.0)
          self.pos_km[2] = self.pos_km[2] + ((self.k1_z + 2.0*self.k2_z + 2.0*self.k3_z + self.k4_z)/6.0)
          self.vel_kmps[0] = self.vel_kmps[0] + ((self.k1_xd + 2.0*self.k2_xd + 2.0*self.k3_xd + self.k4_xd)/6.0)
          self.vel_kmps[1] = self.vel_kmps[1] + ((self.k1_yd + 2.0*self.k2_yd + 2.0*self.k3_yd + self.k4_yd)/6.0)
          self.vel_kmps[2] = self.vel_kmps[2] + ((self.k1_zd + 2.0*self.k2_zd + 2.0*self.k3_zd + self.k4_zd)/6.0)

#-------------------------------------------------------------------------------------------------------------
      def closefile(self):
          self.f.close()
