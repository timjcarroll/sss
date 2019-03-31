import math, csv, os, sys, string
#from pylab import *

class dandt:

#-------------------------------------------------------------------------------------------------
      def __init__(self, year, month, day, hour, minute, sec):
          if month == 1 or month == 2:
             self.yearp = year - 1 
             self.monthp = month + 12
          else:
             self.yearp = year
             self.monthp = month

          self.year = year
          self.month = month
          self.day = day 
          self.hour = hour
          self.minute = minute
          self.sec = sec 
          self.jd = 0 
          self.time = 0.0 

#-------------------------------------------------------------------------------------------------
      def prnt_dandt(self):
          print ('The date and time are')
          print ('year, month and day are = ',self.calc_year, self.calc_month, self.calc_day)
          print ("hour, minute, and sec are ",self.calc_hour, self.calc_min, self.calc_secs)

#-------------------------------------------------------------------------------------------------
      def getJD(self):
      # This method will calculate the Julian Date (jd) from a calendar date

          # this checks where we are in relation to October 15, 1582, the beginning
          # of the Gregorian calendar.
          if ((self.year < 1582) or
              (self.year == 1582 and self.month < 10) or
              (self.year == 1582 and self.month == 10 and self.day < 15)):
          # before start of Gregorian calendar
              B = 0 
          else:
          # after start of Gregorian calendar
              A = math.trunc(self.yearp / 100.)
              B = 2 - A + math.trunc(A / 4.) 
     
          if self.yearp < 0:
             C = math.trunc((365.25 * self.yearp) - 0.75)
          else:
             C = math.trunc(365.25 * self.yearp)
     
          D = math.trunc(30.6001 * (self.monthp + 1)) 
    
          self.time = (self.hour + ((self.minute + (self.sec/60.0))/60.0))/24.0
          self.jd = B + C + D + self.day + 1720994.5 + self.time

#-------------------------------------------------------------------------------------------------
      def getDate_from_JD(self, jd):
          """
          Convert Julian Day to date.
    
          Algorithm from 'Practical Astronomy with your Calculator or Spreadsheet', 
              4th ed., Duffet-Smith and Zwart, 2011.
    
          Parameters
          ----------
          jd : float
              Julian Day
        
          Returns
          -------
          year : int
              Year as integer. Years preceding 1 A.D. should be 0 or negative.
              The year before 1 A.D. is 0, 10 B.C. is year -9.
        
          month : int
              Month as integer, Jan = 1, Feb. = 2, etc.
    
          day : float
              Day, may contain fractional part.
        
          Examples
          --------
          Convert Julian Day 2446113.75 to year, month, and day.
    
          >>> jd_to_date(2446113.75)
          (1985, 2, 17.25)
    
          """

          jd = jd + 0.5
    
          F, I = math.modf(jd)
          I = int(I)
          A = math.trunc((I - 1867216.25)/36524.25)
    
          if I > 2299160:
             B = I + 1 + A - math.trunc(A / 4.)
          else:
             B = I
        
          C = B + 1524
          D = math.trunc((C - 122.1) / 365.25)
          E = math.trunc(365.25 * D)
          G = math.trunc((C - E) / 30.6001)
          calc_day = C - E + F - math.trunc(30.6001 * G)

          fract_parts = math.modf(calc_day)
          fract_parts_hours = fract_parts[0]

          calc_hours = fract_parts_hours*24.
          calc_hours, calc_hour = math.modf(calc_hours)

          calc_mins = calc_hours*60.
          calc_mins, calc_min = math.modf(calc_mins)

          calc_secs = round(calc_mins*60.,3)

          self.calc_hour = int(calc_hour)
          self.calc_min = int(calc_min)
          self.calc_secs = calc_secs
     
          if G < 13.5:
             calc_month = G - 1
          else:
             calc_month = G - 13
        
          if calc_month > 2.5:
             calc_year = D - 4716
          else:
             calc_year = D - 4715
        
          if calc_month == 1:
            str_month = 'Jan'
          elif calc_month == 2:
            str_month = 'Feb'
          elif calc_month == 3:
            str_month = 'Mar'
          elif calc_month == 4:
            str_month = 'Apr'
          elif calc_month == 5:
            str_month = 'May'
          elif calc_month == 6:
            str_month = 'Jun'
          elif calc_month == 7:
            str_month = 'Jul'
          elif calc_month == 8:
            str_month = 'Aug'
          elif calc_month == 9:
            str_month = 'Sep'
          elif calc_month == 10:
            str_month = 'Oct'
          elif calc_month == 11:
            str_month = 'Nov'
          elif calc_month == 12:
            str_month = 'Dec'
          else:
            print(" !!!  Error - Month is not correct !!!!!")

          #print ("          Date = %i-%s-%i" % (calc_year, str_month, calc_day))
          #print ("          Time = %2i:%2i:%15.12f" % (calc_hour, calc_min, calc_secs))
          self.calc_month = int(calc_month)
          self.calc_day   = int(calc_day)
          self.calc_year  = int(calc_year)


#-------------------------------------------------------------------------------------------------
      def prnt_jd(self):
          print ("Julian Day   =  %7.6f" % self.jd)

#-------------------------------------------------------------------------------------------------
      def update_jd(self, dt):
          self.jd = self.jd + dt
