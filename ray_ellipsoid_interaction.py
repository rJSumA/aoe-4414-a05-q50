# ray_ellipsoid_interaction.py
#
# Usage: python3 ray_ellipsoid_interaction.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
#  Determine ray intersection of sphere and ray if it exist
#  Parameters
#  d_l_x: x-component of origin-referenced ray direction
#  d_l_y: y-component of origin-referenced ray direction
#  d_l_z: z-component of origin-referenced ray direction
#  c_l_x: x-component offset of ray origin
#  c_l_y: y-component offset of ray origin
#  c_l_z: z-component offset of ray origin
#  ...
# Output:
#   print(l_d[0]) # x-component of intersection point
#   print(l_d[1]) # y-component of intersection point
#   print(l_d[2]) # z-component of intersection point
#
# Written by Ryo Jumadiao
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# Constants
R_E = 6378.137
e_E = 0.081819221456

# helper functions

## Scalar multiplication
def smul(s,v):
    sprod = []
    for i in range(0,len(v)):
        sprod.append(s*v[i])
    return sprod
    #return [s*e for e in v]

# initialize script arguments
d_l_x = float('nan')
d_l_y = float('nan')
d_l_z = float('nan')
c_l_x = float('nan')
c_l_y = float('nan')
c_l_z = float('nan')

# parse script arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print(\
    'Usage: '\
    'python3 ray_ellipsoid_interaction.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
    )
    exit()

# write script below this line
d_l = [d_l_x, d_l_y, d_l_z] # Musy be Unit Vector
c_l = [c_l_x, c_l_y, c_l_z]
l_d = [0] * 3

##Determinant
a = d_l[0]**2 + d_l[1]**2 + d_l[2]**2 / (1-e_E**2)
b = 2 * (d_l[0]*c_l[0] + d_l[1]*c_l[1] + d_l[2]*c_l[2] / (1 - e_E**2))
c = c_l[0]**2 + c_l[1]**2 + c_l[2]**2 / (1-e_E**2) - R_E**2
discr = b*b-4.0*a*c
print(discr)
##Solution logic -- Solution where discriminant is non-negative
if discr >= 0.0:
    d = (-b-math.sqrt(discr))/(2*a)
    if d < 0.0:
        d = (-b+math.sqrt(discr))/(2*a)
    if d >= 0.0:
        l_d[0] = d * d_l[0] + c_l[0]
        l_d[1] = d * d_l[1] + c_l[1]
        l_d[2] = d * d_l[2] + c_l[2]
        print(l_d[0])
        print(l_d[1])
        print(l_d[2])