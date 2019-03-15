#!/usr/bin/python2.7
import math, csv, os, sys, string
from pylab import *

# Initialize start date and time and get Julian Date

import dandtclass
import planet
import central_star
import small_object

start_date_time = dandtclass.dandt( 2001, 9, 23, 00, 3, 0.0)
start_date_time.getJD()

dt_inc_hours =  0.0
dt_inc_mins  =  0.0
dt_inc_secs  =  30.00
dt_days = (dt_inc_hours + dt_inc_mins/60.0 + dt_inc_secs/3600.0)/24.0
dt_hours = dt_inc_hours + dt_inc_mins/60.0 + dt_inc_secs/3600.0
dt_mins = dt_inc_hours*60.0 + dt_inc_mins + dt_inc_secs/60.0
dt_secs = dt_inc_hours*3600.0 + dt_inc_mins*60.0 + dt_inc_secs
stop_time_days = 5.0

mission_time_secs = 0.0e0

print_dt_secs = 0.05*60.0*60.0
print_dt_mins = print_dt_secs/60.0
print_dt_hours = print_dt_mins/60.0
print_dt_days = print_dt_hours/24.0
print_counter_days = print_dt_days - dt_days

sun = central_star.central_star(1.32712440018e20)
mercury = planet.planet('mercury')
venus = planet.planet('venus')
earth = planet.planet('earth')
mars = planet.planet('mars')
jupiter = planet.planet('jupiter')
saturn = planet.planet('saturn')
uranus = planet.planet('uranus')
neptune = planet.planet('neptune')
pluto = planet.planet('pluto')

#ss1 = small_object.small_object(150110893.196, 60179.2, -181.7379, -0.45000, 28.5, 0.0, 1.0)
ss1 = small_object.small_object('ss1',150000893.196, 40179.2, -181.7379, -1.21000, 33.5, 0.0, 1.0)
ss2 = small_object.small_object('ss2',150000893.196, 42179.2, -181.7379,  4.50000, 31.0, 0.0, 1.0)

current_date_time = dandtclass.dandt( 2001, 9, 23, 00, 3,  0.0)
current_date_time.getJD()
current_date_time.getDate_from_JD(current_date_time.jd)
mercury.update_planet_pos(current_date_time.jd)

print "number = 31"
print "jd, mer_x, mer_y, mer_z, ven_x, ven_y, ven_z, ear_x, ear_y, ear_z, mar_x, mar_y, mar_z, \
           jup_x, jup_y, jup_z, sar_x, sat_y, say_z, urn_x, urn_y, urn_z, nep_x, nep_y, nep_z, \
           plu_x, plu_y, plu_z, ss1_x, ss1_y, ss1_z, ss2_x, ss2_y, ss2_z"

while current_date_time.jd < start_date_time.jd + stop_time_days:

   current_date_time.update_jd(dt_days)
   current_date_time.getDate_from_JD(current_date_time.jd)
   mission_time_secs = mission_time_secs + dt_secs

#   mercury.update_planet_pos(current_date_time.jd)
#   venus.update_planet_pos(current_date_time.jd)
#   earth.update_planet_pos(current_date_time.jd)
#   mars.update_planet_pos(current_date_time.jd)
#   jupiter.update_planet_pos(current_date_time.jd)
#   saturn.update_planet_pos(current_date_time.jd)
#   uranus.update_planet_pos(current_date_time.jd)
#   neptune.update_planet_pos(current_date_time.jd)
#   pluto.update_planet_pos(current_date_time.jd)


   ss1.update_states(current_date_time,dt_secs,sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,pluto)
   ss2.update_states(current_date_time,dt_secs,sun,mercury,venus,earth,mars,jupiter,saturn,uranus,neptune,pluto)

   if print_counter_days >= print_dt_days:
      print_counter_days = 0.0

      print ("%20.9f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f \
             %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f \
             %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f %20.14f \
             %20.14f %20.14f %20.14f %20.14f" \
             % ( current_date_time.jd, mercury.pos_km[0], mercury.pos_km[1], mercury.pos_km[2], \
                                                  venus.pos_km[0],   venus.pos_km[1],   venus.pos_km[2], \
                                                  earth.pos_km[0],   earth.pos_km[1],   earth.pos_km[2], \
                                                   mars.pos_km[0],    mars.pos_km[1],    mars.pos_km[2], \
                                                jupiter.pos_km[0], jupiter.pos_km[1], jupiter.pos_km[2], \
                                                 saturn.pos_km[0],  saturn.pos_km[1],  saturn.pos_km[2], \
                                                 uranus.pos_km[0],  uranus.pos_km[1],  uranus.pos_km[2], \
                                                neptune.pos_km[0], neptune.pos_km[1], neptune.pos_km[2], \
                                                  pluto.pos_km[0],   pluto.pos_km[1],   pluto.pos_km[2], \
                                                    ss1.pos_km[0],     ss1.pos_km[1],     ss1.pos_km[2], \
                                                    ss2.pos_km[0],     ss2.pos_km[1],     ss2.pos_km[2]))

   else:
      print_counter_days = print_counter_days + dt_days
