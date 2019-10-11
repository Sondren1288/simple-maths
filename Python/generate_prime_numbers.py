

def generate_prime(n): 
  """
    Function to genrate all primes <= n using Sieve method
    @params
    input: number n
    output: list o fall primes <= n.
  """
  primes_list=[]
  prime = [True for i in range(n + 1)] 
  p = 2
  while (p * p <= n): 
    
    
    if (prime[p] == True): 
      
       
      for i in range(p * 2, n + 1, p): 
        prime[i] = False
    p += 1
        
  prime[0]= False
  prime[1]= False
  # Print all prime numbers 
  for p in range(n + 1): 
    if prime[p]: 
      primes_list.append(p)
  return primes_list

# driver program 
#n = 30
#generate_prime(n))
