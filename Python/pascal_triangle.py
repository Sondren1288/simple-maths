def make_pascal_triangle(number_of_lines):
    """
    make a pascal triangle
    given the number of lines, return a list of the rows
    each row should also be a list, with each item being the respective item in the pascal triangle
    """
    pascal_triangle = [[1], [1, 1]]
    for i in range(2, number_of_lines):
        pascal_triangle.append([1])
        for k in range(i-1):
            pascal_triangle[i].append(pascal_triangle[i-1][k] + pascal_triangle[i-1][k+1])
        pascal_triangle[i].append(1)
    return pascal_triangle
