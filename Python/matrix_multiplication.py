#Code for matrix multiplication
def matrix_multiplication():
  m = int(input("Enter the m*m matrix size:"))
  matrix1 = []
  matrix2 = []
  result = []

  print("Enter the entries of matrix1 row wise:")
  for i in range(m):
      a =[]
      for j in range(m):
          a.append(int(input()))
      matrix1.append(a)

  print("Enter the entries of matrix2 row wise:")
  for i in range(m):
      b =[]
      for j in range(m):
          b.append(int(input()))
      matrix2.append(b)

  for i in range(m):
      c =[]
      for j in range(m):
          c.append(0)
      result.append(c)

  for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
      for k in range(len(matrix2)):
        result[i][j] += matrix1[i][k] * matrix2[k][j]

  for r in result:
    print(r)

#To call the function
matrix_multiplication()