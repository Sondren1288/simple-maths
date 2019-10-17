
import math
#calulate the area of a quadrilateral with the length of the four sides a,b,c,d and the degrees of an opposite pair of angles
def bretschneider(a,b,c,d,ab,cd):
  p=(a+b+c+d)*0.5
  radsum=(ab+cd)*3.1415926/360
  return ((p-a)*(p-b)*(p-c)*(p-d)-a*b*c*d*math.cos(radsum)**2)**0.5
