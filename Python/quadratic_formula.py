#Quadratic formula solver, given values for ax^2 + bx + c = 0

def quadratic(num_a, num_b, num_c):
    quadpoz = (num_b * -1) + (((num_b * num_b) - 4(num_a * num_c))**0.5)
    quadneg = (num_b * -1) - (((num_b * num_b) - 4(num_a * num_c))**0.5)

    quadpoz_sol = quadpoz/(2 * num_a)
    quadneg_sol = quadneg/(2 * num_a)

    quadsol = (quadpoz_sol, quadneg_sol)

    return quadsol