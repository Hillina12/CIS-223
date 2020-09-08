# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 13:29:45 2020

@author: Hillina Mesfin
#This program calculates the time it takes for a photo to reach NASA from mars rover
#When mars is closest to Earth's orbit
"""

light_speed = 186000
mars_distance = 34000000

time = (mars_distance / light_speed)

print("The time it takes for a photo to reach NASA from mars rover is: " + str(time)+ " seconds")