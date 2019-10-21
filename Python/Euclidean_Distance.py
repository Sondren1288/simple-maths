import math
def euclidean_distance(a, b):
  x = a[0] - b[0]
  y = a[1] - b[1]
  return math.sqrt(x*x + y*y)
  
a = [1 ,1]
b = [2 ,2]

print(euclidean_distance(a,b))
