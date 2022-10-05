"""
Calculate with different methods the integral of a monomial function
"""

def function(x,k,p): 
    """
    Define the function kx^p
    """
    return k*x**p
    
def primitive(x,k,p):
    """
    Calculate the primitive of a monomial function
    """
    return (x**(p+1))*k/(p+1)
    
def integrale(a,b,k,p):
    """
    Calculate the primitive of a monomial function
    """
    s=primitive(b)-primitive(a)
    return s

def rectangle(f,a,b,N):
    """
    Calculate the integrale of a function f with N precision
    """
    c=(b-a)/N
    s=0
    xi=a
    for i in range (N):
        s+=f(xi)*(xi+c-xi)
        xi+=c
    return s
    
def trapeze(f,a,b,N):
    """
    Calculate better than rectangle the integrale of a function f with N precision
    """
    c=(b-a)/N
    s=0
    xi=a
    for i in range (N):
        s+=((f(xi)+f(xi+c))/2)*(xi+c-xi)
        xi+=c
    return s

"""
print(integrale(0,2,1,2))
print(trapeze(function,0,2,999))
"""