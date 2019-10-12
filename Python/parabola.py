# y = ax^2 + bx + c  (a != 0)

def find_delta(a, b, c):
    """
    docstring
    """
    # TODO: find delta = b^2 - 4ac
    if a == 0:
        raise Exception("a is 0! [y = ax^2 + bx + c , a != 0]")
    delta = b**2 - 4*a*c
    return delta

def find_vertex(a, b, c):
    """
    docstring
    returns: tuple
    """
    # TODO: find vertex = (- b/2a ; - delta/4a)
    delta = find_delta(a, b, c)
    coor = ( -b/(2*a), -(delta/(4*a)) )
    return coor

def find_focus(a, b, c):
    """
    docstring
    """
    # TODO: find focus = (- b/2a ; 1-delta / 4a)
    pass


f = 350
g = -5
h = 215

print(find_delta(f, g, h)) # -23
x, y = find_vertex(f, g, h)
print(x,"\n", y)
