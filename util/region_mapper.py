# This function checks if the given spatial coordinate is within the region
# of interest

# A region of interest (1 - 13) has been defined here
# https://github.com/polar-computing/AerosolDelta/issues/7

# if the given point doesn't match a region of interest it returns 0

# Expects point to be a shapely.geometry.point
def regionMapper(point):
  if (point.x >= 45 and point.x <= 63 and point.y >= -180 and point.y <= -110):
    return 1

  if (point.x >= 60 and point.y  >= -130 and point.x <= 84 and point.y <=  -62):
    return 2

  if (point.x >= 58 and point.y  >= -75 and point.x <= 85 and point.y <=  -25):
    return 3

  if (point.x >= 61 and point.y  >= -26 and point.x <= 68 and point.y <=  -11):
    return 4

  if (point.x >= 70 and point.y  >= -180 and point.x <= 90 and point.y <=  180):
    return 5

  if (point.x >= 54 and point.y  >= 3 and point.x <= 72 and point.y <=  35):
    return 6

  if (point.x >= 40 and point.y  >= -2 and point.x <= 48 and point.y <=  20):
    return 7

  if (point.x >= 23 and point.y  >= 35 and point.x <= 50 and point.y <=  63):
    return 8

  if (point.x >= 21 and point.y  >= 70 and point.x <= 50 and point.y <=  99):
    return 9

  if (point.x >= -57 and point.y >= -85 and point.x <= 3 and point.y <=  -60):
    return 10

  if (point.x >= -50 and point.y >= 160 and point.x <= -30 and point.y <=  183):
    return 11

  if (point.x >= -90 and point.y >= -180 and point.x <= -55 and point.y <=  180) :
    return 12

  if (point.x >= -4 and point.y >= 29 and point.x <= 2 and point.y <=  38):
    return 13

  return 0
