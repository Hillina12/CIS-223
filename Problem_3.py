# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:34:38 2020

@author: Hillina Mesfin
#This program calculates the batteing average of a baseball player
#The average is calculated by divinding the hits with the at-bats of the player
"""

player_name = input("What is the player's name? ")
hits = int(input ("How many hits? "))
at_bats = int(input ("How many at-bats? "))
batting_average = float((hits / at_bats))

print ()
print (player_name +"'s batting average is ", batting_average)
