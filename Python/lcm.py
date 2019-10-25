#least common multiple of two numbers
def lcm(a,b):
  greater=b if a<b else a
  while(True):
    if((greater%a==0)&(greater%b==0)):
      lcm=greater
      break
    greater+=1
  return lcm

#print(lcm(5,8))