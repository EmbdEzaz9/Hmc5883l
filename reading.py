#!/usr/bin/env python

import hmc5883l

compass = hmc5883l.hmc5883l(port=2,address=0x0E,gauss = 4.7, declination = (-2,5))

test1 = compass.heading()
test2 = compass.axes()
test3 = compass.degrees(compass.heading())

print( "deg " ,str(test1))
print( "axes " ,str(test2)
print( "deg/min " ,str(test3)
